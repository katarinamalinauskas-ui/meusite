import re

def rewrite_modal_in_file(filename, is_he=False):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if is_he:
        questions_html = """
                <!-- Pergunta 1 -->
                <div>
                    <label class="block text-[13px] text-white mb-3 font-semibold">Como as suas horas extras eram tratadas?</label>
                    <div class="space-y-2 font-sans text-[13px] text-white/80">
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Não eram pagas nem iam para banco de horas" required class="accent-brand-gold"> Não eram pagas nem iam para banco de horas</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Batia o ponto e voltava a trabalhar" class="accent-brand-gold"> Batia o ponto e voltava a trabalhar</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Intervalo de almoço reduzido" class="accent-brand-gold"> Intervalo de almoço reduzido</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Trabalho externo/home office sem controle" class="accent-brand-gold"> Trabalho externo/home office sem controle</label>
                    </div>
                </div>
        """
    else:
        questions_html = """
                <!-- Pergunta 1 -->
                <div>
                    <label class="block text-[13px] text-white mb-3 font-semibold">Seu caso se encaixa em qual dessas situações?</label>
                    <div class="space-y-2 font-sans text-[13px] text-white/80">
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Horas extras não pagas" required class="accent-brand-gold"> Horas extras não pagas</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Acidente de trabalho" class="accent-brand-gold"> Acidente de trabalho</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Doença relacionada ao trabalho" class="accent-brand-gold"> Doença relacionada ao trabalho</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Trabalho sem registro" class="accent-brand-gold"> Trabalho sem registro</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Fui demitido por justa causa" class="accent-brand-gold"> Fui demitido por justa causa</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Quero entender rescisão indireta" class="accent-brand-gold"> Quero entender rescisão indireta</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Problema envolvendo gestação" class="accent-brand-gold"> Problema envolvendo gestação</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Outro problema trabalhista" class="accent-brand-gold"> Outro problema trabalhista</label>
                    </div>
                </div>
        """

    new_modal = """
    <!-- ══ Lead Modal — Trabalhador (Mini Diagnóstico Multi-step) ═════ -->
    <div id="leadModal" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/85 backdrop-blur-sm opacity-0 pointer-events-none transition-all duration-300 overflow-y-auto py-10">
        <div class="modal-card bg-[#0E172E] border border-white/10 p-8 rounded-xl max-w-[500px] w-full relative scale-95 transition-transform duration-300 mx-5 shadow-2xl my-auto">
            <button onclick="closeLeadModal()" class="absolute top-4 right-4 text-white/40 hover:text-white transition-colors text-2xl leading-none" aria-label="Fechar">&times;</button>
            
            <div class="g-line mb-4"></div>
            <h3 class="font-serif text-[24px] text-white leading-tight mb-2">Avaliação de Caso</h3>
            <p id="modal-subtitle" class="font-sans text-[13px] text-white/60 mb-6">Preencha seus dados para iniciarmos a análise.</p>
            
            <form id="popup-form" class="space-y-6">
                <input type="hidden" name="pagina" value="%%FILENAME%%">
                <input type="hidden" name="tipo" value="trabalhador">
                <input type="hidden" name="botao" id="popup-botao" value="">
                
                <!-- PASSO 1: DADOS BÁSICOS -->
                <div id="form-step-1" class="space-y-5 transition-all duration-300">
                    <div>
                        <label class="block text-[10px] uppercase tracking-[2px] text-brand-gold mb-1.5 font-semibold">Seu Nome</label>
                        <input type="text" name="nome" id="input-nome" required class="w-full bg-black/20 border border-white/10 rounded px-3 py-3 text-white focus:outline-none focus:border-brand-gold transition-colors font-sans text-[15px]" placeholder="Nome completo">
                    </div>
                    <div>
                        <label class="block text-[10px] uppercase tracking-[2px] text-brand-gold mb-1.5 font-semibold">WhatsApp</label>
                        <input type="tel" name="whatsapp" id="input-whatsapp" required class="w-full bg-black/20 border border-white/10 rounded px-3 py-3 text-white focus:outline-none focus:border-brand-gold transition-colors font-sans text-[15px]" placeholder="(00) 00000-0000">
                    </div>
                    <div>
                        <label class="block text-[10px] uppercase tracking-[2px] text-brand-gold mb-1.5 font-semibold">Profissão / Função</label>
                        <input type="text" name="profissao" id="input-profissao" required class="w-full bg-black/20 border border-white/10 rounded px-3 py-3 text-white focus:outline-none focus:border-brand-gold transition-colors font-sans text-[15px]" placeholder="Sua profissão">
                    </div>
                    <div class="pt-2">
                        <button type="button" id="btn-next-step" class="w-full btn-wa py-4 text-[14px] font-bold rounded-lg shadow-[0_0_20px_rgba(37,211,102,0.2)] hover:shadow-[0_0_30px_rgba(37,211,102,0.4)] transition-all">
                            PRÓXIMO PASSO →
                        </button>
                    </div>
                </div>

                <!-- PASSO 2: DIAGNÓSTICO -->
                <div id="form-step-2" class="space-y-6 hidden opacity-0 transition-opacity duration-300">
                    %%QUESTIONS_HTML%%

                    <!-- Pergunta 2 -->
                    <div>
                        <label class="block text-[13px] text-white mb-3 font-semibold">Quando isso aconteceu?</label>
                        <div class="space-y-2 font-sans text-[13px] text-white/80">
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="quando" value="Está acontecendo agora" required class="accent-brand-gold"> Está acontecendo agora</label>
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="quando" value="Nos últimos 3 meses" class="accent-brand-gold"> Nos últimos 3 meses</label>
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="quando" value="Nos últimos 6 meses" class="accent-brand-gold"> Nos últimos 6 meses</label>
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="quando" value="Há mais de 6 meses" class="accent-brand-gold"> Há mais de 6 meses</label>
                        </div>
                    </div>

                    <!-- Pergunta 3 -->
                    <div>
                        <label class="block text-[13px] text-white mb-3 font-semibold">Você ainda trabalha nessa empresa?</label>
                        <div class="space-y-2 font-sans text-[13px] text-white/80 flex gap-6">
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="ainda_trabalha" value="Sim" required class="accent-brand-gold"> Sim</label>
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="ainda_trabalha" value="Não" class="accent-brand-gold"> Não</label>
                        </div>
                    </div>

                    <!-- Pergunta 4 -->
                    <div>
                        <label class="block text-[13px] text-white mb-3 font-semibold">Você possui documentos ou provas sobre o que aconteceu?</label>
                        <div class="space-y-2 font-sans text-[13px] text-white/80 flex gap-6">
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="tem_provas" value="Sim" required class="accent-brand-gold"> Sim</label>
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="tem_provas" value="Alguns" class="accent-brand-gold"> Alguns</label>
                            <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="tem_provas" value="Não" class="accent-brand-gold"> Não</label>
                        </div>
                    </div>
                    
                    <div class="pt-2">
                        <button type="submit" id="popup-btn" class="w-full btn-wa py-4 text-[14px] font-bold rounded-lg shadow-[0_0_20px_rgba(37,211,102,0.2)] hover:shadow-[0_0_30px_rgba(37,211,102,0.4)] transition-all">
                            AVALIAR MEU CASO NO WHATSAPP
                        </button>
                        <p class="text-center font-sans text-[11px] text-white/30 mt-3">Suas informações são tratadas com sigilo absoluto.</p>
                        
                        <button type="button" id="btn-prev-step" class="w-full text-white/40 hover:text-white font-sans text-[12px] mt-4 text-center transition-colors">
                            ← Voltar e editar dados
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>

    <!-- ══ Sticky Mobile CTA ══════════════════════════════ -->
    <div id="sticky-cta">
        <a href="#" onclick="openLeadModal('Sticky Mobile - Avaliar Caso'); return false;"
           class="btn-wa w-full py-4 text-[14px] font-bold uppercase tracking-wide">
            Avaliar meu caso
        </a>
    </div>

    <!-- ══ SCRIPTS ════════════════════════════════════════ -->
    <script>
        const SHEET_URL = 'https://script.google.com/macros/s/AKfycbyS8jE_tA9oJmk8LRcGfgkf3GABlxyYbfx94NB4ZCR4mY7mNRXJwjLAVYzneejeUKw5SA/exec';
        
        var _botaoLabel = '';

        function openLeadModal(botaoLabel) {
            _botaoLabel = botaoLabel || 'Não identificado';
            const modal = document.getElementById('leadModal');
            const card  = modal.querySelector('.modal-card');
            if(modal && card) {
                modal.classList.remove('opacity-0', 'pointer-events-none');
                card.classList.remove('scale-95');
                card.classList.add('scale-100');
            }
            
            // Reseta para o passo 1 sempre que abrir
            const step1 = document.getElementById('form-step-1');
            const step2 = document.getElementById('form-step-2');
            
            if(step1 && step2) {
                step1.classList.remove('hidden');
                setTimeout(() => step1.classList.remove('opacity-0'), 10);
                
                step2.classList.add('hidden', 'opacity-0');
                document.getElementById('modal-subtitle').innerText = 'Preencha seus dados para iniciarmos a análise.';
            }
        }

        function closeLeadModal() {
            const modal = document.getElementById('leadModal');
            const card  = modal.querySelector('.modal-card');
            if(modal && card) {
                modal.classList.add('opacity-0', 'pointer-events-none');
                card.classList.remove('scale-100');
                card.classList.add('scale-95');
            }
        }

        function toggleFaq(element) {
            const allFaqs = document.querySelectorAll('.faq-item');
            allFaqs.forEach(faq => {
                if (faq !== element && faq.classList.contains('open')) {
                    faq.classList.remove('open');
                }
            });
            element.classList.toggle('open');
        }

        document.addEventListener('DOMContentLoaded', () => {
            // Scroll animations
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(e => {
                    if (e.isIntersecting) {
                        e.target.classList.add('visible');
                        observer.unobserve(e.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
            document.querySelectorAll('.fade-up, .fade-in').forEach(el => observer.observe(el));

            // Navbar shadow on scroll
            const nav = document.getElementById('nav');
            const stickyCta = document.getElementById('sticky-cta');
            window.addEventListener('scroll', () => {
                if(nav) nav.classList.toggle('shadow-lg', window.scrollY > 40);
                const finalCta = document.getElementById('final-cta');
                if (finalCta && stickyCta) {
                    const rect = finalCta.getBoundingClientRect();
                    stickyCta.style.transform = (rect.top < window.innerHeight) ? 'translateY(100%)' : 'translateY(0)';
                }
            }, { passive: true });

            // Progress bar
            const bar = document.getElementById('pbar');
            window.addEventListener('scroll', () => {
                if(bar) bar.style.width = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100) + '%';
            }, { passive: true });

            // Close modal clicking outside
            document.getElementById('leadModal')?.addEventListener('click', function(e) {
                if (e.target === this) closeLeadModal();
            });

            // Lógica Multi-step do Formulário
            const btnNext = document.getElementById('btn-next-step');
            const btnPrev = document.getElementById('btn-prev-step');
            const step1 = document.getElementById('form-step-1');
            const step2 = document.getElementById('form-step-2');
            const inputNome = document.getElementById('input-nome');
            const inputWhats = document.getElementById('input-whatsapp');
            const inputProfissao = document.getElementById('input-profissao');
            const modalSubtitle = document.getElementById('modal-subtitle');

            if(btnNext) {
                btnNext.addEventListener('click', () => {
                    // Validação simples
                    if (!inputNome.value || !inputWhats.value || !inputProfissao.value) {
                        inputNome.reportValidity();
                        inputWhats.reportValidity();
                        inputProfissao.reportValidity();
                        return;
                    }
                    
                    step1.classList.add('opacity-0');
                    setTimeout(() => {
                        step1.classList.add('hidden');
                        step2.classList.remove('hidden');
                        modalSubtitle.innerText = 'Responda as perguntas abaixo para finalizar.';
                        // Reflow
                        void step2.offsetWidth;
                        step2.classList.remove('opacity-0');
                    }, 300);
                });
            }

            if(btnPrev) {
                btnPrev.addEventListener('click', () => {
                    step2.classList.add('opacity-0');
                    setTimeout(() => {
                        step2.classList.add('hidden');
                        step1.classList.remove('hidden');
                        modalSubtitle.innerText = 'Preencha seus dados para iniciarmos a análise.';
                        void step1.offsetWidth;
                        step1.classList.remove('opacity-0');
                    }, 300);
                });
            }

            // Form submit final
            document.getElementById('popup-form')?.addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn  = document.getElementById('popup-btn');
                const form = e.target;

                btn.disabled = true;
                btn.innerHTML = 'Enviando...';
                btn.style.opacity = '0.7';
                
                const nome = form.nome.value;
                const whatsapp = form.whatsapp.value;
                const profissao = form.profissao.value;
                const situacao = form.situacao.value;
                const quando = form.quando.value;
                const aindaTrabalha = form.ainda_trabalha.value;
                const provas = form.tem_provas.value;
                
                const textoWa = `Olá, meu nome é ${nome}. Trabalhei/trabalho como ${profissao} e gostaria de uma avaliação do meu caso.\\n\\nSituação: ${situacao}\\nQuando: ${quando}\\nAinda na empresa: ${aindaTrabalha}\\nPossui provas: ${provas}`;
                const WA_LINK = 'https://wa.me/5511933502503?text=' + encodeURIComponent(textoWa);

                const data = {
                    nome:       nome,
                    whatsapp:   whatsapp,
                    profissao:  profissao,
                    situacao:   situacao,
                    quando:     quando,
                    ainda_trabalha: aindaTrabalha,
                    tem_provas: provas,
                    info_extra: `Profissão: ${profissao} | Situação: ${situacao} | Quando: ${quando} | Ainda Trabalha: ${aindaTrabalha} | Provas: ${provas}`,
                    pagina:     form.pagina.value,
                    tipo:       form.tipo.value,
                    botao:      _botaoLabel
                };

                try {
                    await fetch(SHEET_URL, {
                        method:  'POST',
                        mode:    'no-cors',
                        headers: { 'Content-Type': 'text/plain' },
                        body:    JSON.stringify(data),
                    });
                } catch (_) {}

                window.open(WA_LINK, '_blank');
                closeLeadModal();
                form.reset();
                
                // Volta pro passo 1 em background
                step2.classList.add('hidden', 'opacity-0');
                step1.classList.remove('hidden');
                setTimeout(() => step1.classList.remove('opacity-0'), 10);
                
                btn.disabled = false;
                btn.innerHTML = 'AVALIAR MEU CASO NO WHATSAPP';
                btn.style.opacity = '1';
            });
        });
    </script>
</body>
</html>
    """

    new_modal = new_modal.replace("%%QUESTIONS_HTML%%", questions_html)
    new_modal = new_modal.replace("%%FILENAME%%", filename)

    idx = content.find('<!-- ══ Lead Modal')
    if idx != -1:
        new_content = content[:idx] + new_modal
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)

update_trabalhador = lambda: rewrite_modal_in_file('trabalhador.html', False)
update_horas_extras = lambda: rewrite_modal_in_file('horas-extras.html', True)

if __name__ == '__main__':
    update_trabalhador()
    update_horas_extras()
    print("Atualizado formulário para 2 passos com sucesso!")
