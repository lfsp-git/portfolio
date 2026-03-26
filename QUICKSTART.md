# 🚀 COMECE AQUI - QUICKSTART EM 5 MINUTOS

## Para Windows 10/11

### Opção 1: Automático (Recomendado)
```batch
# 1. Abra PowerShell na pasta do projeto
# 2. Execute:
.\setup.bat

# 3. Edite o arquivo .env com suas credenciais
# 4. Inicie o servidor:
python servidor.py
```

### Opção 2: Manual

```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Copiar arquivo de exemplo
copy .env.example .env

# 5. Editar .env com suas credenciais
# (Abrir com Bloco de Notas e preencher)

# 6. Rodar servidor
python servidor.py

# 7. Acessar em http://localhost:5000
```

---

## Para Mac/Linux

### Opção 1: Automático
```bash
chmod +x setup.sh
./setup.sh
```

### Opção 2: Manual
```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar ambiente
source venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Copiar arquivo de exemplo
cp .env.example .env

# 5. Editar .env
nano .env
# Preencha TELEGRAM_TOKEN e CHAT_ID

# 6. Salve com Ctrl+X, Y, Enter

# 7. Rodar servidor
python servidor.py

# 8. Acessar em http://localhost:5000
```

---

## 📋 Checklist Final

- [ ] `.env` criado e preenchido corretamente
- [ ] `pip install -r requirements.txt` executado
- [ ] Servidor rodando: `python servidor.py`
- [ ] Browser acessando: `http://localhost:5000`
- [ ] Testes passando: `pytest test_servidor.py -v`

---

## ⚠️ Se algo der errado

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "ConnectionRefusedError: [Errno 111]"
- Certifique-se que o servidor está rodando em outro terminal

### TELEGRAM_TOKEN inválido
- Gere um novo token: https://t.me/BotFather
- Copie para o arquivo `.env`

### Erro: "Address already in use"
```bash
# A porta 5000 já está em uso, altere:
python servidor.py  # ou
export FLASK_PORT=5001 && python servidor.py
```

---

## 🎯 Teste rápido da API

Com o servidor rodando, abra outro terminal:

```bash
# Teste 1: Health Check
curl http://localhost:5000/

# Teste 2: Port Scan
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"ip": "8.8.8.8"}'

# Teste 3: Headers
curl -X POST http://localhost:5000/headers \
  -H "Content-Type: application/json" \
  -d '{"alvo": "google.com"}'
```

---

## 📞 Suporte

Se tiver problemas:
1. Leia `README_v2.md` (seção "Como Instalar")
2. Verifique `ROADMAP.md` (seção "Troubleshooting")
3. Rode os testes: `pytest test_servidor.py -v`

---

**Pronto para começar! 🎉**
