from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import html
import requests
import logging
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



# ==========================================
# 🚀 PONTO DE ENTRADA
# ==========================================

if __name__ == '__main__':
    # Modo Web (padrão)
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Iniciando servidor na porta {port}")
    app.run(host='0.0.0.0', port=port, debug=False)