@echo off
REM Quick Start Script for Portfolio v2.0 - Windows Edition
REM Execute este script para configurar tudo automaticamente!

cls
echo.
echo ==========================================
echo 🚀 SETUP PORTFOLIO v2.0 - WINDOWS
echo ==========================================
echo.

REM 1. Criar ambiente virtual
echo 📦 [1/5] Criando ambiente virtual...
python -m venv venv
if errorlevel 1 (
    echo ❌ Erro ao criar venv. Verifique se Python está instalado!
    pause
    exit /b 1
)

REM 2. Ativar ambiente
echo 💻 [2/5] Ativando ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Erro ao ativar venv!
    pause
    exit /b 1
)

REM 3. Instalar dependências
echo 📚 [3/5] Instalando dependências...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erro ao instalar dependências!
    pause
    exit /b 1
)

REM 4. Criar arquivo .env
echo 🔐 [4/5] Criando arquivo .env...
if not exist .env (
    copy .env.example .env
    echo ✅ .env criado. EDITE COM SUAS CREDENCIAIS!
) else (
    echo ⚠️  .env já existe, usando existente
)

REM 5. Rodar testes
echo 🧪 [5/5] Rodando testes...
pytest test_servidor.py -v --tb=short

REM 6. Resumo
cls
echo.
echo ==========================================
echo ✨ SETUP COMPLETO! ✨
echo ==========================================
echo.
echo 📋 PRÓXIMOS PASSOS:
echo.
echo 1️⃣  Edite o arquivo .env
echo    (Botão direito → Abrir com → Bloco de Notas)
echo    - TELEGRAM_TOKEN (do BotFather)
echo    - CHAT_ID (seu ID do Telegram)
echo.
echo 2️⃣  Inicie o servidor:
echo    python servidor.py
echo.
echo 3️⃣  Acesse no navegador:
echo    http://localhost:5000
echo.
echo 4️⃣  Rode os testes:
echo    pytest test_servidor.py -v
echo.
echo 📖 DOCUMENTAÇÃO:
echo    - README_v2.md (Overview)
echo    - ROADMAP.md (Melhorias)
echo    - IMPLEMENTATION_SUMMARY.md (Mudanças)
echo.
echo ==========================================
echo.
pause
