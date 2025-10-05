/**
 * main.js
 * Funcionalidades interativas para o site BioSpace.
 */

// ----------------------------------------------------
// 1. SCROLL SPY E DESTAQUE DO LINK ATIVO
// ----------------------------------------------------

// Define as seções observadas. Os IDs devem corresponder aos IDs das tags <section> no HTML.
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-links a');

// Configuração do Intersection Observer
const observerOptions = {
    root: null, // O viewport (janela de visualização) é o root
    rootMargin: '0px',
    // O threshold define a porcentagem da seção que deve estar visível
    // para ser considerada "ativa". 0.3 = 30%
    threshold: 0.3 
};

/**
 * Atualiza o destaque da navbar quando uma nova seção entra/sai do viewport.
 * @param {IntersectionObserverEntry[]} entries - Lista de elementos observados.
 */
function handleIntersect(entries) {
    entries.forEach(entry => {
        const targetId = entry.target.id;
        // Encontra o link na navbar que corresponde ao ID da seção visível
        const targetLink = document.querySelector(`.nav-links a[data-target="${targetId}"]`);
        
        if (entry.isIntersecting) {
            // Remove o destaque de todos os links primeiro
            navLinks.forEach(link => link.classList.remove('active'));
            
            // Adiciona o destaque ao link da seção que está visível
            if (targetLink) {
                targetLink.classList.add('active');
            }
        }
    });
}

// Cria e inicia o Observer para todas as seções
const observer = new IntersectionObserver(handleIntersect, observerOptions);

sections.forEach(section => {
    // Apenas observamos as seções que têm links correspondentes na navbar
    if (section.id === 'research' || section.id === 'discoveries' || section.id === 'missions-section') {
        observer.observe(section);
    }
});


// ----------------------------------------------------
// 2. ROLAGEM SUAVE (Função principal de navegação)
// ----------------------------------------------------

/**
 * FUNÇÃO PRINCIPAL: Controla a navegação e o clique de todos os botões e cards.
 * @param {string} target - Nome da ação ou ID da seção de destino.
 */
function handleNavigation(target) {
    // 1. Lógica de Rolagem Suave para links internos
    const section = document.getElementById(target);
    
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
        return; // Sai da função após a rolagem
    }

    // 2. Lógica de Alerta (para simular outras ações como ir para uma nova página ou formulário)
    alert(`Ação Executada! O item "${target.toUpperCase().replace(/-/g, ' ')}" foi clicado.`);
    console.log('Navegação/Ação:', target);
}

// Expõe a função para que os botões com "onclick" no HTML possam usá-la
window.handleNavigation = handleNavigation;

// ----------------------------------------------------
// 3. MELHORIAS NA UX
// ----------------------------------------------------

// Adiciona cursor de clique para os cards
document.querySelectorAll('.research-card, .discovery-card, .mission-card, .btn').forEach(element => {
    element.style.cursor = 'pointer'; 
});

// Adiciona a rolagem suave aos links da navbar (usa a função handleNavigation)
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        const targetId = this.getAttribute('data-target');
        if (targetId) {
            e.preventDefault();
            handleNavigation(targetId);
        }
    });
});