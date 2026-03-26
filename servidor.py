from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import html
import socket
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
import ssl
import sys
import argparse
import requests
import logging
import ipaddress
from datetime import datetime

# ==========================================
# 🔧 CONFIGURAÇÃO INICIAL
# ==========================================
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuração de Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Rate Limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["30 per hour"],
    storage_uri="memory://"
)

# Configurações do Telegram (via variáveis de ambiente)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
CHAT_ID = os.getenv('CHAT_ID', '')

# Configurações de Segurança
ALLOWED_PORTS = list(map(int, os.getenv('ALLOWED_PORTS', '21,22,80,443,3306,8080').split(',')))
TIMEOUT_SECONDS = int(os.getenv('TIMEOUT_SECONDS', '10'))

# ==========================================
# 🛡️ FUNÇÕES UTILITÁRIAS
# ==========================================

def validar_ip(ip):
    """Valida se o IP é legítimo e público."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        # Rejeita IPs privados, loopback, etc
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved:
            return False, "IP privado ou reservado detectado"
        return True, "OK"
    except ValueError:
        return False, "IP inválido"

def validar_url(url):
    """Valida se a URL tem formato válido."""
    try:
        if not url.startswith(('http://', 'https://')):
            url = f'http://{url}'
        from urllib.parse import urlparse
        resultado = urlparse(url)
        if not resultado.netloc:
            return False, "URL inválida"
        return True, url
    except Exception as e:
        return False, str(e)

def criar_contexto_ssl_seguro():
    """Cria contexto SSL seguro e reutilizável."""
    contexto = ssl.create_default_context()
    contexto.check_hostname = False
    contexto.verify_mode = ssl.CERT_NONE
    return contexto

def fazer_requisicao(url, timeout=TIMEOUT_SECONDS):
    """Faz requisição HTTP de forma segura."""
    try:
        contexto = criar_contexto_ssl_seguro()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout, context=contexto) as resposta:
            return resposta.read().decode('utf-8', errors='ignore'), resposta.headers, None
    except HTTPError as e:
        return None, e.headers, str(e)
    except urllib.error.URLError as e:
        logger.warning(f"URL Error: {e}")
        return None, {}, "Alvo rejeitou a conexão"
    except socket.timeout:
        return None, {}, "Timeout na conexão"
    except Exception as e:
        logger.warning(f"Erro na requisição: {e}")
        return None, {}, f"Erro de conexão: {str(e)}"

# ==========================================
# 📡 ROTAS DA API
# ==========================================

@app.route('/', methods=['GET'])
def pagina_inicial():
    """Health check do servidor."""
    logger.info("Health check realizado")
    return jsonify({
        "status": "online",
        "mensagem": "🚀 Servidor Backend do Leozin está Online e operante!",
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route('/enviar', methods=['POST'])
@limiter.limit("5 per minute")
def receber_mensagem():
    """Recebe mensagem e envia para o Telegram."""
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Nenhum dado recebido"}), 400

        nome = html.escape(dados.get('nome', 'Anónimo'))
        mensagem = html.escape(dados.get('mensagem', ''))

        if not mensagem or len(mensagem.strip()) == 0:
            return jsonify({"erro": "A mensagem não pode estar vazia."}), 400

        if len(mensagem) > 1000:
            return jsonify({"erro": "Mensagem muito longa (máx 1000 caracteres)"}), 400

        # Validação de credenciais
        if not TELEGRAM_TOKEN or not CHAT_ID:
            logger.error("Credenciais do Telegram não configuradas")
            return jsonify({"erro": "Erro de configuração do servidor"}), 500

        # Montamos a mensagem
        texto_alerta = f"🚨 *NOVA MENSAGEM DO PORTFÓLIO* 🚨\n\n👤 *Remetente:* {nome}\n💬 *Mensagem:* {mensagem}"
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": texto_alerta,
            "parse_mode": "Markdown"
        }

        resposta = requests.post(url, json=payload, timeout=TIMEOUT_SECONDS)

        if resposta.status_code == 200:
            logger.info(f"Mensagem enviada de {nome}")
            return jsonify({"mensagem": "Mensagem encriptada e enviada com sucesso ao QG!"}), 200
        else:
            logger.warning(f"Telegram retornou status {resposta.status_code}")
            return jsonify({"erro": "Falha ao contactar o QG via satélite."}), 500

    except Exception as e:
        logger.error(f"Erro ao processar mensagem: {e}")
        return jsonify({"erro": "Erro interno do servidor"}), 500


@app.route('/scan', methods=['POST'])
@limiter.limit("10 per hour")
def realizar_scan():
    """Executa port scanning em um IP."""
    try:
        dados = request.get_json()
        if not dados or 'ip' not in dados:
            return jsonify({"erro": "IP não fornecido"}), 400

        ip_alvo = dados.get('ip').strip()

        # Validação do IP
        valido, mensagem = validar_ip(ip_alvo)
        if not valido:
            logger.warning(f"IP inválido: {ip_alvo} - {mensagem}")
            return jsonify({"erro": mensagem}), 400

        logger.info(f"Iniciando scan no IP: {ip_alvo}")
        resultados = []

        for porta in ALLOWED_PORTS:
            sonda = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sonda.settimeout(0.5)
            resultado_conexao = sonda.connect_ex((ip_alvo, porta))

            if resultado_conexao == 0:
                resultados.append({"porta": porta, "status": "ABERTA ⚠️"})
                logger.info(f"Porta {porta} aberta em {ip_alvo}")
            else:
                resultados.append({"porta": porta, "status": "FECHADA 🔒"})
            sonda.close()

        return jsonify({"ip": ip_alvo, "scan": resultados, "timestamp": datetime.now().isoformat()}), 200

    except socket.gaierror:
        logger.warning(f"Hostname inválido: {ip_alvo}")
        return jsonify({"erro": "Host não encontrado"}), 400
    except Exception as e:
        logger.error(f"Erro no scan: {e}")
        return jsonify({"erro": "Erro ao realizar scan"}), 500


@app.route('/headers', methods=['POST'])
@limiter.limit("10 per hour")
def analisar_headers():
    """Analisa headers OWASP de um site."""
    try:
        dados = request.get_json()
        if not dados or 'alvo' not in dados:
            return jsonify({"erro": "URL não fornecida"}), 400

        alvo = dados.get('alvo').strip()

        # Validação da URL
        valida, url = validar_url(alvo)
        if not valida:
            logger.warning(f"URL inválida: {alvo}")
            return jsonify({"erro": url}), 400

        logger.info(f"Analisando headers em: {url}")

        html_content, headers_do_site, erro = fazer_requisicao(url)

        if erro and not headers_do_site:
            return jsonify({"erro": erro}), 400

        resultados = []
        headers_owasp = [
            'Strict-Transport-Security',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Content-Security-Policy'
        ]

        for escudo in headers_owasp:
            if escudo in headers_do_site:
                resultados.append({"header": escudo, "status": "SEGURO 🔒"})
            else:
                resultados.append({"header": escudo, "status": "VULNERÁVEL ⚠️"})

        logger.info(f"Análise completa para: {url}")
        return jsonify({
            "alvo": url,
            "scan": resultados,
            "timestamp": datetime.now().isoformat()
        }), 200

    except Exception as e:
        logger.error(f"Erro na análise de headers: {e}")
        return jsonify({"erro": "Erro ao analisar headers"}), 500


@app.route('/xss', methods=['POST'])
@limiter.limit("10 per hour")
def testar_xss():
    """Testa vulnerabilidade de XSS Reflected."""
    try:
        dados = request.get_json()
        if not dados or 'alvo' not in dados:
            return jsonify({"erro": "URL não fornecida"}), 400

        alvo = dados.get('alvo').strip()

        # Validação da URL
        valida, url = validar_url(alvo)
        if not valida:
            logger.warning(f"URL inválida para XSS test: {alvo}")
            return jsonify({"erro": url}), 400

        logger.info(f"Testando XSS em: {url}")

        payload = "<script>alert('LEOZIN_XSS_TEST')</script>"
        payload_url = urllib.parse.quote(payload)
        url_ataque = f"{url}/?busca={payload_url}"

        html_resposta, _, erro = fazer_requisicao(url_ataque)

        if erro:
            return jsonify({"alvo": url, "status": "ERRO", "detalhe": erro}), 400

        if html_resposta and payload in html_resposta:
            logger.warning(f"XSS encontrado em: {url}")
            return jsonify({
                "alvo": url,
                "status": "VULNERÁVEL ⚠️",
                "detalhe": "Payload refletido no HTML sem sanitização.",
                "timestamp": datetime.now().isoformat()
            }), 200
        else:
            logger.info(f"Site seguro contra XSS: {url}")
            return jsonify({
                "alvo": url,
                "status": "SEGURO 🔒",
                "detalhe": "O site sanitizou os caracteres ou bloqueou o input.",
                "timestamp": datetime.now().isoformat()
            }), 200

    except Exception as e:
        logger.error(f"Erro no teste de XSS: {e}")
        return jsonify({"erro": "Erro ao testar XSS"}), 500


# ==========================================
# 🛠️ MODO CLI
# ==========================================

def cli_port_scan(ip):
    """CLI: Port Scan."""
    valido, msg = validar_ip(ip)
    if not valido:
        print(f"[!] Erro: {msg}")
        return

    print(f"[*] Iniciando CLI Port Scan em: {ip}")
    portas = ALLOWED_PORTS
    for p in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, p)) == 0:
            print(f"[✓] Porta {p}: ABERTA")
        else:
            print(f"[✗] Porta {p}: FECHADA")
        s.close()

def cli_headers_analysis(url):
    """CLI: Headers Analysis."""
    valida, url = validar_url(url)
    if not valida:
        print(f"[!] Erro: URL inválida")
        return

    print(f"[*] Analisando headers em: {url}")
    _, headers, erro = fazer_requisicao(url)

    if erro:
        print(f"[!] Erro: {erro}")
        return

    headers_owasp = [
        'Strict-Transport-Security',
        'X-Frame-Options',
        'X-Content-Type-Options',
        'Content-Security-Policy'
    ]

    for header in headers_owasp:
        status = "✓ SEGURO" if header in headers else "✗ VULNERÁVEL"
        print(f"[{status}] {header}")

# ==========================================
# 🚀 PONTO DE ENTRADA
# ==========================================

if __name__ == '__main__':
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="LFSP Security Tool - CLI Mode")
        parser.add_argument("--scan", help="Executa Port Scan no IP informado")
        parser.add_argument("--headers", help="Analisa Headers OWASP da URL informada")

        args = parser.parse_args()

        if args.scan:
            cli_port_scan(args.scan)
        elif args.headers:
            cli_headers_analysis(args.headers)
    else:
        # Modo Web
        port = int(os.environ.get('PORT', 5000))
        logger.info(f"Iniciando servidor na porta {port}")
        app.run(host='0.0.0.0', port=port, debug=False)