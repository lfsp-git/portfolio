# 🎨 GUIA: Customize Sua GUI v2.1

Este guia mostra como personalizar cada seção da GUI com suas informações reais.

---

## 📸 1. Foto do Perfil

### Localização (HTML):
[public/index.html](public/index.html) - Linha ~47
```html
<img src="https://via.placeholder.com/150" alt="Foto do Leonardo" class="gui-foto">
```

### Como Alterar:

**Opção 1: Upload em um serviço gratuito**
1. Visite [Imgur.com](https://imgur.com) ou [ImgBB.com](https://imgbb.com)
2. Faça upload de sua foto
3. Copie a URL (Direct Link)
4. Substitua no código:
```html
<img src="https://i.imgur.com/YOUR_ID.jpg" alt="Sua Foto" class="gui-foto">
```

**Opção 2: Self-host (Firebase Storage)**
```bash
# 1. Upload via Firebase Console
# 2. Copie a URL pública
# 3. Use:
<img src="https://firebasestorage.googleapis.com/..." alt="Foto">
```

**Opção 3: GitHub (se tiver repo com imagens)**
```html
<img src="https://raw.githubusercontent.com/seu-usuario/repo/main/assets/foto.jpg">
```

---

## 👤 2. Customizar Aba "SOBRE"

### Localização (HTML):
[public/index.html](public/index.html) - Linha ~105-115

### Alterar Biografia:
```html
<!-- ANTES -->
<p class="bio-text">
    Sou um desenvolvedor full-stack apaixonado por <strong>Cibersegurança</strong> ...
</p>

<!-- DEPOIS (seu texto) -->
<p class="bio-text">
    Sou especialista em <strong>DevSecOps</strong> com 5 anos de experiência...
</p>
```

### Customizar Timeline:

```html
<!-- Timeline é composta por 3 itens -->
<div class="timeline-item">
    <div class="timeline-marker">2020</div>
    <div class="timeline-content">
        <h4>Seu Marco 1</h4>
        <p>Descrição...</p>
    </div>
</div>

<!-- Adicionar novo item (copiar/colar bloco acima) -->
<div class="timeline-item">
    <div class="timeline-marker">2023</div>
    <div class="timeline-content">
        <h4>Novo Marco</h4>
        <p>Descrição do que aconteceu em 2023...</p>
    </div>
</div>
```

**Lembretes:**
- Coloque anos em ordem cronológica
- Máximo 5-6 itens (senão fica muito longo)
- Use eventos importantes da sua carreira

---

## 🚀 3. Customizar Aba "PROJETOS"

### Localização (HTML):
[public/index.html](public/index.html) - Linha ~122-180

### Adicionar Novo Projeto:

```html
<!-- Template completo de um card -->
<div class="projeto-card">
    <div class="projeto-icon">🔧</div>  <!-- Mude emoji aqui -->
    <h4>Nome do Seu Projeto</h4>
    <p class="projeto-desc">Descrição clara do que o projeto faz.</p>
    
    <div class="projeto-tech">
        <span>Tecnologia1</span>
        <span>Tecnologia2</span>
        <span>Tecnologia3</span>
    </div>
    
    <a href="https://github.com/SEU_USUARIO/seu-projeto" 
       class="btn-projeto" target="_blank">
        Ver Código →
    </a>
</div>

<!-- Copie este bloco inteiro e cole embaixo do último projeto -->
```

### Remover Projeto:
Apenas delete o `<div class="projeto-card">...</div>` completo.

### Emojis Sugeridos para Projetos:
```
🔍 - Scanner/Análise
🌐 - Website
🐳 - Docker/DevOps
📊 - Dashboard/Analytics
🤖 - Automação/Bot
🔐 - Segurança
📱 - App Mobile
💻 - Software
```

---

## ⚡ 4. Customizar Aba "HABILIDADES"

### Localização (HTML):
[public/index.html](public/index.html) - Linha ~195-280

### Estrutura de uma Habilidade:

```html
<div class="skill-categoria">
    <h4>💻 Backend</h4>
    <div class="skill-bar-grupo">
        
        <!-- CADA HABILIDADE: -->
        <div class="skill-bar">
            <div class="skill-label">Python</div>
            <div class="skill-progress">
                <div class="skill-fill" style="width: 95%"></div>
            </div>
        </div>
        
        <!-- Copie e adapte o bloco acima -->
        
    </div>
</div>
```

### Como Adicionar Skill:

```html
<!-- Copiar APENAS este bloco -->
<div class="skill-bar">
    <div class="skill-label">Nova Linguagem</div>
    <div class="skill-progress">
        <div class="skill-fill" style="width: 80%"></div>
    </div>
</div>
<!-- Colar DENTRO de skill-bar-grupo correspondente -->
```

### Remover Skill:
Delete o bloco `<div class="skill-bar">...</div>` completo.

### Escalas de Proficiência:
```
5% - Iniciante
25% - Básico
50% - Intermediário
75% - Avançado
90% - Especialista
95% - Expert
100% - Dominado (raramente use)
```

### Adicionar Nova Categoria:

```html
<!-- Copiar categoria inteira -->
<div class="skill-categoria">
    <h4>🌐 Frontend</h4>
    <div class="skill-bar-grupo">
        <div class="skill-bar">
            <div class="skill-label">React</div>
            <div class="skill-progress">
                <div class="skill-fill" style="width: 85%"></div>
            </div>
        </div>
    </div>
</div>

<!-- Inserir após a última categoria -->
```

### Emojis para Categorias:
```
💻 - Backend/Programação
🎨 - Frontend/Design
🔐 - Segurança/Pentest
🛠️ - DevOps/Tools
📊 - Data/Analytics
🤖 - IA/ML
🌐 - Web/APIs
```

---

## 📞 5. Customizar Aba "CONTATO"

### Localização (HTML):
[public/index.html](public/index.html) - Linha ~285-330

### Seus Links Sociais:

```html
<!-- Linkedin -->
<a href="https://linkedin.com/in/COLOQUE_SEU_USERNAME" target="_blank" 
   class="contact-card">
    <div class="contact-icon">💼</div>
    <h4>LinkedIn</h4>
    <p>Conecte-se comigo</p>
</a>

<!-- GitHub -->
<a href="https://github.com/COLOQUE_SEU_USERNAME" target="_blank" 
   class="contact-card">
    <div class="contact-icon">🐙</div>
    <h4>GitHub</h4>
    <p>Veja meus projetos</p>
</a>

<!-- Email -->
<a href="mailto:seu-email@gmail.com" class="contact-card">
    <div class="contact-icon">📧</div>
    <h4>Email</h4>
    <p>seu-email@gmail.com</p>
</a>

<!-- Telegram -->
<a href="https://t.me/seu_username" target="_blank" 
   class="contact-card">
    <div class="contact-icon">📱</div>
    <h4>Telegram</h4>
    <p>Chat comigo direto</p>
</a>
```

### Adicionar Novo Contato:

Copie um card inteiro e personalize:

```html
<a href="COLOQUE_URL_AQUI" target="_blank" class="contact-card">
    <div class="contact-icon">EMOJI</div>
    <h4>Nome do Contato</h4>
    <p>Descrição curta</p>
</a>
```

### URLs Úteis:
```
LinkedIn:  https://linkedin.com/in/seu-username
GitHub:    https://github.com/seu-username
Email:     mailto:seu-email@gmail.com
Telegram:  https://t.me/seu_username
Twitter:   https://twitter.com/seu_username
Discord:   https://discord.gg/seu-link
Whatsapp:  https://wa.me/+5511999999999
```

---

## 🎨 6. Customizar Cores Neon

### Localização (CSS):
[public/style.css](public/style.css)

### Cores Principais (Verde Neon):

```css
/* Verde neon padrão */
border: 1px solid #0f0;        /* #0f0 = verde neon */
color: #0f0;
box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);

/* Verde claro/secundário */
color: #3fb950;                 /* #3fb950 = verde mais claro */
```

### Como Trocar Cor:

1. **Opção rápida:** Substituir #0f0 pela sua cor

```css
/* Procure no CSS: */
border: 1px solid #0f0;

/* Substitua globalmente (Ctrl+H no editor) */
#0f0 → #FF00FF   /* Magenta */
#0f0 → #00FFFF   /* Ciano */
#0f0 → #FFFF00   /* Amarelo */
```

2. **Cores Sugeridas:**
```
Verde Neon:     #0f0 ou #00FF00
Ciano:          #00FFFF
Magenta:        #FF00FF
Azul Neon:      #0099FF
Rosa Neon:      #FF00FF
Laranja Neon:   #FF6600
```

3. **Encontrar Todas as Cores no CSS:**

```css
/* Procurar por (Ctrl+F): */
#0f0
#3fb950
rgba(0, 255, 0

/* Substituir padrão */
```

### Exemplo: Trocar para Ciano

```css
/* Antes (verde) */
.tab-btn.ativo {
    background: #0f0;
    color: #000;
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
}

/* Depois (ciano) */
.tab-btn.ativo {
    background: #00FFFF;
    color: #000;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
}
```

---

## 🔤 7. Customizar Nomes & Títulos

### Nome (Header da GUI):
```html
<!-- Antes -->
<h2>Leonardo (Leozin)</h2>

<!-- Depois -->
<h2>Seu Nome (Apelido)</h2>
```

### Subtítulo (Header da GUI):
```html
<!-- Antes -->
<p class="gui-subtitulo">🔐 Desenvolvedor Web & 🛡️ Analista de Segurança</p>

<!-- Depois -->
<p class="gui-subtitulo">Seu Cargo/Titulo Profissional</p>
```

### Títulos das Abas:
Já em português. Se quiser traduzir:

```html
<!-- Botões das abas -->
<button class="tab-btn ativo" data-tab="sobre">
    <span class="icon">👤</span> Sobre
</button>

<!-- Títulos dentro das abas -->
<h3>Quem Sou?</h3>
```

---

## 🧪 8. Testar Suas Mudanças

### Localmente:

```bash
# 1. Editar os arquivos HTML/CSS
# 2. Abrir no navegador
file:///caminho/para/public/index.html

# 3. Ou rodar servidor
python servidor.py
# Acessar: http://localhost:5000
```

### Após Deploy:

```bash
# Sua URL (ex: Firebase Hosting)
https://seu-projeto.web.app

# Digitar no terminal virtual:
gui
```

### Verificar com DevTools:

```
F12 → Inspector
- Verificar HTML está correto
- Verificar CSS foi aplicado
- Verificar elementos visíveis
```

---

## 📋 Checklist de Customização

Antes de fazer deploy final:

- [ ] Foto de perfil alterada
- [ ] Nome personalizado
- [ ] Biografia escrita
- [ ] Timeline com seus marcos
- [ ] Projetos seus listados
- [ ] Skills com suas tecnologias
- [ ] Links sociais corretos
- [ ] Cores customizadas (opcional)
- [ ] Testado em localhost
- [ ] Responsivo em mobile
- [ ] Sem erros de console

---

## 🚀 Deploy Customizado

Após customizar tudo:

```bash
# 1. Teste localmente
python servidor.py
# Vá em http://localhost:5000 e teste a GUI

# 2. Commit das mudanças
git add -A
git commit -m "🎨 Customização v2.1: GUI personalizada"

# 3. Deploy
git push origin main

# 4. Firebase/Netlify fará deploy automático
# Ou manualmente:
firebase deploy --only hosting
# ou
netlify deploy --prod --dir=public
```

---

## 💡 Dicas de Boas Práticas

1. **Descrições Curtas:** Max 100 caracteres por descrição
2. **Consistência:** Use mesmo tom/estilo em todas abas
3. **Links Atualizados:** Verifique todos os links antes de deploy
4. **Imagens Otimizadas:** Comprima fotos antes de upload
5. **Testar Responsivo:** Verifique em mobile, tablet, desktop
6. **UI Consistente:** Não mude cores/fontes aleatoriamente
7. **Acessibilidade:** Use emojis + texto (não só emojis)

---

## ⚠️ Erros Comuns

| Erro | Causa | Solução |
|------|-------|--------|
| Texto não aparece | Sintaxe HTML incorreta | Verificar tags abertas/fechadas |
| Links não funcionam | URL errada | Copiar/colar URL exata |
| Cores estranhas | Cache do navegador | Limpar cache (Ctrl+Shift+Del) |
| Imagem quebrada | URL inválida | Usar URL pública/direta |
| Abas não mudam | JS não carregou | Verificar console (F12) |
| Layout quebrado | CSS não aplica | Verificar seletores CSS |

---

## 🎉 Você Está Pronto!

Agora você pode customizar completamente sua GUI com:
- ✅ Suas informações
- ✅ Suas cores/tema
- ✅ Seus links e contatos
- ✅ Seus projetos

**Próximo:** Faça deploy e compartilhe! 🚀

---

**Dúvidas?** Consulte os arquivos:
- `V2_1_GUI_IMPLEMENTATION.md` - Detalhes técnicos
- `DEPLOYMENT_V2_1.md` - Como fazer deploy
- `README_v2.md` - Documentação geral
