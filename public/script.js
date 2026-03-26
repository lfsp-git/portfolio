// ==========================================
// 0. CONFIGURAÇÕES GLOBAIS
// ==========================================
// URL base da API - adapta-se ao ambiente (localhost ou produção)
const API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000'
    : 'https://portfolio-wmf7.onrender.com';

// ==========================================
// 1. O EFEITO MATRIX
// ==========================================
const canvas = document.getElementById('matrix');
const contexto = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレゲゼデベペオォコソトノホモヨョロゴゾドボポヴッン';
const tamanhoFonte = 16;
const colunas = canvas.width / tamanhoFonte;
const gotas = [];
for (let x = 0; x < colunas; x++) gotas[x] = 1;

function desenharMatrix() {
    contexto.fillStyle = 'rgba(0, 0, 0, 0.05)';
    contexto.fillRect(0, 0, canvas.width, canvas.height);
    contexto.fillStyle = '#0F0';
    contexto.font = tamanhoFonte + 'px monospace';

    for (let i = 0; i < gotas.length; i++) {
        const texto = letras.charAt(Math.floor(Math.random() * letras.length));
        contexto.fillText(texto, i * tamanhoFonte, gotas[i] * tamanhoFonte);
        if (gotas[i] * tamanhoFonte > canvas.height && Math.random() > 0.975) gotas[i] = 0;
        gotas[i]++;
    }
}
setInterval(desenharMatrix, 33);

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// ==========================================
// 2. O INTERPRETADOR DE COMANDOS DO TERMINAL
// ==========================================
const terminalLog = document.getElementById('tela-log');
const terminalInput = document.getElementById('terminal-input');

// Função base para imprimir mensagens no ecrã (terminal)
function escreverLog(mensagem, classeHtml = "") {
    terminalLog.innerHTML += `<p class="${classeHtml}">${mensagem}</p>`;
    terminalLog.scrollTop = terminalLog.scrollHeight; 
}

// O "Ouvinte" que espera o usuário apertar a tecla ENTER
terminalInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const comandoCompleto = this.value.trim();
        if (comandoCompleto === '') return; // Ignora se o usuário der Enter no vazio
        
        // Imprime o que o usuário digitou na tela para simular um terminal real
        escreverLog(`root@lfsp-sec:~# ${comandoCompleto}`, 'texto-comando');
        
        // Manda o texto para ser interpretado
        processarComando(comandoCompleto);
        
        // Limpa a barra de digitação
        this.value = ''; 
    }
});

// O Cérebro que traduz o texto para ações
function processarComando(texto) {
    const partes = texto.split(' ');
    const acao = partes[0].toLowerCase();
    const alvo = partes[1]; 
    
    // Captura tudo o que vem depois do comando (útil para mensagens longas)
    const restoDoTexto = texto.substring(acao.length).trim(); 

    switch (acao) {
        case 'help':
            escreverLog(`>_ COMANDOS DISPONÍVEIS:`, 'texto-sucesso');
            escreverLog(`>_ whoami         - Exibe o meu currículo e habilidades`);
            escreverLog(`>_ contact        - Mostra os meus links de contato`);
            escreverLog(`>_ msg [texto]    - Envia uma mensagem para o meu Telegram`);
            escreverLog(`>_ gui            - Inicia a Interface Gráfica de Usuário (Modo Visual)`);
            escreverLog(`>_ clear          - Limpa a tela do terminal`);
            break;

        case 'gui':
            escreverLog(`>_ [!] Alternando para Interface Gráfica de Usuário (GUI)...`, 'texto-sucesso');
            setTimeout(() => {
                // Desabilita snap scroll para melhor UX
                document.querySelector('.scroll-container').classList.add('disable-snap');
                document.getElementById('tela-scanner').classList.add('oculto');
                document.getElementById('portfolio-gui').classList.remove('oculto');
                // Scroll suave até a GUI
                document.getElementById('portfolio-gui').scrollIntoView({ behavior: 'smooth', block: 'center' });
            }, 800);
            break;

        case 'clear':
            terminalLog.innerHTML = '';
            break;

        case 'whoami':
            escreverLog(`>_ --------------------------------------------------`);
            escreverLog(`>_ NOME: Leonardo (Leozin)`, 'texto-sucesso');
            escreverLog(`>_ CARGO: Desenvolvedor Web & Entusiasta de Cibersegurança`);
            escreverLog(`>_ SKILLS: Python, JavaScript, Docker, Pentest Web, DevSecOps`);
            escreverLog(`>_ MISSÃO: Construir código limpo e defender o ciberespaço.`);
            escreverLog(`>_ --------------------------------------------------`);
            break;

        case 'contact':
            escreverLog(`>_ [ LINKEDIN ]: linkedin.com/in/leonardofsp`, 'texto-sucesso');
            escreverLog(`>_ [ GITHUB   ]: github.com/lfsp-git`, 'texto-sucesso');
            escreverLog(`>_ [ EMAIL    ]: svmpvix@gmail.com`, 'texto-sucesso');
            escreverLog(`>_ DICA: Use o comando 'msg SeuNome | Sua Mensagem' para me mandar um alerta direto!`);
            break;

        case 'msg':
            if (!restoDoTexto.includes('|')) { 
                escreverLog(`[-] FORMATO INVÁLIDO. Use: msg Seu Nome | Sua mensagem aqui`, 'texto-alerta'); 
                return; 
            }
            // Divide o texto na barra vertical "|"
            const [nomeRemetente, mensagemRemetente] = restoDoTexto.split('|');
            enviarMensagem(nomeRemetente.trim(), mensagemRemetente.trim());
            break;

        default:
            escreverLog(`[-] Comando não reconhecido: '${acao}'. Digite 'help' para ajuda.`, 'texto-alerta');
    }
}

// ==========================================
// 3. ENVIAR MENSAGEM PARA TELEGRAM
// ==========================================
function enviarMensagem(nome, mensagem) {
    escreverLog(`>_ [+] Criptografando e enviando pacote para o QG de Leonardo...`);
    
    fetch(`${API_BASE_URL}/enviar`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome: nome, mensagem: mensagem }) 
    })
    .then(resposta => {
        if(!resposta.ok) {
            throw new Error(`HTTP ${resposta.status}`);
        }
        return resposta.json();
    })
    .then(dados => {
        if(dados.mensagem) {
            escreverLog(`>_ [✓] SUCESSO: ${dados.mensagem}`, "texto-sucesso");
        } else if(dados.erro) {
            escreverLog(`>_ [-] ERRO: ${dados.erro}`, "texto-alerta");
        } else {
            escreverLog(`>_ [-] ERRO: Resposta inválida do servidor`, "texto-alerta");
        }
    })
    .catch(erro => {
        escreverLog(`>_ [-] ERRO: QG Incomunicável (${erro.message}). Tente pelo LinkedIn!`, "texto-alerta");
    });
}

// ==========================================
// 4. CONTROLES DA INTERFACE GRÁFICA (GUI)
// ==========================================

// Sistema de Abas da GUI
const tabButtons = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

function abrirAba(nomeAba) {
    // Remove classe 'ativo' de todos os botões e conteúdos
    tabButtons.forEach(btn => btn.classList.remove('ativo'));
    tabContents.forEach(content => content.classList.remove('ativo'));

    // Adiciona 'ativo' ao botão e conteúdo selecionados
    document.querySelector(`.tab-btn[data-tab="${nomeAba}"]`).classList.add('ativo');
    document.getElementById(nomeAba).classList.add('ativo');
}

// Event listeners para os botões de aba
tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const tab = btn.getAttribute('data-tab');
        abrirAba(tab);
    });
});

// Botão voltar ao terminal
document.getElementById('btn-voltar-terminal').addEventListener('click', () => {
    // Re-habilita snap scroll
    document.querySelector('.scroll-container').classList.remove('disable-snap');
    document.getElementById('portfolio-gui').classList.add('oculto');
    document.getElementById('tela-scanner').classList.remove('oculto');
    escreverLog(`>_ [✓] Sessão GUI encerrada. Modo texto restaurado.`, 'texto-sucesso');
    terminalInput.focus();
});

// Botão voltar ao terminal a partir da aba contato
const btnBackFromContact = document.getElementById('btn-back-to-terminal-from-contact');
if (btnBackFromContact) {
    btnBackFromContact.addEventListener('click', () => {
        // Re-habilita snap scroll
        document.querySelector('.scroll-container').classList.remove('disable-snap');
        document.getElementById('portfolio-gui').classList.add('oculto');
        document.getElementById('tela-scanner').classList.remove('oculto');
        escreverLog(`>_ [✓] Sessão GUI encerrada. Modo texto restaurado.`, 'texto-sucesso');
        terminalInput.focus();
    });
}