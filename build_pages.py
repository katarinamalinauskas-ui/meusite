import re

def update_trabalhador():
    with open('trabalhador.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract head (everything before <!-- ══ NAV ══════════════════════════════════════════ -->)
    head_match = re.search(r'(.*?)(?=<!-- ══ NAV)', content, re.DOTALL)
    head = head_match.group(1) if head_match else ''

    # Extract nav (we keep nav)
    nav_match = re.search(r'(<!-- ══ NAV.*?</nav>)', content, re.DOTALL)
    nav = nav_match.group(1) if nav_match else ''

    # Extract map and footer
    footer_match = re.search(r'(<!-- ══ MAPA.*?)(?=<!-- ══ Lead Modal)', content, re.DOTALL)
    footer = footer_match.group(1) if footer_match else ''

    new_body = """
    <!-- ══ URGENCY TOP BAR ════════════════════════════════ -->
    <div class="urgency-strip pt-[72px]">
        <p class="text-center font-sans text-[12px] font-semibold text-brand-dark py-2.5 px-4 tracking-wide">
            ⚖️ Atendimento especializado para trabalhadores com situações trabalhistas concretas.
        </p>
    </div>

    <!-- ══ HERO SECTION ═══════════════════════════════════ -->
    <section class="relative bg-brand-dark flex items-center hero-grid overflow-hidden" style="min-height:calc(100vh - 108px);">
        <!-- Glow orbs -->
        <div class="absolute top-1/3 right-[15%] w-[900px] h-[900px] rounded-full pointer-events-none" style="background:radial-gradient(circle,rgba(212,175,55,.15) 0%,transparent 65%);"></div>
        <div class="absolute bottom-0 left-0 w-[600px] h-[600px] rounded-full pointer-events-none" style="background:radial-gradient(circle,rgba(37,211,102,.1) 0%,transparent 70%);"></div>

        <div class="max-w-[1140px] mx-auto px-6 w-full relative z-10 py-16 lg:py-20">
            <div class="flex flex-col lg:flex-row items-center gap-12 lg:gap-8">
                
                <!-- Text Column -->
                <div class="w-full lg:w-[56%] fade-up">
                    <div class="g-line mb-6"></div>
                    <span class="sec-label block mb-5">Análise de Caso Trabalhista</span>
                    
                    <h1 class="font-serif text-[38px] md:text-[48px] lg:text-[56px] text-white leading-[1.1] mb-6 font-semibold tracking-tight" style="max-width:680px; text-shadow: 0 4px 20px rgba(0,0,0,0.5);">
                        Seu empregador deixou de pagar seus direitos trabalhistas?
                    </h1>
                    
                    <p class="font-sans text-[16px] text-white/80 leading-relaxed mb-6" style="max-width:550px;">
                        Se você trabalha ou trabalhou com carteira assinada e passou por problemas como <strong class="text-white">horas extras não pagas, acidente de trabalho, doença profissional, falta de registro, justa causa, rescisão indireta ou problemas relacionados à gestação</strong>, seu caso pode precisar de uma análise jurídica.
                    </p>
                    
                    <p class="font-sans text-[15px] text-brand-gold font-semibold mb-8">
                        Conte o que aconteceu e veja se sua situação pode ser analisada pela nossa equipe.
                    </p>
                    
                    <!-- CTA Buttons -->
                    <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 mb-7">
                        <a id="hero-cta-primary"
                           href="#" onclick="openLeadModal('Hero - Quero avaliar meu caso'); return false;"
                           class="btn-wa w-fit px-10 py-4 shadow-[0_0_30px_rgba(37,211,102,0.3)] hover:shadow-[0_0_45px_rgba(37,211,102,0.5)] text-[14px] uppercase tracking-wide">
                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16" class="mr-2"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/></svg>
                            QUERO AVALIAR MEU CASO TRABALHISTA
                        </a>
                    </div>
                </div>

                <!-- Photo Column -->
                <div class="w-full lg:w-[44%] flex justify-center lg:justify-end fade-in" style="transition-delay:.2s;">
                    <div class="relative w-full max-w-[360px] lg:max-w-[420px]" style="height:520px;">
                        <div class="absolute -top-10 -right-10 w-[200px] h-[200px] bg-brand-gold/20 blur-[60px] rounded-full z-0 pointer-events-none"></div>
                        <div class="absolute top-4 -right-4 w-full h-full border-2 border-brand-gold/30 rounded-xl z-0"></div>
                        <div class="relative w-full h-full overflow-hidden rounded-xl z-10 border border-white/10 shadow-2xl">
                            <div class="absolute inset-0 bg-gradient-to-t from-[#0B0F19] via-transparent to-transparent z-10"></div>
                            <div class="absolute inset-0 bg-brand-gold/10 mix-blend-overlay z-20"></div>
                            <img src="hero_nova.jpg" alt="Dra. Katarina Malinauskas" class="w-full h-full object-cover object-top scale-105 hover:scale-100 transition-transform duration-1000">
                        </div>
                        <div class="absolute bottom-6 left-6 z-30 bg-brand-dark/90 backdrop-blur-sm border border-white/10 px-5 py-3.5 rounded-md shadow-xl">
                            <p class="font-serif text-white text-[17px] leading-tight">Dra. Katarina Malinauskas</p>
                            <p class="font-sans text-[10px] text-brand-gold/90 tracking-widest uppercase mt-1">OAB/SP nº 338.901</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="absolute bottom-6 left-1/2 -translate-x-1/2 flex flex-col items-center gap-1.5 fade-up" style="transition-delay:.5s;">
            <span class="font-sans text-[9px] uppercase tracking-[2px] text-white/20">Rolar</span>
            <div class="w-px h-7 bg-gradient-to-b from-white/20 to-transparent"></div>
        </div>
    </section>

    <!-- ══ BLOCO DE FILTRO ════════════════════════════════ -->
    <section class="py-16 bg-white border-b border-slate-100">
        <div class="max-w-[960px] mx-auto px-6 fade-up">
            <div class="text-center mb-10">
                <span class="sec-label">Filtro de Atendimento</span>
                <h2 class="font-serif text-[28px] md:text-[36px] text-brand-dark mt-2">Antes de entrar em contato, veja se você está no lugar certo.</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Para quem É -->
                <div class="bg-brand-green/5 border border-brand-green/20 rounded-xl p-8">
                    <h3 class="font-sans font-semibold text-[18px] text-brand-dark mb-5 flex items-center gap-2">
                        <span class="w-6 h-6 rounded-full bg-brand-green text-white flex items-center justify-center text-[14px]">✔</span>
                        Este atendimento é para você se:
                    </h3>
                    <ul class="space-y-4 font-sans text-[14px] text-text-s">
                        <li class="flex items-start gap-3"><span class="text-brand-green font-bold">✓</span> Você é trabalhador ou ex-trabalhador da empresa envolvida</li>
                        <li class="flex items-start gap-3"><span class="text-brand-green font-bold">✓</span> Existe uma situação trabalhista concreta acontecendo ou que aconteceu recentemente</li>
                        <li class="flex items-start gap-3"><span class="text-brand-green font-bold">✓</span> Você quer entender se houve violação dos seus direitos</li>
                        <li class="flex items-start gap-3"><span class="text-brand-green font-bold">✓</span> Está disposto a fornecer informações sobre o que aconteceu</li>
                        <li class="flex items-start gap-3"><span class="text-brand-green font-bold">✓</span> Possui, quando houver, documentos, mensagens, holerites, ou registros de ponto</li>
                    </ul>
                </div>
                
                <!-- Para quem NÃO É -->
                <div class="bg-red-50 border border-red-100 rounded-xl p-8">
                    <h3 class="font-sans font-semibold text-[18px] text-brand-dark mb-5 flex items-center gap-2">
                        <span class="w-6 h-6 rounded-full bg-red-500 text-white flex items-center justify-center text-[14px]">✕</span>
                        Não é para você se:
                    </h3>
                    <ul class="space-y-4 font-sans text-[14px] text-text-s">
                        <li class="flex items-start gap-3"><span class="text-red-500 font-bold">✕</span> Você é empregador procurando orientação para sua empresa</li>
                        <li class="flex items-start gap-3"><span class="text-red-500 font-bold">✕</span> Quer apenas uma informação genérica sobre Direito do Trabalho</li>
                        <li class="flex items-start gap-3"><span class="text-red-500 font-bold">✕</span> Não possui nenhuma situação trabalhista específica para relatar</li>
                        <li class="flex items-start gap-3"><span class="text-red-500 font-bold">✕</span> Está procurando apenas "quanto vou ganhar" sem analisar o caso real</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- ══ BLOCO DE IDENTIFICAÇÃO DE DOR ════════════════ -->
    <section class="py-[88px] bg-brand-alt" id="dores">
        <div class="max-w-[960px] mx-auto px-6 fade-up">
            <div class="text-center mb-14">
                <div class="g-line mx-auto mb-6"></div>
                <span class="sec-label">Diagnóstico de Situação</span>
                <h2 class="font-serif text-[34px] md:text-[44px] text-white mt-4 leading-[1.2] max-w-[640px] mx-auto">
                    Qual dessas situações aconteceu com você?
                </h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-12">
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Você trabalhava além do horário e essas horas não eram pagas?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Se fazia horas extras com frequência e elas não apareciam corretamente no pagamento, seu caso pode precisar de uma análise trabalhista.</p>
                    </div>
                </div>
                
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Sofreu acidente no trabalho?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Você se machucou durante o trabalho ou no trajeto? Teve afastamento, tratamento ou ficou com alguma limitação?</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Trabalhou sem registro?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Você trabalhava como funcionário, mas passou meses trabalhando sem carteira assinada?</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Foi demitido por justa causa?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Recebeu uma justa causa e acredita que a empresa não tinha motivo para aplicar essa penalidade?</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Pediu demissão, mas queria sair por culpa da empresa?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Dependendo do que aconteceu, pode existir diferença entre simplesmente pedir demissão e buscar o reconhecimento de uma rescisão indireta.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Está grávida e teve problemas com a empresa?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Demissão, pressão para pedir desligamento ou outros problemas durante a gestação podem exigir uma análise específica.</p>
                    </div>
                </div>
            </div>

            <!-- Consequência / Urgência -->
            <div class="bg-[#0B0F19] rounded-xl p-8 md:p-10 text-center relative overflow-hidden border border-white/10 shadow-2xl">
                <div class="relative z-10">
                    <span class="text-brand-gold text-3xl mb-4 block">⚠️</span>
                    <h3 class="font-serif text-[24px] md:text-[30px] text-white leading-tight mb-4">
                        Quanto mais tempo passa, mais difícil pode ser reconstruir o que realmente aconteceu.
                    </h3>
                    <p class="font-sans text-[15px] text-white/80 leading-relaxed mb-8 max-w-[700px] mx-auto">
                        Se você trabalhou horas extras, sofreu um acidente, ficou sem registro ou passou por uma situação de demissão que considera irregular, reúna as informações que possui e procure orientação sobre o seu caso.
                    </p>
                    <a href="#" onclick="openLeadModal('Consequencia - Quero avaliar meu caso'); return false;"
                       class="btn-wa px-10 py-4.5 text-[14px] shadow-[0_0_30px_rgba(37,211,102,0.3)] hover:shadow-[0_0_45px_rgba(37,211,102,0.5)] uppercase tracking-wide mx-auto">
                        Quero avaliar meu caso trabalhista
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- ══ BLOCO COMO FUNCIONA ════════════════════════════ -->
    <section class="py-[88px] bg-white border-t border-slate-100">
        <div class="max-w-[1140px] mx-auto px-6 fade-up">
            <div class="text-center mb-16">
                <div class="g-line mx-auto mb-6"></div>
                <h2 class="font-serif text-[34px] md:text-[44px] text-text-p leading-[1.15]">O que acontece depois que você envia seu caso?</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="text-center px-4">
                    <div class="w-16 h-16 rounded-full bg-brand-gold/10 text-brand-gold flex items-center justify-center text-2xl font-bold mx-auto mb-6">1</div>
                    <h3 class="font-sans font-semibold text-[18px] text-text-p mb-3">Você conta o que aconteceu</h3>
                    <p class="font-sans text-[14px] text-text-s leading-relaxed">Envie as principais informações sobre sua relação de trabalho e o problema enfrentado no formulário.</p>
                </div>
                
                <div class="text-center px-4">
                    <div class="w-16 h-16 rounded-full bg-brand-gold/10 text-brand-gold flex items-center justify-center text-2xl font-bold mx-auto mb-6">2</div>
                    <h3 class="font-sans font-semibold text-[18px] text-text-p mb-3">A equipe analisa as informações</h3>
                    <p class="font-sans text-[14px] text-text-s leading-relaxed">A situação é avaliada considerando os fatos apresentados e os documentos que você já possui disponíveis.</p>
                </div>
                
                <div class="text-center px-4">
                    <div class="w-16 h-16 rounded-full bg-brand-gold/10 text-brand-gold flex items-center justify-center text-2xl font-bold mx-auto mb-6">3</div>
                    <h3 class="font-sans font-semibold text-[18px] text-text-p mb-3">Você entende os próximos passos</h3>
                    <p class="font-sans text-[14px] text-text-s leading-relaxed">Se houver elementos para atuação, você recebe orientação clara sobre o caminho adequado para o seu caso.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ══ BLOCO PROVAS ═══════════════════════════════════ -->
    <section class="py-[88px] bg-slate-50 border-t border-slate-100">
        <div class="max-w-[1140px] mx-auto px-6 fade-up">
            <div class="text-center mb-14">
                <div class="g-line mx-auto mb-6"></div>
                <h2 class="font-serif text-[34px] md:text-[44px] text-text-p leading-[1.15]">Casos Reais</h2>
                <p class="font-sans text-[15px] text-text-s mt-4 max-w-[600px] mx-auto">Situações de trabalhadores que passaram por problemas parecidos e buscaram orientação.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-[900px] mx-auto">
                <div class="bg-white p-8 rounded-xl shadow-sm border border-slate-100 relative">
                    <div class="text-brand-gold text-4xl font-serif absolute top-4 left-6 opacity-30">"</div>
                    <p class="font-sans text-[15px] text-text-p italic leading-relaxed relative z-10 pt-4">Trabalhava horas extras praticamente todos os dias e não recebia corretamente. Achava que não tinha como provar, mas com a orientação certa consegui buscar meus direitos.</p>
                    <p class="font-sans text-[13px] text-text-s mt-4 font-semibold">— Cliente, São Paulo/SP</p>
                </div>
                
                <div class="bg-white p-8 rounded-xl shadow-sm border border-slate-100 relative">
                    <div class="text-brand-gold text-4xl font-serif absolute top-4 left-6 opacity-30">"</div>
                    <p class="font-sans text-[15px] text-text-p italic leading-relaxed relative z-10 pt-4">Fui dispensada grávida e não sabia quais eram meus direitos. A empresa dizia que estava tudo certo. A análise do caso foi fundamental para eu entender a situação.</p>
                    <p class="font-sans text-[13px] text-text-s mt-4 font-semibold">— Cliente, Campinas/SP</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ══ BLOCO AUTORIDADE ═══════════════════════════════ -->
    <section id="sobre" class="bg-brand-dark border-t border-white/10 text-white">
        <div class="flex flex-col lg:flex-row min-h-[600px]">
            <!-- Photo -->
            <div class="w-full lg:w-[48%] h-[400px] lg:h-auto overflow-hidden fade-in relative">
                <img src="nova_foto_katarina.jpg" alt="Dra. Katarina Malinauskas" class="w-full h-full object-cover object-top scale-[1.02]">
                <div class="absolute inset-0 bg-gradient-to-r from-transparent via-transparent to-[#0B0F19]"></div>
            </div>

            <!-- Text -->
            <div class="w-full lg:w-[52%] flex items-center py-[64px] px-8 md:px-[64px] lg:px-[80px] fade-up">
                <div class="w-full">
                    <div class="g-line mb-6"></div>
                    <h2 class="font-serif text-[32px] md:text-[40px] leading-[1.1] mb-6">Por que trabalhadores procuram a Dra. Katarina?</h2>
                    
                    <ul class="space-y-4 mb-8 font-sans text-[15px] text-white/80">
                        <li class="flex items-start gap-3"><span class="text-brand-gold font-bold">✓</span> Atuação direcionada exclusivamente ao Direito do Trabalho</li>
                        <li class="flex items-start gap-3"><span class="text-brand-gold font-bold">✓</span> Atendimento focado 100% em trabalhadores</li>
                        <li class="flex items-start gap-3"><span class="text-brand-gold font-bold">✓</span> Experiência com situações como horas extras, rescisões e acidentes</li>
                        <li class="flex items-start gap-3"><span class="text-brand-gold font-bold">✓</span> Análise criteriosa de documentação e provas</li>
                    </ul>
                    
                    <div class="bg-white/5 border border-white/10 rounded-lg p-5 inline-block">
                        <p class="font-sans font-bold text-[18px] text-brand-gold leading-none mb-1">OAB/SP nº 338.901</p>
                        <p class="font-sans text-[12px] text-white/60 uppercase tracking-widest">Inscrição Regular</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══ BLOCO FAQ (QUALIFICAÇÃO) ═══════════════════════ -->
    <section id="faq" class="py-[88px] bg-white">
        <div class="max-w-[1100px] mx-auto px-6">
            <div class="flex flex-col lg:flex-row gap-14 lg:gap-20">
                <div class="w-full lg:w-[36%] fade-up">
                    <div class="g-line mb-6"></div>
                    <span class="sec-label block mb-4">Dúvidas Frequentes</span>
                    <h2 class="font-serif text-[34px] md:text-[38px] text-text-p leading-[1.15] mb-5 max-w-[300px]">Perguntas Frequentes</h2>
                    <p class="font-sans text-[14px] text-text-s leading-relaxed mb-8">Informações para te ajudar a entender se faz sentido enviar seu caso para análise.</p>
                </div>

                <div class="w-full lg:w-[64%] fade-up divide-y divide-slate-100 border-t border-slate-100">
                    <div class="faq-item cursor-pointer py-5" onclick="toggleFaq(this)">
                        <div class="flex justify-between items-start gap-6">
                            <h4 class="font-sans font-semibold text-[15px] text-text-p leading-[1.5]">Preciso já ter todos os documentos?</h4>
                            <span class="faq-icon text-brand-gold text-2xl flex-shrink-0 mt-0.5">+</span>
                        </div>
                        <div class="faq-body">
                            <p class="font-sans text-[14px] text-text-s leading-[1.8] pt-4">Não necessariamente. Você pode começar relatando o que aconteceu. Caso existam documentos, mensagens, registros de ponto, holerites ou outros materiais, eles podem ajudar na análise.</p>
                        </div>
                    </div>

                    <div class="faq-item cursor-pointer py-5" onclick="toggleFaq(this)">
                        <div class="flex justify-between items-start gap-6">
                            <h4 class="font-sans font-semibold text-[15px] text-text-p leading-[1.5]">Fui demitido. Ainda posso procurar orientação?</h4>
                            <span class="faq-icon text-brand-gold text-2xl flex-shrink-0 mt-0.5">+</span>
                        </div>
                        <div class="faq-body">
                            <p class="font-sans text-[14px] text-text-s leading-[1.8] pt-4">Depende da situação e das circunstâncias do desligamento. Informe quando ocorreu e como foi feita a rescisão para que o caso possa ser avaliado. Existe um prazo de até 2 anos após a demissão para agir.</p>
                        </div>
                    </div>

                    <div class="faq-item cursor-pointer py-5" onclick="toggleFaq(this)">
                        <div class="flex justify-between items-start gap-6">
                            <h4 class="font-sans font-semibold text-[15px] text-text-p leading-[1.5]">Trabalhei sem carteira assinada. Posso procurar ajuda?</h4>
                            <span class="faq-icon text-brand-gold text-2xl flex-shrink-0 mt-0.5">+</span>
                        </div>
                        <div class="faq-body">
                            <p class="font-sans text-[14px] text-text-s leading-[1.8] pt-4">Se você trabalhava como empregado sem registro, essa informação é relevante. O caso precisa ser analisado de acordo com as circunstâncias concretas da relação de trabalho.</p>
                        </div>
                    </div>

                    <div class="faq-item cursor-pointer py-5" onclick="toggleFaq(this)">
                        <div class="flex justify-between items-start gap-6">
                            <h4 class="font-sans font-semibold text-[15px] text-text-p leading-[1.5]">Eu só quero saber se tenho direito a alguma coisa. Posso entrar em contato?</h4>
                            <span class="faq-icon text-brand-gold text-2xl flex-shrink-0 mt-0.5">+</span>
                        </div>
                        <div class="faq-body">
                            <p class="font-sans text-[14px] text-text-s leading-[1.8] pt-4">Sim, mas quanto mais informações você fornecer sobre o que aconteceu, mais útil será a análise inicial. Análises genéricas sem um caso concreto são menos eficientes.</p>
                        </div>
                    </div>

                    <div class="faq-item cursor-pointer py-5" onclick="toggleFaq(this)">
                        <div class="flex justify-between items-start gap-6">
                            <h4 class="font-sans font-semibold text-[15px] text-text-p leading-[1.5]">A empresa ainda não me demitiu. Posso procurar orientação?</h4>
                            <span class="faq-icon text-brand-gold text-2xl flex-shrink-0 mt-0.5">+</span>
                        </div>
                        <div class="faq-body">
                            <p class="font-sans text-[14px] text-text-s leading-[1.8] pt-4">Sim. Algumas situações, como rescisão indireta (quando a empresa não cumpre com suas obrigações graves), precisam ser avaliadas enquanto a relação de trabalho ainda está acontecendo.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══ ANTI-LEAD LIXO CTA ════════════════════════════ -->
    <section class="py-[88px] bg-brand-alt border-t border-white/5">
        <div class="max-w-[700px] mx-auto px-6 text-center fade-up">
            <div class="g-line mx-auto mb-8"></div>
            <h2 class="font-serif text-[32px] md:text-[40px] text-white leading-tight mb-6">Este atendimento é para casos trabalhistas concretos.</h2>
            <p class="font-sans text-[15px] text-white/70 mb-5 max-w-[550px] mx-auto leading-relaxed">
                Se você está apenas procurando uma informação genérica sobre Direito do Trabalho ou quer saber “quanto ganharia” sem apresentar os fatos do seu caso, este atendimento provavelmente não é o mais adequado.
            </p>
            <p class="font-sans text-[16px] text-brand-gold font-semibold mb-10 max-w-[550px] mx-auto">
                Se existe uma situação específica acontecendo ou que aconteceu com você, conte os detalhes e envie seu caso para análise.
            </p>
            
            <a id="final-cta"
               href="#" onclick="openLeadModal('Final CTA - Quero enviar meu caso'); return false;"
               class="btn-wa px-12 py-5 text-[15px] uppercase tracking-wide mx-auto">
                QUERO ENVIAR MEU CASO
            </a>
        </div>
    </section>
    """

    modal_and_scripts = """
    <!-- ══ Lead Modal — Trabalhador (Mini Diagnóstico) ═════ -->
    <div id="leadModal" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/85 backdrop-blur-sm opacity-0 pointer-events-none transition-all duration-300 overflow-y-auto py-10">
        <div class="modal-card bg-[#0E172E] border border-white/10 p-8 rounded-xl max-w-[500px] w-full relative scale-95 transition-transform duration-300 mx-5 shadow-2xl my-auto">
            <button onclick="closeLeadModal()" class="absolute top-4 right-4 text-white/40 hover:text-white transition-colors text-2xl leading-none" aria-label="Fechar">&times;</button>
            
            <div class="g-line mb-4"></div>
            <h3 class="font-serif text-[24px] text-white leading-tight mb-2">Avaliação de Caso</h3>
            <p class="font-sans text-[13px] text-white/60 mb-6">Responda rapidamente para que possamos entender sua situação antes do atendimento no WhatsApp.</p>
            
            <form id="popup-form" class="space-y-6">
                <input type="hidden" name="pagina" value="trabalhador.html">
                <input type="hidden" name="tipo" value="trabalhador">
                <input type="hidden" name="botao" id="popup-botao" value="">
                
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
                
                <div class="border-t border-white/10 pt-5">
                    <div class="flex gap-4">
                        <div class="flex-1">
                            <label class="block text-[10px] uppercase tracking-[2px] text-brand-gold mb-1.5 font-semibold">Seu Nome</label>
                            <input type="text" name="nome" required class="w-full bg-black/20 border border-white/10 rounded px-3 py-2.5 text-white focus:outline-none focus:border-brand-gold transition-colors font-sans text-[14px]" placeholder="Nome completo">
                        </div>
                        <div class="flex-1">
                            <label class="block text-[10px] uppercase tracking-[2px] text-brand-gold mb-1.5 font-semibold">WhatsApp</label>
                            <input type="tel" name="whatsapp" required class="w-full bg-black/20 border border-white/10 rounded px-3 py-2.5 text-white focus:outline-none focus:border-brand-gold transition-colors font-sans text-[14px]" placeholder="(00) 00000-0000">
                        </div>
                    </div>
                </div>
                
                <div class="pt-2">
                    <button type="submit" id="popup-btn" class="w-full btn-wa py-4 text-[14px] font-bold rounded-lg shadow-[0_0_20px_rgba(37,211,102,0.2)] hover:shadow-[0_0_30px_rgba(37,211,102,0.4)] transition-all">
                        AVALIAR MEU CASO NO WHATSAPP
                    </button>
                    <p class="text-center font-sans text-[11px] text-white/30 mt-3">Suas informações são tratadas com sigilo absoluto.</p>
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
            modal.classList.remove('opacity-0', 'pointer-events-none');
            card.classList.remove('scale-95');
            card.classList.add('scale-100');
        }

        function closeLeadModal() {
            const modal = document.getElementById('leadModal');
            const card  = modal.querySelector('.modal-card');
            modal.classList.add('opacity-0', 'pointer-events-none');
            card.classList.remove('scale-100');
            card.classList.add('scale-95');
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
                nav.classList.toggle('shadow-lg', window.scrollY > 40);
                const finalCta = document.getElementById('final-cta');
                if (finalCta) {
                    const rect = finalCta.getBoundingClientRect();
                    stickyCta.style.transform = (rect.top < window.innerHeight) ? 'translateY(100%)' : 'translateY(0)';
                }
            }, { passive: true });

            // Progress bar
            const bar = document.getElementById('pbar');
            window.addEventListener('scroll', () => {
                bar.style.width = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100) + '%';
            }, { passive: true });

            // Close modal clicking outside
            document.getElementById('leadModal').addEventListener('click', function(e) {
                if (e.target === this) closeLeadModal();
            });

            // Form submit
            document.getElementById('popup-form')?.addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn  = document.getElementById('popup-btn');
                const form = e.target;

                btn.disabled = true;
                btn.innerHTML = 'Enviando...';
                btn.style.opacity = '0.7';
                
                // Formata os dados preenchidos no form para uma mensagem de WhatsApp
                const nome = form.nome.value;
                const situacao = form.situacao.value;
                const quando = form.quando.value;
                const aindaTrabalha = form.ainda_trabalha.value;
                const provas = form.tem_provas.value;
                
                const textoWa = `Olá, meu nome é ${nome}. Gostaria de uma avaliação do meu caso.\\n\\nSituação: ${situacao}\\nQuando: ${quando}\\nAinda na empresa: ${aindaTrabalha}\\nPossui provas: ${provas}`;
                const WA_LINK = 'https://wa.me/5511933502503?text=' + encodeURIComponent(textoWa);

                const data = {
                    nome:       nome,
                    whatsapp:   form.whatsapp.value,
                    info_extra: `Situação: ${situacao} | Quando: ${quando} | Ainda Trabalha: ${aindaTrabalha} | Provas: ${provas}`,
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
                btn.disabled = false;
                btn.innerHTML = 'AVALIAR MEU CASO NO WHATSAPP';
                btn.style.opacity = '1';
            });
        });
    </script>
</body>
</html>
    """

    full_trabalhador = head + nav + new_body + footer + modal_and_scripts
    with open('trabalhador.html', 'w', encoding='utf-8') as f:
        f.write(full_trabalhador)

    # Agora criar horas-extras.html mudando a COPY específica.
    # Vou usar o trabalhador gerado e substituir o Hero, dores e form values.
    
    # Substituir Hero
    he_body = new_body.replace(
        "Seu empregador deixou de pagar seus direitos trabalhistas?",
        "Você trabalhava além do horário e essas horas não eram pagas?"
    ).replace(
        """Se você trabalha ou trabalhou com carteira assinada e passou por problemas como <strong class="text-white">horas extras não pagas, acidente de trabalho, doença profissional, falta de registro, justa causa, rescisão indireta ou problemas relacionados à gestação</strong>, seu caso pode precisar de uma análise jurídica.""",
        """Se você fazia horas extras com frequência e elas não apareciam corretamente no seu pagamento, assinava folha de ponto e voltava a trabalhar, ou levava trabalho para casa sem receber por isso, seu caso pode precisar de uma análise jurídica específica."""
    )
    
    # Modificar Identificação
    he_body = he_body.replace(
        "Qual dessas situações aconteceu com você?",
        "Identifique como as suas horas extras foram violadas:"
    )
    
    # Refazendo os cards
    pain_cards_regex = r'<div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-12">.*?</div>\s*<!-- Consequência / Urgência -->'
    he_pain_cards = """<div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-12">
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Bater o ponto e voltar a trabalhar?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">A empresa pedia para você registrar a saída, mas você continuava trabalhando por horas sem que isso fosse contabilizado.</p>
                    </div>
                </div>
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Trabalhar aos finais de semana e feriados sem adicional?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Você abria mão dos seus dias de descanso e não recebia os adicionais legais (100% ou folga compensatória).</p>
                    </div>
                </div>
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Não ter intervalo de almoço completo?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Tinha que engolir a comida e voltar ao trabalho antes de completar a 1 hora mínima de descanso obrigatório.</p>
                    </div>
                </div>
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[16px] text-white mb-2">Banco de horas que nunca era pago ou folgado?</h4>
                        <p class="font-sans text-[14px] text-white/70 leading-relaxed">Acumulava milhares de horas, mas não conseguia tirar folga nem recebia o valor em dinheiro no final.</p>
                    </div>
                </div>
            </div>
            <!-- Consequência / Urgência -->"""
    
    he_body = re.sub(pain_cards_regex, he_pain_cards, he_body, flags=re.DOTALL)
    
    he_modal = modal_and_scripts.replace(
        '<input type="hidden" name="pagina" value="trabalhador.html">',
        '<input type="hidden" name="pagina" value="horas-extras.html">'
    )
    
    # O form_situacao para HE
    he_modal = re.sub(
        r'<!-- Pergunta 1 -->.*?<!-- Pergunta 2 -->',
        """<!-- Pergunta 1 -->
                <div>
                    <label class="block text-[13px] text-white mb-3 font-semibold">Como as suas horas extras eram tratadas?</label>
                    <div class="space-y-2 font-sans text-[13px] text-white/80">
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Não eram pagas nem iam para banco de horas" required class="accent-brand-gold"> Não eram pagas nem iam para banco de horas</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Batia o ponto e voltava a trabalhar" class="accent-brand-gold"> Batia o ponto e voltava a trabalhar</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Intervalo de almoço reduzido" class="accent-brand-gold"> Intervalo de almoço reduzido</label>
                        <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="situacao" value="Trabalho externo/home office sem controle" class="accent-brand-gold"> Trabalho sem externo/home office sem controle</label>
                    </div>
                </div>
                <!-- Pergunta 2 -->""",
        he_modal, flags=re.DOTALL
    )

    full_he = head + nav + he_body + footer + he_modal
    
    # Atualizar title meta tag na página HE
    full_he = re.sub(r'<title>.*?</title>', '<title>Katarina Malinauskas | Horas Extras Não Pagas</title>', full_he)
    full_he = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Trabalhava além do horário e não recebia corretamente? Você pode ter valores atrasados de horas extras a receber.">', full_he)

    with open('horas-extras.html', 'w', encoding='utf-8') as f:
        f.write(full_he)
        
    print("Sucesso")

if __name__ == '__main__':
    update_trabalhador()
