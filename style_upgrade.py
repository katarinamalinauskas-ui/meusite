import re

with open('trabalhador.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update colors in tailwind config for a richer look
old_config = """                    colors: {
                        'brand-dark': '#070D1E',
                        'brand-navy': '#0E172E',
                        'brand-alt': '#F8FAFC',
                        'brand-gold': '#C5A059',
                        'brand-gold-hover': '#B38B44',
                        'brand-gold-light': '#F8F4E6',
                        'brand-green': '#25D366',
                        'brand-green-hover': '#1EBE57',
                        'text-p': '#1E293B',
                        'text-s': '#64748B',
                        'text-m': '#94A3B8',
                    },"""

new_config = """                    colors: {
                        'brand-dark': '#0B0F19',
                        'brand-navy': '#111827',
                        'brand-alt': '#0B0F19', // Dark mode for alt section
                        'brand-gold': '#D4AF37',
                        'brand-gold-hover': '#F3E5AB',
                        'brand-gold-light': '#1F1A0F',
                        'brand-green': '#25D366',
                        'brand-green-hover': '#1EBE57',
                        'text-p': '#F3F4F6',
                        'text-s': '#9CA3AF',
                        'text-m': '#6B7280',
                        'glass': 'rgba(255, 255, 255, 0.03)',
                        'glass-border': 'rgba(255, 255, 255, 0.08)',
                    },"""

content = content.replace(old_config, new_config)

# 2. Add glassmorphism CSS
css_add = """
        /* Premium Glass Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            transition: all 0.4s ease;
        }
        .glass-card:hover {
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(212, 175, 55, 0.4);
            transform: translateY(-5px);
            box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
        }
"""
content = content.replace("/* ── Reset & Base ── */", "/* ── Reset & Base ── */" + css_add)

# 3. Update Headline
old_headline = """<h1 class="font-serif text-[40px] md:text-[52px] lg:text-[58px] text-white leading-[1.08] mb-6" style="max-width:640px;">
                        Trabalhador, seus direitos foram violados?
                        <em class="grad-text not-italic block mt-1">Fale com uma advogada especialista em Direito do Trabalho!</em>
                    </h1>"""

new_headline = """<h1 class="font-serif text-[42px] md:text-[56px] lg:text-[64px] text-white leading-[1.05] mb-6 font-semibold" style="max-width:700px; text-shadow: 0 4px 20px rgba(0,0,0,0.5);">
                        Trabalhador, seus direitos foram violados?
                        <em class="not-italic block mt-2 text-transparent bg-clip-text bg-gradient-to-r from-brand-gold to-[#F3E5AB]">Fale com uma advogada especialista em Direito do Trabalho!</em>
                    </h1>"""

content = content.replace(old_headline, new_headline)

# 4. Make "Dores" section totally dark & premium
# old pain-card CSS
old_pain_card_css = """        /* Pain cards */
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
new_pain_card_css = """        /* Pain cards */
        .pain-card {
            background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.05);
            border-left: 3px solid rgba(212,175,55,0.5);
            border-radius: 12px;
            padding: 28px;
            box-shadow: 0 4px 24px rgba(0,0,0,.2);
            transition: all .4s cubic-bezier(.16,1,.3,1);
        }
        .pain-card:hover {
            box-shadow: 0 12px 40px rgba(0,0,0,.4);
            border-left: 3px solid #D4AF37;
            background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
            transform: translateY(-4px);
        }
        .pain-card h4 { color: #F3F4F6; }
        .pain-card p { color: #9CA3AF; }"""
content = content.replace(old_pain_card_css, new_pain_card_css)

# Update dores section title text colors
content = content.replace('text-text-p mt-4 leading-[1.2]', 'text-white mt-4 leading-[1.2]')
content = content.replace('text-text-s mt-4', 'text-white/70 mt-4')

# 5. Fix remaining "text-text-p" colors in white sections, wait, I changed text-p to white in tailwind!
# This means sections that WERE white background (like "Sobre" and "FAQ") are now white background with white text if I don't fix them.
# Let's revert the tailwind colors change for text-p, text-s, and just use custom classes for the dark sections!
# Actually, it's safer to keep tailwind colors as they were for the light sections, and explicitly use text-white in the dark sections.

content = content.replace("'text-p': '#F3F4F6',", "'text-p': '#1E293B',")
content = content.replace("'text-s': '#9CA3AF',", "'text-s': '#64748B',")
content = content.replace("'text-m': '#6B7280',", "'text-m': '#94A3B8',")

# Then explicitly color the dores section texts:
content = content.replace('<h2 class="font-serif text-[34px] md:text-[44px] text-text-p', '<h2 class="font-serif text-[34px] md:text-[44px] text-white')
content = content.replace('<p class="font-sans text-[15px] text-text-s', '<p class="font-sans text-[15px] text-white/70')
content = content.replace('<strong class="text-text-p">', '<strong class="text-brand-gold">')

# 6. Hero subtle animations and layout
content = content.replace('w-[700px] h-[700px]', 'w-[900px] h-[900px]')
content = content.replace('rgba(197,160,89,.06)', 'rgba(212,175,55,.15)')
content = content.replace('w-[400px] h-[400px]', 'w-[600px] h-[600px]')
content = content.replace('rgba(37,211,102,.04)', 'rgba(37,211,102,.1)')

# 7. Hero Photo premium styling
old_hero_photo = """                        <!-- Decorative border -->
                        <div class="absolute -top-5 -right-5 w-full h-full border border-brand-gold/20 rounded-sm z-0"></div>
                        <!-- Gold dot accent -->
                        <div class="absolute -bottom-3 -left-3 w-24 h-24 rounded-sm z-0" style="background:linear-gradient(135deg,rgba(197,160,89,.08),transparent);"></div>
                        
                        <div class="relative w-full h-full overflow-hidden rounded-sm z-10">
                            <div class="absolute inset-0 bg-gradient-to-t from-brand-dark via-brand-dark/20 to-transparent z-10"></div>
                            <div class="absolute inset-0 bg-brand-gold/4 mix-blend-overlay z-20"></div>
                            <img src="foto-katarina-sobre.jpg" alt="Dra. Katarina Malinauskas" class="w-full h-full object-cover object-top">
                        </div>"""

new_hero_photo = """                        <!-- Decorative blur -->
                        <div class="absolute -top-10 -right-10 w-[200px] h-[200px] bg-brand-gold/20 blur-[60px] rounded-full z-0 pointer-events-none"></div>
                        <!-- Gold outline -->
                        <div class="absolute top-4 -right-4 w-full h-full border-2 border-brand-gold/30 rounded-xl z-0"></div>
                        
                        <div class="relative w-full h-full overflow-hidden rounded-xl z-10 border border-white/10 shadow-2xl">
                            <div class="absolute inset-0 bg-gradient-to-t from-[#0B0F19] via-transparent to-transparent z-10"></div>
                            <div class="absolute inset-0 bg-brand-gold/10 mix-blend-overlay z-20"></div>
                            <img src="foto-katarina-sobre.jpg" alt="Dra. Katarina Malinauskas" class="w-full h-full object-cover object-top scale-105 hover:scale-100 transition-transform duration-1000">
                        </div>"""
content = content.replace(old_hero_photo, new_hero_photo)

# 8. Add shimmering effect to main CTAs
content = content.replace('class="btn-wa px-8 py-4', 'class="btn-wa px-10 py-4.5 shadow-[0_0_30px_rgba(37,211,102,0.3)] hover:shadow-[0_0_45px_rgba(37,211,102,0.5)]')
content = content.replace('class="btn-wa px-10 py-4 text-[14px]', 'class="btn-wa px-10 py-4.5 text-[14px] shadow-[0_0_30px_rgba(37,211,102,0.3)] hover:shadow-[0_0_45px_rgba(37,211,102,0.5)]')
content = content.replace('class="btn-wa px-9 py-4', 'class="btn-wa px-10 py-4.5 shadow-[0_0_30px_rgba(37,211,102,0.3)] hover:shadow-[0_0_45px_rgba(37,211,102,0.5)]')

with open('trabalhador.html', 'w', encoding='utf-8') as f:
    f.write(content)
