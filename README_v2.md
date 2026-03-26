# 🛡️ Portfólio de Leonardo Fernando Sampaio Pena - v2.0

## OWASP 10 Security & Development Portfolio

Bem-vindo ao meu laboratório de Cibersegurança e Desenvolvimento Full-Stack **REFATORADO E SECURIZADO**. Uma ferramenta ativa de reconhecimento de rede com implementação de boas práticas de segurança.

---

## 📋 MELHORIAS IMPLEMENTADAS (v2.0)

### 🔒 Segurança

✅ **Remoção de Credenciais Exposure**
- Credenciais agora em variáveis de ambiente (`.env`)
- Nunca mais expostas no código-fonte
- Suporte a diferentes ambientes (dev, prod)

✅ **Validação Robusta de Entrada**
- Validação de IPs públicos (rejeita privados, loopback, reservados)
- Validação de URLs com parsing correto
- Escape de HTML em inputs do usuário

✅ **Rate Limiting**
- Máximo 5 mensagens por minuto
- Máximo 10 scans/análises por hora
- Proteção contra abuso e DDoS

✅ **Tratamento de Erros Seguro**
- Erros não expõem detalhes da infraestrutura
- Logging estruturado com Python logging
- Mensagens de erro genéricas ao usuário

### 🎯 Performance & Qualidade

✅ **Refatoração de Código**
- Eliminação de redundância (SSL context reutilizável)
- Funções utilitárias extraídas (`validar_ip`, `validar_url`, `fazer_requisicao`)
- Código DRY (Don't Repeat Yourself)

✅ **Logging Estruturado**
- Rastreamento de operações
- Diferentes níveis de log (INFO, WARNING, ERROR)
- Timestamps para auditoria

✅ **CLI Aprimorado**
- Port scan via terminal com validação
- Análise de headers via CLI
- Integração com modo web

### 🧪 Testes

✅ **Suite de Testes Automatizados**
- 20+ testes de funcionalidade
- Testes de validação de entrada
- Testes de segurança
- Testes de integração
- Cobertura de casos de erro

### 🎨 Frontend

✅ **JavaScript Bug Fix**
- Corrigido typo `escreverLogescreverLog` → `escreverLog`

✅ **CSS Completo**
- Responsividade mobile-first
- Scrollbar customizado
- Animações adicionais
- Media queries para 768px e 480px

---

## 📡 Arquitetura do Sistema

### Duas Camadas de Operação

**Front-end (UI/UX):**
- HTML5, CSS3, JavaScript Vanilla
- Efeito "Matrix Digital Rain" com Canvas API
- Terminal interativo com simulação realista
- Rastreamento de IP público via API externa (`ipify`)
- Scroll Snapping com transições suaves

**Back-end (API REST):**
- Framework `Flask` em Python
- Port Scanner TCP (simula Nmap)
- Análise de Headers OWASP
- Teste de XSS Reflected
- Rate Limiting com Flask-Limiter
- Logging estruturado

---

## 🚀 Funcionalidades

| Feature | Status | Segurança | Descrição |
|---------|--------|-----------|-----------|
| Rastreamento de IP Público | ✅ | ⭐⭐ | Reconhecimento com validação |
| Scanner de Portas TCP | ✅ | ⭐⭐⭐ | Apenas IPs públicos, limite de taxa |
| Análise de Headers OWASP | ✅ | ⭐⭐⭐ | Detecção de headers de segurança |
| Teste de XSS | ✅ | ⭐⭐⭐ | Injeção XSS Reflected com validação |
| Rate Limiting | ✅ | ⭐⭐⭐⭐ | Proteção contra abuso |
| Validação de Entrada | ✅ | ⭐⭐⭐⭐ | Dupla validação (IP/URL) |
| Variáveis de Ambiente | ✅ | ⭐⭐⭐⭐⭐ | Zero credenciais no código |
| Testes Automatizados | ✅ | ⭐⭐⭐⭐ | 20+ testes de qualidade |

---

## 💻 Como Instalar e Rodar

### Pré-requisitos
- Python 3.8+
- pip ou conda

### 1. Clone o Repositório
```bash
git clone <seu-repo>
cd portfolio
```

### 2. Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto:
```env
TELEGRAM_TOKEN=seu_token_aqui
CHAT_ID=seu_chat_id
FLASK_ENV=production
SECRET_KEY=sua_chave_secreta
MAX_REQUESTS_PER_HOUR=30
ALLOWED_PORTS=21,22,80,443,3306,8080
TIMEOUT_SECONDS=10
```

### 5. Execute o Servidor
```bash
python servidor.py
```
Acesse em: `http://localhost:5000`

---

## 🧪 Rodar os Testes

```bash
# Todos os testes
pytest test_servidor.py -v

# Com cobertura
pytest test_servidor.py --cov=. --cov-report=html

# Teste específico
pytest test_servidor.py::TestValidacoes::test_validar_ip_valido -v
```

---

## 📡 Modo CLI (Command Line Interface)

O servidor também pode rodar em modo CLI:

```bash
# Port Scan
python servidor.py --scan 8.8.8.8

# Análise de Headers
python servidor.py --headers google.com

# Modo Web (padrão)
python servidor.py
```

---

## 🔌 Rotas da API

### Health Check
```http
GET /
```
**Resposta:** Status do servidor

### Enviar Mensagem (com Rate Limit: 5/min)
```http
POST /enviar
Content-Type: application/json

{
  "nome": "Seu Nome",
  "mensagem": "Sua mensagem aqui"
}
```

### Port Scanner (com Rate Limit: 10/hora)
```http
POST /scan
Content-Type: application/json

{
  "ip": "8.8.8.8"
}
```

### Análise de Headers (com Rate Limit: 10/hora)
```http
POST /headers
Content-Type: application/json

{
  "alvo": "google.com"
}
```

### Teste de XSS (com Rate Limit: 10/hora)
```http
POST /xss
Content-Type: application/json

{
  "alvo": "exemplo.com"
}
```

---

## 🐳 Deploy com Docker

```bash
# Build
docker build -t portfolio-leo .

# Run
docker run -p 5000:5000 --env-file .env portfolio-leo
```

---

## 📊 Estrutura de Arquivos

```
portfolio/
├── .env                    # Variáveis de ambiente (não commitar!)
├── .gitignore             # Padrões git ignorados
├── .env.example           # Template para .env
├── servidor.py            # Back-end Flask (refatorado)
├── requirements.txt       # Dependências Python
├── test_servidor.py       # Suite de testes
├── Dockerfile             # Containerização
├── firebase.json          # Config Firebase (opcional)
├── README.md              # Esta documentação
└── public/
    ├── index.html         # Front-end HTML5
    ├── style.css          # Estilos (completo)
    ├── script.js          # Lógica JavaScript (bug fix)
    ├── 404.html           # Página 404
```

---

## 🔐 Boas Práticas de Segurança

✅ **Implementadas:**
- ✅ Validação de entrada dupla (IP + URL)
- ✅ Escape HTML em todos os inputs
- ✅ Rate limiting inteligente
- ✅ Variáveis de ambiente para credenciais
- ✅ Logging estruturado para auditoria
- ✅ Rejeição de IPs privados/loopback
- ✅ Tratamento de exceções seguro
- ✅ CORS configurado
- ✅ Testes de segurança automatizados

⚠️ **Pontos de Melhoria Futura:**
- HTTPS em produção (force SSL)
- Autenticação de usuário (JWT/OAuth)
- Banco de dados para histórico de scans
- Cache de resultados com TTL
- Notificações em tempo real (WebSocket)
- API Documentation (Swagger/OpenAPI)

---

## 📞 Contato e Links

- **LinkedIn:** linkedin.com/in/leonardofsp
- **GitHub:** github.com/lfsp-git
- **Email:** svmpvix@gmail.com
- **Telegram:** Via formulário no portfólio

---

## 📄 Licença

MIT License - Sinta-se livre para usar, copiar e modificar este projeto!

---

## 🎯 Changelog

### v2.0 (Atual)
- ✅ Remoção de credenciais expostas
- ✅ Validação robusta de entrada
- ✅ Refatoração completa do código
- ✅ Rate limiting implementado
- ✅ Suite de testes com 20+ testes
- ✅ CSS completamente responsivo
- ✅ Bug fix JavaScript
- ✅ Logging estruturado
- ✅ Documentação melhorada

### v1.0 (Original)
- Funcionalidade básica de scanning
- Interface Matrix
- API Flask simples

---

**Desenvolvido com ❤️ e 🔒 Segurança**
