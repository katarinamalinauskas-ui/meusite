import re

with open('trabalhador.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS for pain-card and remove pain-icon
css_old = """        /* Pain cards */
        .pain-card {
            background: #fff;
            border: 1px solid #F1F5F9;
            border-radius: 8px;
            padding: 20px 22px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,.04);
            transition: box-shadow .3s ease, border-color .3s ease;
        }
        .pain-card:hover {
            box-shadow: 0 8px 28px rgba(0,0,0,.08);
            border-color: rgba(197,160,89,.3);
        }
        .pain-icon {
            width: 38px; height: 38px;
            border-radius: 8px;
            background: linear-gradient(135deg, rgba(197,160,89,.12), rgba(197,160,89,.06));
            display: flex; align-items: center; justify-content: center;
            flex-shrink: 0;
            font-size: 18px;
        }"""

css_new = """        /* Pain cards */
        .pain-card {
            background: #fff;
            border: 1px solid #F1F5F9;
            border-left: 3px solid #C5A059;
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 4px 12px rgba(0,0,0,.03);
            transition: box-shadow .3s ease, border-left-color .3s ease;
        }
        .pain-card:hover {
            box-shadow: 0 12px 32px rgba(0,0,0,.08);
            border-left-color: #B38B44;
        }"""

content = content.replace(css_old, css_new)

# 2. Update HTML to remove emojis from pain cards
html_old = """            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-12">
                <div class="pain-card">
                    <div class="pain-icon">⏰</div>
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Fazia horas extras e não recebia corretamente?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Entradas antecipadas, saídas tardias, fins de semana ou intervalos reduzidos sem o devido pagamento.</p>
                    </div>
                </div>
                
                <div class="pain-card">
                    <div class="pain-icon">🧠</div>
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Trabalhou doente, sob pressão ou desenvolveu burnout?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Cobranças excessivas, metas impossíveis e sobrecarga que levaram a crises de ansiedade ou esgotamento.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div class="pain-icon">🚑</div>
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Sofreu acidente de trabalho e ficou sem suporte?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Lesões no local de trabalho ou no trajeto, sem emissão de CAT ou acompanhamento de estabilidade legal.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div class="pain-icon">😤</div>
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Era humilhado ou pressionado no ambiente de trabalho?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Tratamento rude por chefias, perseguições veladas ou constrangimentos constantes que caracterizam assédio.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div class="pain-icon">⚠️</div>
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Recebia funções além da sua contratação sem aumento?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Acúmulo de responsabilidades ou mudança para cargo superior sem anotação e reajuste salarial.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div class="pain-icon">☢️</div>
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Trabalhou em ambiente perigoso ou insalubre sem adicional?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Exposição a ruído excessivo, calor, produtos nocivos ou risco de vida sem receber os adicionais previstos em lei.</p>
                    </div>
                </div>
            </div>"""

html_new = """            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-12">
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Fazia horas extras e não recebia corretamente?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Entradas antecipadas, saídas tardias, fins de semana ou intervalos reduzidos sem o devido pagamento.</p>
                    </div>
                </div>
                
                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Trabalhou doente, sob pressão ou desenvolveu burnout?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Cobranças excessivas, metas impossíveis e sobrecarga que levaram a crises de ansiedade ou esgotamento.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Sofreu acidente de trabalho e ficou sem suporte?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Lesões no local de trabalho ou no trajeto, sem emissão de CAT ou acompanhamento de estabilidade legal.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Era humilhado ou pressionado no ambiente de trabalho?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Tratamento rude por chefias, perseguições veladas ou constrangimentos constantes que caracterizam assédio.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Recebia funções além da sua contratação sem aumento?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Acúmulo de responsabilidades ou mudança para cargo superior sem anotação e reajuste salarial.</p>
                    </div>
                </div>

                <div class="pain-card">
                    <div>
                        <h4 class="font-sans font-semibold text-[15px] text-text-p mb-1.5">Trabalhou em ambiente perigoso ou insalubre sem adicional?</h4>
                        <p class="font-sans text-[13px] text-text-s leading-relaxed">Exposição a ruído excessivo, calor, produtos nocivos ou risco de vida sem receber os adicionais previstos em lei.</p>
                    </div>
                </div>
            </div>"""

content = content.replace(html_old, html_new)

# 3. Replace all WhatsApp href links with openLeadModal
pattern = r'href="https://wa\.me/5511933502503\?text=Ol%C3%A1%2C%20meu%20direitos%20foram%20violados%2C%20gostaria%20de%20falar%20com%20uma%20advogada%20especialista!"\s*target="_blank"\s*rel="noopener"'
new_href = 'href="#" onclick="openLeadModal(); return false;"'

content = re.sub(pattern, new_href, content)

with open('trabalhador.html', 'w', encoding='utf-8') as f:
    f.write(content)
