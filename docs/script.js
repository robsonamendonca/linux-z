const translations = {
    'pt-BR': {
        'nav.features': 'Funcionalidades',
        'nav.howto': 'Como Usar',
        'nav.contribute': 'Contribuir',
        'hero.title': 'Otimize seu Linux com <span>Hardware Precision</span>',
        'hero.subtitle': 'Linux-Z analisa sua CPU, RAM e GPU para recomendar a distribuição perfeita para o seu desempenho.',
        'hero.btn_learn': 'Saiba Mais',
        'features.title': 'Funcionalidades Premium',
        'features.f1.title': 'Detecção Avançada',
        'features.f1.desc': 'Identifica CPU, núcleos, threads, RAM, Armazenamento e GPU com precisão cirúrgica.',
        'features.f2.title': 'Pontuação Inteligente',
        'features.f2.desc': 'Calcula uma pontuação de 0 a 12 baseada na performance real do seu hardware.',
        'features.f3.title': 'Recomendações',
        'features.f3.desc': 'Sugestões personalizadas de distros leves, gamer ou focadas em desenvolvimento.',
        'howto.title': 'Escolha sua interface',
        'howto.cli.desc': 'Interface de terminal elegante alimentada pela biblioteca Rich.',
        'howto.web.desc': 'Painel moderno com modo escuro e design glassmorphism.',
        'contribute.title': 'Como Contribuir',
        'contribute.desc': 'O Linux-Z é um projeto comunitário. Sua ajuda é fundamental para mantermos o banco de dados de distros atualizado!',
        'contribute.opt1.title': 'Código & Backend',
        'contribute.opt1.desc': 'Melhore o algoritmo de detecção ou adicione suporte a novos hardwares.',
        'contribute.opt2.title': 'Banco de Distros',
        'contribute.opt2.desc': 'Atualize o arquivo distros.json com os requisitos mais recentes.',
        'contribute.opt3.title': 'Traduções',
        'contribute.opt3.desc': 'Ajude-nos a levar o Linux-Z para mais idiomas ao redor do mundo.',
        'contribute.step1': 'Fork no GitHub',
        'contribute.step2': 'Feature Branch',
        'contribute.step3': 'Pull Request',
        'contribute.btn_issues': 'Ver Issues',
        'contribute.btn_star': 'Dar uma Estrela',
        'footer.about': 'Analisador de hardware open source inspirado no CPU-Z para a comunidade Linux.',
        'footer.links.title': 'Projeto',
        'footer.comm.title': 'Comunidade'
    },
    'en': {
        'nav.features': 'Features',
        'nav.howto': 'How to Use',
        'nav.contribute': 'Contribute',
        'hero.title': 'Optimize your Linux with <span>Hardware Precision</span>',
        'hero.subtitle': 'Linux-Z analyzes your CPU, RAM, and GPU to recommend the perfect distribution for your performance.',
        'hero.btn_learn': 'Learn More',
        'features.title': 'Premium Features',
        'features.f1.title': 'Advanced Detection',
        'features.f1.desc': 'Identifies CPU, cores, threads, RAM, Storage, and GPU with surgical precision.',
        'features.f2.title': 'Smart Scoring',
        'features.f2.desc': 'Calculates a score from 0 to 12 based on your hardware\'s real performance.',
        'features.f3.title': 'Recommendations',
        'features.f3.desc': 'Personalized suggestions for lightweight, gaming, or dev-focused distros.',
        'howto.title': 'Choose your interface',
        'howto.cli.desc': 'Elegant terminal interface powered by the Rich library.',
        'howto.web.desc': 'Modern dashboard with dark mode and glassmorphism design.',
        'contribute.title': 'How to Contribute',
        'contribute.desc': 'Linux-Z is a community project. Your help is vital to keep the distro database up to date!',
        'contribute.opt1.title': 'Code & Backend',
        'contribute.opt1.desc': 'Improve the detection algorithm or add support for new hardware.',
        'contribute.opt2.title': 'Distro Database',
        'contribute.opt2.desc': 'Update the distros.json file with the latest requirements.',
        'contribute.opt3.title': 'Translations',
        'contribute.opt3.desc': 'Help us bring Linux-Z to more languages around the world.',
        'contribute.step1': 'Fork on GitHub',
        'contribute.step2': 'Feature Branch',
        'contribute.step3': 'Pull Request',
        'contribute.btn_issues': 'View Issues',
        'contribute.btn_star': 'Give a Star',
        'footer.about': 'Open source hardware analyzer inspired by CPU-Z for the Linux community.',
        'footer.links.title': 'Project',
        'footer.comm.title': 'Community'
    }
};

function setLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });

    // Update active button
    document.getElementById('btn-pt').classList.toggle('active', lang === 'pt-BR');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');

    // Update HTML lang attribute
    document.documentElement.lang = lang;

    // Save preference
    localStorage.setItem('preferred-lang', lang);
}

// Event Listeners
document.getElementById('btn-pt').addEventListener('click', () => setLanguage('pt-BR'));
document.getElementById('btn-en').addEventListener('click', () => setLanguage('en'));

// Smooth Scroll for local links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            e.preventDefault();
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Init on Load
window.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('preferred-lang') || 'pt-BR';
    setLanguage(savedLang);
});
