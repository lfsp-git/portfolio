# 🛡️ Portfólio de Leonardo Fernando Sampaio Pena
## OWASP 10 Security & Development Portfolio

Bem-vindo ao meu laboratório de Cibersegurança e Desenvolvimento Full-Stack. Este projeto não é apenas um portfólio, mas uma ferramenta ativa de reconhecimento de rede construída do zero.

## 📡 Arquitetura do Sistema
O projeto é dividido em duas camadas principais, simulando uma operação real de Red Team:
* **Front-end (A Interface UI/UX):** Construído com HTML5, CSS3 e JS (Vanilla). Apresenta um efeito "Matrix Digital Rain" dinâmico no background e um terminal interativo com Scroll Snapping. Ele rastreia o IP público do usuário via API externa (`ipify`).
* **Back-end (A Ogiva):** Um servidor robusto em Python utilizando o framework `Flask`. Ele recebe o IP alvo via requisição POST e utiliza a biblioteca `socket` para realizar varreduras reais de portas TCP (Nmap Simulado), devolvendo os resultados de forma assíncrona.

## 🚀 Funcionalidades
- [x] Rastreamento de IP Público (Reconhecimento).
- [x] Scanner de Portas TCP integrado (Testa portas críticas como 21, 22, 80, 443, 3306, 8080).
- [x] Proteção anti-XSS no Back-end utilizando `html.escape`.
- [x] Rotas de API RESTful com CORS habilitado.

## 💻 Como rodar localmente
1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   ```bash
   pip install flask flask-cors