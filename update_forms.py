import os
import re

files_config = {
    'index.html': {
        'tipo': 'trabalhador',
        'wa_msg': 'https://wa.me/5511933502503?text=Ol%C3%A1%2C%20estou%20precisando%20de%20uma%20advogada%20trabalhista',
        'extra_label': 'Sua Profissão / Cargo',
        'extra_placeholder': 'Ex: Vendedor, Motorista...',
        'has_exposed_form': False
    },
    'SITE HORA EXTRA.html': {
        'tipo': 'trabalhador',
        'wa_msg': 'https://wa.me/5511933502503?text=Ol%C3%A1%2C%20estou%20precisando%20de%20uma%20advogada%20trabalhista',
        'extra_label': 'Sua Profissão / Cargo',
        'extra_placeholder': 'Ex: Vendedor, Motorista...',
        'has_exposed_form': True
    },
    'trabalhista-para-empresas.html': {
        'tipo': 'empresarial',
        'wa_msg': 'https://wa.me/5511933502503?text=Ol%C3%A1%2C%20estou%20precisando%20de%20uma%20advogada%20trabalhista%20empresarial',
        'extra_label': 'Nome da Empresa',
        'extra_placeholder': 'Nome da sua empresa',
        'has_exposed_form': True
    },
    'empresarios.html': {
        'tipo': 'empresarial',
        'wa_msg': 'https://wa.me/5511933502503?text=Ol%C3%A1%2C%20estou%20precisando%20de%20uma%20advogada%20trabalhista%20empresarial',
        'extra_label': 'Nome da Empresa',
        'extra_placeholder': 'Nome da sua empresa',
        'has_exposed_form': True
    }
}

modal_template = """
<!-- Lead Modal -->
<div id="leadModal" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/80 backdrop-blur-sm opacity-0 pointer-events-none transition-all duration-300">
    <div class="bg-[#1A1A1A] border border-white/10 p-8 rounded-sm max-w-[420px] w-full relative scale-95 transition-transform duration-300 mx-6 shadow-2xl">
        <button onclick="closeLeadModal()" class="absolute top-4 right-4 text-white/40 hover:text-white transition-colors text-2xl leading-none" aria-label="Fechar">&times;</button>
        <h3 class="font-serif text-[24px] text-white leading-tight mb-2 text-center">Fale com a Advogada</h3>
        <p class="font-sans text-[14px] text-white/60 mb-6 text-center">Preencha rapidamente para ser direcionado ao WhatsApp.</p>
        
        <form id="popup-form" class="space-y-5">
            <input type="hidden" name="pagina" value="{page_name}">
            <input type="hidden" name="tipo" value="{page_type}">
            
            <div>
                <label class="block text-[10px] uppercase tracking-[2px] text-[#C5A059] mb-2 font-semibold">Nome Completo</label>
                <input type="text" name="nome" required class="w-full bg-transparent border-b border-white/20 text-white py-2 focus:outline-none focus:border-[#C5A059] transition-colors font-sans text-[15px]" placeholder="Seu nome">
            </div>
            
            <div>
                <label class="block text-[10px] uppercase tracking-[2px] text-[#C5A059] mb-2 font-semibold">{extra_label}</label>
                <input type="text" name="info_extra" required class="w-full bg-transparent border-b border-white/20 text-white py-2 focus:outline-none focus:border-[#C5A059] transition-colors font-sans text-[15px]" placeholder="{extra_placeholder}">
            </div>
            
            <div>
                <label class="block text-[10px] uppercase tracking-[2px] text-[#C5A059] mb-2 font-semibold">WhatsApp</label>
                <input type="tel" name="whatsapp" required class="w-full bg-transparent border-b border-white/20 text-white py-2 focus:outline-none focus:border-[#C5A059] transition-colors font-sans text-[15px]" placeholder="(00) 00000-0000">
            </div>
            
            <div class="pt-4">
                <button type="submit" id="popup-btn" class="w-full bg-[#C5A059] hover:bg-[#b38d45] text-white py-[15px] text-[15px] font-medium text-center transition-colors rounded-sm">Ir para o WhatsApp →</button>
                <div id="popup-msg" class="hidden mt-3 text-center font-sans text-[13px]"></div>
            </div>
        </form>
    </div>
</div>
"""

js_template = """
<script>
    // URL atualizada enviada pelo usuario
    const SHEET_URL = 'https://script.google.com/macros/s/AKfycbyS8jE_tA9oJmk8LRcGfgkf3GABlxyYbfx94NB4ZCR4mY7mNRXJwjLAVYzneejeUKw5SA/exec';

    function openLeadModal() {{
        const modal = document.getElementById('leadModal');
        const card = modal.querySelector('div');
        modal.classList.remove('opacity-0', 'pointer-events-none');
        card.classList.remove('scale-95');
        card.classList.add('scale-100');
    }}

    function closeLeadModal() {{
        const modal = document.getElementById('leadModal');
        const card = modal.querySelector('div');
        modal.classList.add('opacity-0', 'pointer-events-none');
        card.classList.remove('scale-100');
        card.classList.add('scale-95');
    }}

    document.getElementById('popup-form')?.addEventListener('submit', async function(e) {{
        e.preventDefault();
        const btn = document.getElementById('popup-btn');
        const msg = document.getElementById('popup-msg');
        const form = e.target;

        btn.disabled = true;
        btn.textContent = 'Enviando...';
        btn.style.opacity = '0.7';

        const data = {{
            nome: form.nome.value,
            whatsapp: form.whatsapp.value,
            info_extra: form.info_extra.value,
            pagina: form.pagina.value,
            tipo: form.tipo.value
        }};

        try {{
            await fetch(SHEET_URL, {{
                method: 'POST',
                mode: 'no-cors',
                headers: {{ 'Content-Type': 'text/plain' }},
                body: JSON.stringify(data),
            }});

            window.open("{wa_link}", "_blank");
            closeLeadModal();
            form.reset();
            btn.disabled = false;
            btn.textContent = 'Ir para o WhatsApp →';
            btn.style.opacity = '1';
            
        }} catch (err) {{
            btn.disabled = false;
            btn.textContent = 'Ir para o WhatsApp →';
            btn.style.opacity = '1';
            msg.textContent = 'Erro ao conectar. Redirecionando...';
            msg.classList.remove('hidden');
            msg.className = 'mt-3 text-center font-sans text-[13px] text-red-400 block';
            setTimeout(() => {{
                window.open("{wa_link}", "_blank");
                closeLeadModal();
                msg.classList.add('hidden');
            }}, 1500);
        }}
    }});

    // Close on click outside
    document.getElementById('leadModal')?.addEventListener('click', function(e) {{
        if(e.target === this) closeLeadModal();
    }});
"""

for file_name, cfg in files_config.items():
    with open(file_name, 'r') as f:
        content = f.read()

    # 1. Update WhatsApp links
    # Change any https://wa.me link to open the modal
    content = re.sub(r'href="https://wa\.me/[^"]*"', 'href="#" onclick="openLeadModal(); return false;"', content)
    
    # Change #contato links to open modal
    content = re.sub(r'href="#contato"', 'href="#" onclick="openLeadModal(); return false;"', content)
    
    # 2. If it has exposed form, replace the form div with a CTA
    if cfg['has_exposed_form']:
        if file_name in ['trabalhista-para-empresas.html', 'empresarios.html']:
            # We must only replace the specific form section
            form_regex = re.compile(r'<form id="lead-form".*?</form>', re.DOTALL)
            cta_html = """
            <div class="text-center py-10">
                <div class="w-16 h-16 rounded-full bg-[#C5A059]/10 flex items-center justify-center mx-auto mb-6 text-[#C5A059]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
                        <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c-.003 1.398.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.005-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                    </svg>
                </div>
                <h3 class="font-serif text-[24px] text-white leading-tight mb-3">Atendimento via WhatsApp</h3>
                <p class="font-sans text-[15px] text-white/70 mb-8 leading-relaxed">Clique no botão abaixo para preencher seus dados e ser direcionado automaticamente ao meu WhatsApp.</p>
                <a href="#" onclick="openLeadModal(); return false;" class="btn px-10 py-4 text-[16px] font-medium inline-block">Falar Agora</a>
            </div>
            """
            content = form_regex.sub(cta_html, content)
        elif file_name == 'SITE HORA EXTRA.html':
            form_regex = re.compile(r'<form class="space-y-8 w-full">.*?</form>', re.DOTALL)
            cta_html = """
            <div class="text-center py-10 w-full">
                <div class="w-16 h-16 rounded-full bg-[#1A1A1A] flex items-center justify-center mx-auto mb-6 text-white border border-[#2C2C2A]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
                        <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c-.003 1.398.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.005-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
                    </svg>
                </div>
                <h3 class="font-serif text-[24px] text-white leading-tight mb-3">Atendimento Rápido</h3>
                <p class="font-sans text-[15px] text-[#A1A19A] mb-8 leading-relaxed">Clique no botão abaixo para conversar comigo pelo WhatsApp e tirar suas dúvidas.</p>
                <a href="#" onclick="openLeadModal(); return false;" class="bg-white text-black px-10 py-4 rounded-[4px] font-sans font-medium text-[16px] inline-block hover:bg-gray-200 transition-colors">Falar no WhatsApp</a>
            </div>
            """
            content = form_regex.sub(cta_html, content)

    # 3. Add Modal HTML before </body>
    if '<!-- Lead Modal -->' not in content:
        modal_populated = modal_template.format(
            page_name=file_name,
            page_type=cfg['tipo'],
            extra_label=cfg['extra_label'],
            extra_placeholder=cfg['extra_placeholder']
        )
        content = content.replace('</body>', modal_populated + '\n</body>')

    # 4. Remove old script blocks that handled the form/whatsapp Modal from previous version (WhatsApp Redirect Modal)
    content = re.sub(r'<!-- WhatsApp Redirect Modal -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # 5. Extract existing JS before modifying
    # Instead of deleting all scripts, let's ONLY replace the SHEET_URL script.
    # The SHEET_URL script is usually near the end. Let's find it.
    sheet_url_script_match = re.search(r'<script>\s*const SHEET_URL = .*?</script>', content, re.DOTALL)
    
    js_populated = js_template.format(wa_link=cfg['wa_msg'])
    
    if sheet_url_script_match:
        old_script = sheet_url_script_match.group(0)
        extras = ""
        if 'toggleFaq' in old_script:
            extras += """
    function toggleFaq(el) {
        const isOpen = el.classList.contains('open');
        document.querySelectorAll('.faq-item.open').forEach(item => {
            item.classList.remove('open');
            item.querySelector('.faq-icon').textContent = '+';
        });
        if (!isOpen) {
            el.classList.add('open');
            el.querySelector('.faq-icon').textContent = '×';
        }
    }
"""
        if 'updateNav' in old_script:
            extras += """
    document.addEventListener('DOMContentLoaded', () => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
        document.querySelectorAll('.fade-up, .fade-in').forEach(el => observer.observe(el));

        const nav = document.getElementById('nav');
        if(nav) {
            function updateNav() {
                if (window.scrollY > 60) {
                    nav.style.cssText = 'background:rgba(12,12,12,0.94);backdrop-filter:blur(14px);border-color:rgba(255,255,255,0.06);';
                } else {
                    nav.style.cssText = 'background:transparent;backdrop-filter:none;border-color:transparent;';
                }
            }
            window.addEventListener('scroll', updateNav, { passive: true });
            updateNav();
        }

        const bar = document.getElementById('pbar');
        if(bar) {
            window.addEventListener('scroll', () => {
                bar.style.width = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100) + '%';
            }, { passive: true });
        }
        
        const mobToggle = document.getElementById('mob-toggle');
        const mobMenu = document.getElementById('mob-menu');
        if(mobToggle && mobMenu) {
            mobToggle.addEventListener('click', () => {
                mobMenu.classList.toggle('hidden');
            });
            mobMenu.querySelectorAll('a').forEach(a => {
                a.addEventListener('click', () => {
                    mobMenu.classList.add('hidden');
                });
            });
        }
    });
"""
        js_populated += extras + "\n</script>"
        content = content.replace(old_script, js_populated)
    else:
        # If no SHEET_URL script existed, just append it before body end
        content = content.replace('</body>', js_populated + "\n</script>\n</body>")

    with open(file_name, 'w') as f:
        f.write(content)

print("Updates applied safely to all 4 files.")
