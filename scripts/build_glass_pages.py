import os
import re

with open('pages/find-courses.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = "".join(lines[:198])
footer = "".join(lines[271:])

# Clearing Support Header
header_clearing = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Clearing Support | Kensington Ivy</title>')
header_clearing = re.sub(r'<style>.*?</style>', '', header_clearing, flags=re.DOTALL)
header_clearing = header_clearing.replace('</head>', """<style>
body { background-color: var(--off, #faf9f6); padding-top: 80px; }
.glass-hero {
    position: relative;
    padding: 8rem 0;
    background: url('../assets/images/hero_illustration.png') center/cover fixed;
    color: #fff;
    overflow: hidden;
}
.glass-overlay {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(14,23,38,0.92) 0%, rgba(14,23,38,0.98) 100%);
    z-index: 1;
}
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 3rem;
    box-shadow: 0 30px 60px rgba(0,0,0,0.2);
    transition: transform 0.4s ease, border-color 0.4s ease;
}
.glass-card:hover {
    transform: translateY(-5px);
    border-color: rgba(201, 162, 88, 0.4);
}
.glass-icon-box {
    width: 60px; height: 60px;
    background: rgba(201, 162, 88, 0.15);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(201, 162, 88, 0.3);
}
.phase-tag {
    display: inline-block;
    padding: 0.4rem 1rem;
    background: linear-gradient(90deg, rgba(201,162,88,0.2), transparent);
    color: var(--gold);
    border-left: 2px solid var(--gold);
    font-weight: 700;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.glow-text {
    text-shadow: 0 0 30px rgba(255,255,255,0.2);
}
</style>
</head>""")

clearing_content = """
<!-- PREMIUM GLASS HERO -->
<section class="glass-hero">
    <div class="glass-overlay"></div>
    <div class="container" style="position: relative; z-index: 2; text-align: center;">
        <span style="color: var(--gold); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 1.5rem; display: block;">Urgent Admissions Placement</span>
        <h1 class="glow-text" style="font-family: var(--ff-head); font-size: 4.5rem; margin-bottom: 1.5rem; line-height: 1.1;">Elite UCAS Clearing<br><span style="font-style: italic; font-weight: 400; color: rgba(255,255,255,0.9);">Representation.</span></h1>
        <p style="font-size: 1.25rem; color: rgba(255,255,255,0.7); max-width: 700px; margin: 0 auto 3rem auto; line-height: 1.8;">
            Missed your expected grades? Don't settle. We act as your private admissions advocates to bypass standard queues and secure premium placements in hours.
        </p>
        <a href="register.html" class="btn btn-gold" style="font-size: 1.1rem; padding: 1.2rem 3rem; box-shadow: 0 10px 30px rgba(201,162,88,0.3);">Initiate Urgent Review <i data-lucide="arrow-right"></i></a>
    </div>
</section>

<!-- THE REALITY OF CLEARING -->
<section style="background: var(--navy); padding: 8rem 0; position: relative;">
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at top right, rgba(201,162,88,0.05), transparent 50%); pointer-events: none;"></div>
    
    <div class="container">
        <div style="text-align: center; margin-bottom: 5rem;">
            <h2 style="font-family: var(--ff-head); font-size: 3rem; color: #fff; margin-bottom: 1rem;">The Kensington Advantage</h2>
            <p style="color: rgba(255,255,255,0.6); font-size: 1.2rem; max-width: 600px; margin: 0 auto;">While standard applicants wait on hold, our consultants leverage direct back-channels to university decision-makers.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem;">
            <div class="glass-card">
                <div class="glass-icon-box"><i data-lucide="phone-call" style="color: var(--gold); width: 28px; height: 28px;"></i></div>
                <h3 style="font-family: var(--ff-head); font-size: 1.8rem; color: #fff; margin-bottom: 1rem;">Bypass the Hotlines</h3>
                <p style="color: rgba(255,255,255,0.6); line-height: 1.7;">Direct communication with faculty decision-makers, entirely avoiding the chaotic public clearing queues.</p>
            </div>
            <div class="glass-card">
                <div class="glass-icon-box"><i data-lucide="file-check" style="color: var(--gold); width: 28px; height: 28px;"></i></div>
                <h3 style="font-family: var(--ff-head); font-size: 1.8rem; color: #fff; margin-bottom: 1rem;">Grade Negotiation</h3>
                <p style="color: rgba(255,255,255,0.6); line-height: 1.7;">Expert advocacy for students who missed their offer by a single grade, leveraging portfolio strengths.</p>
            </div>
            <div class="glass-card">
                <div class="glass-icon-box"><i data-lucide="compass" style="color: var(--gold); width: 28px; height: 28px;"></i></div>
                <h3 style="font-family: var(--ff-head); font-size: 1.8rem; color: #fff; margin-bottom: 1rem;">Alternative Pathways</h3>
                <p style="color: rgba(255,255,255,0.6); line-height: 1.7;">Immediate access to premium Foundation or International Year One options at elite institutions.</p>
            </div>
        </div>
    </div>
</section>

<!-- OUR PROCESS -->
<section style="padding: 8rem 0; background: #fff; position: relative; overflow: hidden;">
    <div style="position: absolute; top: -20%; left: -10%; width: 50%; height: 50%; background: radial-gradient(circle, rgba(201,162,88,0.05) 0%, transparent 70%); border-radius: 50%; pointer-events: none;"></div>
    
    <div class="container">
        <div style="text-align: center; margin-bottom: 5rem;">
            <h2 style="font-family: var(--ff-head); font-size: 3rem; color: var(--navy);">Our 24-Hour Protocol</h2>
            <p style="font-size: 1.2rem; color: #666; max-width: 600px; margin: 1rem auto 0 auto;">Swift, discreet, and highly effective placement execution.</p>
        </div>
        
        <div style="max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 3rem;">
            
            <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; align-items: center; padding: 3rem; background: #fdfbf7; border-radius: 24px; border: 1px solid rgba(201,162,88,0.15);">
                <div>
                    <span class="phase-tag">Phase 01</span>
                    <h3 style="font-family: var(--ff-head); font-size: 2.2rem; color: var(--navy); margin: 0;">Rapid Profile<br>Assessment</h3>
                </div>
                <div>
                    <p style="color: #555; font-size: 1.1rem; line-height: 1.8; margin: 0;">Within hours of receiving your results, our consultants analyze your exact academic profile, identifying hidden strengths that can be aggressively leveraged during faculty negotiations.</p>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; align-items: center; padding: 3rem; background: #fdfbf7; border-radius: 24px; border: 1px solid rgba(201,162,88,0.15);">
                <div>
                    <span class="phase-tag">Phase 02</span>
                    <h3 style="font-family: var(--ff-head); font-size: 2.2rem; color: var(--navy); margin: 0;">Strategic<br>Matching</h3>
                </div>
                <div>
                    <p style="color: #555; font-size: 1.1rem; line-height: 1.8; margin: 0;">We cross-reference your results with our internal database of available Clearing vacancies across elite institutions, presenting you with 3 to 5 realistic, premium options instantly.</p>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; align-items: center; padding: 3rem; background: #fdfbf7; border-radius: 24px; border: 1px solid rgba(201,162,88,0.15);">
                <div>
                    <span class="phase-tag">Phase 03</span>
                    <h3 style="font-family: var(--ff-head); font-size: 2.2rem; color: var(--navy); margin: 0;">Direct<br>Negotiation</h3>
                </div>
                <div>
                    <p style="color: #555; font-size: 1.1rem; line-height: 1.8; margin: 0;">We advocate on your behalf directly to our university contacts. We present your case, negotiate contextual factors, and bypass the standard UCAS queue entirely.</p>
                </div>
            </div>
            
        </div>
    </div>
</section>
"""


# Registries Header
header_registries = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Awarding Bodies | Kensington Ivy</title>')
header_registries = re.sub(r'<style>.*?</style>', '', header_registries, flags=re.DOTALL)
header_registries = header_registries.replace('</head>', """<style>
body { background-color: var(--navy); padding-top: 80px; color: #fff; }
.header { background: rgba(255,255,255,0.95) !important; } /* Force header white to contrast */
.registry-glass-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
    gap: 2rem;
    margin-top: 4rem;
}
.registry-glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 24px;
    padding: 3rem;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
}
.registry-glass-card::before {
    content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at top right, rgba(201,162,88,0.1), transparent 70%);
    pointer-events: none; opacity: 0; transition: opacity 0.4s ease;
}
.registry-glass-card:hover {
    transform: translateY(-5px);
    border-color: rgba(201, 162, 88, 0.3);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
.registry-glass-card:hover::before { opacity: 1; }

.reg-abbr-glass {
    font-family: var(--ff-head);
    font-size: 3rem;
    background: linear-gradient(135deg, var(--gold) 0%, #dfc596 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    line-height: 1;
}
.reg-title {
    font-family: var(--ff-head);
    font-size: 1.5rem;
    color: #fff;
    margin-bottom: 1rem;
    font-weight: 400;
    letter-spacing: 0.02em;
}
.reg-desc {
    color: rgba(255,255,255,0.5);
    line-height: 1.7;
    margin-bottom: 2rem;
    font-size: 1rem;
}
.glass-tags {
    display: flex; gap: 0.5rem; flex-wrap: wrap;
}
.glass-tag {
    padding: 0.4rem 1rem;
    background: rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.8);
    border-radius: 50px;
    font-size: 0.8rem;
    letter-spacing: 0.05em;
}
</style>
</head>""")

registries_content = """
<section style="padding: 8rem 0; position: relative; min-height: 100vh;">
    <!-- Abstract blurred background elements -->
    <div style="position: absolute; top: 10%; left: 5%; width: 40vw; height: 40vw; background: rgba(201,162,88,0.05); filter: blur(100px); border-radius: 50%; pointer-events: none;"></div>
    <div style="position: absolute; bottom: 10%; right: 5%; width: 30vw; height: 30vw; background: rgba(59,82,132,0.2); filter: blur(100px); border-radius: 50%; pointer-events: none;"></div>
    
    <div class="container" style="position: relative; z-index: 2;">
        <div style="text-align: center; max-width: 800px; margin: 0 auto;">
            <span style="color: var(--gold); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 1.5rem; display: block;">Academic Evaluation</span>
            <h1 style="font-family: var(--ff-head); font-size: 4rem; color: #fff; margin-bottom: 1.5rem; line-height: 1.1; text-shadow: 0 0 40px rgba(255,255,255,0.1);">UK Awarding Bodies</h1>
            <p style="font-size: 1.25rem; color: rgba(255,255,255,0.6); line-height: 1.8;">
                We meticulously evaluate qualifications from all major examination boards. Our profound understanding of distinct grading frameworks ensures we optimally position your academic profile.
            </p>
        </div>
        
        <div class="registry-glass-grid">
            
            <div class="registry-glass-card">
                <div class="reg-abbr-glass">P/E</div>
                <h3 class="reg-title">Pearson Edexcel</h3>
                <p class="reg-desc">The UK's largest awarding organization, offering academic and vocational qualifications recognized globally by top-tier institutions.</p>
                <div class="glass-tags">
                    <span class="glass-tag">A-Levels</span><span class="glass-tag">GCSEs</span><span class="glass-tag">BTEC Nationals</span>
                </div>
            </div>
            
            <div class="registry-glass-card">
                <div class="reg-abbr-glass">AQA</div>
                <h3 class="reg-title">Assessment & Qualifications Alliance</h3>
                <p class="reg-desc">An independent education charity and the largest provider of academic qualifications taught in schools and colleges in England.</p>
                <div class="glass-tags">
                    <span class="glass-tag">A-Levels</span><span class="glass-tag">GCSEs</span><span class="glass-tag">EPQ</span>
                </div>
            </div>
            
            <div class="registry-glass-card">
                <div class="reg-abbr-glass">OCR</div>
                <h3 class="reg-title">Oxford, Cambridge and RSA</h3>
                <p class="reg-desc">A leading UK awarding body providing a wide range of academic and vocational qualifications to meet diverse learner needs.</p>
                <div class="glass-tags">
                    <span class="glass-tag">A-Levels</span><span class="glass-tag">Cambridge Nationals</span>
                </div>
            </div>
            
            <div class="registry-glass-card">
                <div class="reg-abbr-glass">CAIE</div>
                <h3 class="reg-title">Cambridge International</h3>
                <p class="reg-desc">The world's largest provider of international education programmes, highly valued by elite UK and global universities.</p>
                <div class="glass-tags">
                    <span class="glass-tag">Intl. A-Levels</span><span class="glass-tag">IGCSE</span>
                </div>
            </div>
            
            <div class="registry-glass-card">
                <div class="reg-abbr-glass">IB</div>
                <h3 class="reg-title">International Baccalaureate</h3>
                <p class="reg-desc">A highly prestigious global educational foundation offering a rigorous Diploma Programme celebrated by Ivy League and Russell Group universities.</p>
                <div class="glass-tags">
                    <span class="glass-tag">IB Diploma</span><span class="glass-tag">Career-related</span>
                </div>
            </div>
            
            <div class="registry-glass-card">
                <div class="reg-abbr-glass">WJEC</div>
                <h3 class="reg-title">Welsh Joint Education Committee</h3>
                <p class="reg-desc">Providing highly respected examinations and educational resources to schools across Wales, England, and Northern Ireland.</p>
                <div class="glass-tags">
                    <span class="glass-tag">A-Levels</span><span class="glass-tag">Vocational</span>
                </div>
            </div>

        </div>
    </div>
</section>
"""

with open('pages/clearing-support.html', 'w', encoding='utf-8') as f:
    f.write(header_clearing + clearing_content + footer)

with open('pages/registries.html', 'w', encoding='utf-8') as f:
    f.write(header_registries + registries_content + footer)
