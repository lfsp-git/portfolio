#!/bin/bash
# Quick Start Script para Portfolio v2.0
# Execute este script para configurar tudo automaticamente!

echo "🚀 Iniciando setup do Portfolio v2.0..."
echo ""

# 1. Criar ambiente virtual
echo "📦 [1/5] Criando ambiente virtual..."
python -m venv venv

# 2. Ativar ambiente (platform-specific)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    echo "💻 Sistema Windows detectado"
    source venv/Scripts/activate
else
    echo "🐧 Sistema Linux/Mac detectado"
    source venv/bin/activate
fi

# 3. Instalar dependências
echo "📚 [2/5] Instalando dependências..."
pip install -r requirements.txt

# 4. Criar arquivo .env
echo "🔐 [3/5] Criando arquivo .env..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ .env criado. POR FAVOR, edite com suas credenciais!"
else
    echo "⚠️  .env já existe, usando existente"
fi

# 5. Rodar testes
echo "🧪 [4/5] Rodando testes..."
pytest test_servidor.py -v --tb=short

# 6. Resumo
echo ""
echo "✨ [5/5] Setup Completo! ✨"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 PRÓXIMOS PASSOS:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1️⃣  Edite o arquivo .env com suas credenciais:"
echo "   - TELEGRAM_TOKEN (obtenha do BotFather)"
echo "   - CHAT_ID (seu ID do Telegram)"
echo ""
echo "2️⃣  Inicie o servidor:"
echo "   python servidor.py"
echo ""
echo "3️⃣  Acesse em seu navegador:"
echo "   http://localhost:5000"
echo ""
echo "4️⃣  Rode os testes a qualquer momento:"
echo "   pytest test_servidor.py -v"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📖 Leia a documentação:"
echo "   - README_v2.md (Overview do projeto)"
echo "   - ROADMAP.md (Melhorias futuras)"
echo "   - IMPLEMENTATION_SUMMARY.md (O que foi mudado)"
echo ""
echo "💡 Dica: Mantenha o venv ativado!"
echo ""
