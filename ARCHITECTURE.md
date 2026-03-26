# 🏗️ ARQUITETURA VISUAL v2.1

## Sistema Geral

```
┌─────────────────────────────────────────────────────────────┐
│                   PORTFOLIO v2.1                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [FRONTEND - Firebase/Netlify]                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ public/index.html                                  │    │
│  │ ├─ Matrix Hero (Canvas)                           │    │
│  │ ├─ Terminal (Xterm style)                         │    │
│  │ └─ GUI (4 ABAS) ⭐                                │    │
│  │    ├─ Sobre (Timeline)                           │    │
│  │    ├─ Projetos (Grid)                            │    │
│  │    ├─ Skills (Progress bars)                      │    │
│  │    └─ Contato (Contact cards)                    │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  [STYLES - public/style.css]                               │
│  ┌────────────────────────────────────────────────────┐    │
│  │ • Matrix effect styling                            │    │
│  │ • Terminal neon (#0f0)                            │    │
│  │ • GUI tabs + animations                           │    │
│  │ • Responsive (480px, 768px, desktop)             │    │
│  │ • Grid/Flexbox layouts                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  [LOGIC - public/script.js]                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │ • Terminal command interpreter                     │    │
│  │ • GUI tab switching (abrirAba)                    │    │
│  │ • API communication (dynamic URL)                 │    │
│  │ • Canvas matrix animation                         │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                         ↓ FETCH ↓                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [BACKEND - Render.com]                                    │
│  ┌────────────────────────────────────────────────────┐    │
│  │ servidor.py (Python/Flask)                         │    │
│  │ ├─ GET /        ← Health check                   │    │
│  │ ├─ POST /enviar  ← Telegram (5/min)             │    │
│  │ ├─ POST /scan    ← Port scan (10/hr)            │    │
│  │ ├─ POST /headers ← OWASP check (10/hr)          │    │
│  │ └─ POST /xss     ← XSS test (10/hr)             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  [SECURITY]                                                  │
│  ├─ Environment variables (.env)                           │
│  ├─ Input validation                                       │
│  ├─ Rate limiting                                          │
│  └─ CORS enabled                                           │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                    EXTERNAL SERVICES                        │
├─────────────────────────────────────────────────────────────┤
│  ├─ 🤖 Telegram Bot (messaging)                            │
│  ├─ 🌐 Various APIs (port scan, headers, XSS)             │
│  └─ 📦 Firebase/Netlify (hosting)                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Fluxo de Dados

### 1. Usuário → Terminal
```
[Usuário digita]
        ↓
[processarComando()]
        ↓
┌─ "gui" ─────→ [abrirAba()] → Mostra GUI profissional
├─ "scan" ────→ [executarPortScan()] → Fetch /scan
├─ "headers" ─→ [executarHeaders()] → Fetch /headers
├─ "xss" ─────→ [executarXSS()] → Fetch /xss
└─ "msg text" → [enviarMensagem()] → Fetch /enviar (Telegram)
        ↓
[Backend processa & responde]
        ↓
[escreverLog() exibe resultado]
```

### 2. GUI Interativa
```
[Usuário clica em aba]
        ↓
[Tab button → addEventListener]
        ↓
[abrirAba(nomeAba)]
        ↓
┌─ Remove classe 'ativo' de todos
├─ Adiciona classe 'ativo' ao botão/conteúdo
├─ CSS @keyframes fadeIn ativa
└─ Conteúdo aparece com animação
        ↓
[Usuário vê: Sobre/Projetos/Skills/Contato]
```

### 3. API Dinâmica
```
[JavaScript executa]
        ↓
[const API_BASE_URL ← Detecta ambiente]
        ↓
┌─ localhost → http://localhost:5000
└─ produção → https://portfolio-wmf7.onrender.com
        ↓
[Fetch com URL dinâmica]
        ↓
[Backend responde em JSON]
        ↓
[JavaScript renderiza resultado]
```

---

## Estrutura de Pastas

```
portfolio/
├── 📄 servidor.py           ← Backend Flask
├── 📄 requirements.txt       ← Dependências Python
├── 📄 .env                   ← Variáveis (CONFIDENCIAL)
├── 📄 .env.example           ← Template de variáveis
├── 📄 Dockerfile             ← Para deploy Docker
├── 📄 firebase.json          ← Config Firebase Hosting
│
├── 📂 public/                ← Frontend (static files)
│   ├── 📄 index.html         ← DOM principal
│   ├── 📄 style.css          ← Estilos (800+ linhas)
│   ├── 📄 script.js          ← Lógica JS
│   ├── 📄 404.html           ← Página erro
│   └── 📷 (imagens aqui)
│
├── 📂 tests/                 ← Testes automatizados
│   └── 📄 test_servidor.py   ← 20+ testes
│
└── 📂 docs/                  ← Documentação
    ├── README_v2.md
    ├── ROADMAP.md
    ├── V2_1_GUI_IMPLEMENTATION.md
    ├── DEPLOYMENT_v2_1.md
    ├── GUI_CUSTOMIZATION.md
    ├── START_HERE_v2_1.md
    ├── QUICK_REFERENCE.md
    ├── QUICKSTART.md
    ├── IMPLEMENTATION_SUMMARY.md
    └── DOCUMENTATION_INDEX.md
```

---

## Componentes da GUI

### Layout Principal
```
┌─────────────────────────────────────────┐
│  [FOTO]  LEONARDO                       │
│          Junior Full Stack Developer     │
├─────────────────────────────────────────┤
│  [SOBRE]  [PROJETOS]  [SKILLS]  [CONTATO] │
├─────────────────────────────────────────┤
│                                           │
│  ┌─ CONTEÚDO DA ABA ATIVA ──┐            │
│  │                           │            │
│  │  (Muda com animação)      │            │
│  │                           │            │
│  └───────────────────────────┘            │
│                                           │
├─────────────────────────────────────────┤
│  [← VOLTAR AO TERMINAL]                 │
└─────────────────────────────────────────┘
```

### Aba: SOBRE
```
┌──────────────────────────────┐
│  Sobre Mim - Timeline        │
├──────────────────────────────┤
│                              │
│  2020 ──o── Comecei          │
│         │      Studies        │
│         │                    │
│  2022 ──o── Primeiro Projeto │
│         │      LaunchPad     │
│         │                    │
│  2024 ──o── Agora            │
│            Full Stack Dev    │
│                              │
│  Bio: Lorem ipsum...         │
└──────────────────────────────┘
```

### Aba: PROJETOS
```
┌──────────────────────────────────────────┐
│  Meus Projetos (Grid 3 colunas)          │
├──────────────────────────────────────────┤
│                                          │
│  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │ Project1 │  │ Project2 │  │ Project3│ │
│  │ Desc     │  │ Desc     │  │ Desc   │ │
│  │ [Link]   │  │ [Link]   │  │ [Link] │ │
│  └──────────┘  └──────────┘  └────────┘ │
│                                          │
│  (Hover: sobe com shadow)               │
└──────────────────────────────────────────┘
```

### Aba: SKILLS
```
┌──────────────────────────────┐
│  Minhas Habilidades          │
├──────────────────────────────┤
│                              │
│  FRONTEND                    │
│  HTML/CSS    ▓▓▓▓▓▓░░  90%  │
│  JavaScript  ▓▓▓▓▓░░░░  80%  │
│  React       ▓▓▓▓░░░░░  75%  │
│                              │
│  BACKEND                     │
│  Python      ▓▓▓▓▓▓░░  85%  │
│  Flask       ▓▓▓▓▓░░░░  80%  │
│  PostgreSQL  ▓▓▓▓░░░░░  70%  │
│                              │
│  (Bar fill animation)        │
└──────────────────────────────┘
```

### Aba: CONTATO
```
┌──────────────────────────────────────┐
│  Vamos Conversar?                    │
├──────────────────────────────────────┤
│                                      │
│  ┌──────────┐  ┌──────────┐         │
│  │ LinkedIn │  │ GitHub   │         │
│  │ /leonar- │  │ /leonardo│         │
│  │   do     │  │   -dev   │         │
│  └──────────┘  └──────────┘         │
│                                      │
│  ┌──────────┐  ┌──────────┐         │
│  │ Email    │  │ Telegram │         │
│  │ leo@...  │  │ @leonardo│         │
│  │          │  │          │         │
│  └──────────┘  └──────────┘         │
│                                      │
│  (Hover: zoom scale 1.05)           │
└──────────────────────────────────────┘
```

---

## Animações CSS

### 1. Tab Transition
```
Tab clicada
    ↓
fadeIn animation (0.4s ease)
    ├─ opacity: 0 → 1
    └─ translateY: 10px → 0
```

### 2. Project Hover
```
Mouse enter
    ↓
    ├─ translateY: -5px (sobe)
    ├─ box-shadow: glow verde
    └─ transition: 0.3s ease
```

### 3. Skill Bar Fill
```
Page load
    ↓
barFill animation (1.5s ease-out)
    ├─ width: 0% → {percentage}%
    └─ Repeat indefinitely com glint
```

### 4. Glow Effect
```
Tab ativo
    ├─ box-shadow: 0 0 10px rgba(0,255,0,0.5)
    └─ text-shadow: glow effect
```

---

## Responsividade

### Desktop (1200px+)
```
┌──────────────────────────────────────────────┐
│  Header com foto lado-a-lado nominal         │
├──────────────────────────────────────────────┤
│  Abas em linha horizontal completa           │
├──────────────────────────────────────────────┤
│  Conteúdo em layout grid otimizado:          │
│  • Timeline 2 colunas alternadas             │
│  • Projetos 3 colunas                        │
│  • Skills em 2 colunas                       │
│  • Contato 4 cards em linha                  │
└──────────────────────────────────────────────┘
```

### Tablet (768px - 1199px)
```
┌──────────────────────────────┐
│  Header stackado              │
├──────────────────────────────┤
│  Abas em 2 linhas             │
├──────────────────────────────┤
│  Conteúdo ajustado:           │
│  • Timeline 1 coluna          │
│  • Projetos 2 colunas         │
│  • Skills em coluna única     │
│  • Contato 2x2 grid           │
└──────────────────────────────┘
```

### Mobile (< 768px)
```
┌─────────────────────┐
│  Header vertical     │
├─────────────────────┤
│  Abas em coluna      │
├─────────────────────┤
│  Conteúdo 100%:      │
│  • Timeline vertical │
│  • Projetos 1 col    │
│  • Skills 1 col      │
│  • Contato 1 col     │
└─────────────────────┘
```

---

## Tecnologias Utilizadas

```
Frontend Stack:
├─ HTML5 (semântico)
├─ CSS3 (animações, grid, flexbox)
├─ Canvas API (matrix effect)
├─ JavaScript ES6+ (vanilla)
├─ Fetch API (AJAX)
└─ DOM API (manipulation)

Backend Stack:
├─ Python 3.8+
├─ Flask 3.0.0
├─ Flask-CORS
├─ Flask-Limiter (rate limiting)
├─ python-dotenv (env vars)
├─ requests (HTTP client)
└─ gunicorn (production server)

DevOps:
├─ Docker (containerização)
├─ Render.com (backend hosting)
├─ Firebase Hosting (frontend)
├─ Git/GitHub (version control)
└─ GitHub Actions (CI/CD)

Testing:
├─ pytest (framework)
├─ pytest-cov (coverage)
└─ unittest (built-in)

Security:
├─ Environment variables
├─ Input validation
├─ Rate limiting (5/min, 10/hr)
├─ CORS (cross-origin)
├─ HTML escape (XSS protection)
└─ HTTPS (in production)
```

---

## Fluxo Completo: Usuário → Resposta

```
1. [FRONTEND]
   Usuário digita "gui" no terminal
            ↓
   JavaScript recebe comando
            ↓
   Chama abrirAba("sobre")
            ↓
   Mostra conteúdo com animação
   
2. [INTERAÇÃO GUI]
   Usuário clica em "Projetos"
            ↓
   Tab button addEventListener dispara
            ↓
   abrirAba("projetos")
            ↓
   Remove .ativo de "sobre"
   Adiciona .ativo a "projetos"
            ↓
   CSS fadeIn anima entrada
   
3. [AÇÃO COM API]
   Usuário clica em "Enviar Mensagem"
            ↓
   enviarMensagem() lê input
            ↓
   Valida conteúdo (not empty)
            ↓
   Fetch para ${API_BASE_URL}/enviar
            ↓
   [BACKEND RECEBE]
   Valida entrada (HTML escape)
            ↓
   Conecta com Telegram Bot
            ↓
   Envia para chat_id
            ↓
   Retorna status JSON
            ↓
   [FRONTEND RECEBE]
   Exibe resposta no terminal
            ↓
   escreverLog("Mensagem enviada!")
```

---

## Status de Implementação

```
v2.0 - Security & Foundation ✅
├─ [✅] .env + validation
├─ [✅] Rate limiting
├─ [✅] Input validation
├─ [✅] Testing suite (20+)
└─ [✅] Documentation

v2.1 - Professional GUI ✅
├─ [✅] 4-tab interface
├─ [✅] Animation system
├─ [✅] Dynamic API URLs
├─ [✅] Responsive design (3 breakpoints)
├─ [✅] Complete CSS (800+ lines)
└─ [✅] Documentation (5 guides)

v2.2+ - Future Features ⏳
├─ [ ] Database integration
├─ [ ] History tracking
├─ [ ] WebSocket updates
├─ [ ] Authentication (JWT/OAuth2)
└─ [ ] Admin dashboard
```

---

## Links Rápidos

📖 **Documentação:**
- [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) ← Índice de tudo
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) ← 3 minutos
- [START_HERE_v2_1.md](START_HERE_v2_1.md) ← Overview
- [V2_1_GUI_IMPLEMENTATION.md](V2_1_GUI_IMPLEMENTATION.md) ← Detalhes técnicos

🛠️ **Implementação:**
- [GUI_CUSTOMIZATION.md](GUI_CUSTOMIZATION.md) ← Personalizar
- [DEPLOYMENT_v2_1.md](DEPLOYMENT_v2_1.md) ← Deploy

📚 **Referência:**
- [README_v2.md](README_v2.md) ← Tudo
- [ROADMAP.md](ROADMAP.md) ← Futuro

---

## Próximos Passos

```
1. ⏱️ 5 min   → Leia QUICK_REFERENCE.md
2. ⚙️ 5 min   → python servidor.py (desenvolver)
3. 🎨 15 min  → GUI_CUSTOMIZATION.md (personalizar)
4. 🚀 5 min   → DEPLOYMENT_v2_1.md (deploy)
5. ✅ 2 min   → Validar em produção

TOTAL: ~32 minutos
```

---

Tudo pronto! 🎉

Escolha seu documento e comece! 🚀
