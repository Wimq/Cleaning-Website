import os
import re

# Read base header/footer
with open('pages/find-courses.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = "".join(lines[:198])
footer = "".join(lines[271:])

# Clearing Support Header
header_clearing = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Clearing Support | Kensington Ivy</title>')
header_clearing = re.sub(r'<style>.*?</style>', '', header_clearing, flags=re.DOTALL)
header_clearing = header_clearing.replace('</head>', '<style>\nbody { background-color: var(--off, #faf9f6); padding-top: 100px; }\n.clearing-section { padding: 6rem 0; }\n.clearing-section:nth-child(even) { background: #fff; }\n.step-card { padding: 2rem; border-left: 3px solid var(--gold); background: #fdfbf7; margin-bottom: 1.5rem; }\n</style>\n</head>')

clearing_content = """
<!-- HERO -->
<section class="clearing-section" style="padding-top: 8rem; padding-bottom: 4rem; text-align: center;">
    <div class="container">
        <span style="color: var(--gold); font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; display: block;">Urgent Admissions Placement</span>
        <h1 style="font-family: var(--ff-head); font-size: 4rem; color: var(--navy); margin-bottom: 1.5rem; line-height: 1.1;">Elite UCAS Clearing<br>Representation</h1>
        <p style="font-size: 1.25rem; color: #555; max-width: 700px; margin: 0 auto 3rem auto; line-height: 1.6;">
            Missed your expected grades? The Clearing window is highly competitive and time-sensitive. We act as your private admissions advocates to bypass standard queues and secure premium placements in hours, not weeks.
        </p>
        <a href="register.html" class="btn btn-gold" style="font-size: 1.1rem; padding: 1rem 2.5rem;">Begin Urgent Profile Review <i data-lucide="arrow-right"></i></a>
    </div>
</section>

<!-- THE REALITY OF CLEARING -->
<section class="clearing-section" style="background: var(--navy); color: #fff;">
    <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
        <div>
            <h2 style="font-family: var(--ff-head); font-size: 2.5rem; margin-bottom: 1.5rem; color: var(--gold);">The Reality of Clearing</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: rgba(255,255,255,0.8); margin-bottom: 1.5rem;">
                When A-Level and BTEC results are released, tens of thousands of students immediately flood university hotlines. Standard applicants spend hours on hold, often settling for courses that don't match their true ambitions.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: rgba(255,255,255,0.8);">
                Kensington Ivy operates differently. Our senior consultants hold direct, back-channel relationships with admissions boards at Top 30 UK institutions, allowing us to negotiate offers directly on your behalf while others wait in the queue.
            </p>
        </div>
        <div style="background: rgba(255,255,255,0.05); padding: 3rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 1.5rem; display: flex; gap: 1rem; align-items: flex-start;">
                    <i data-lucide="check-circle-2" style="color: var(--gold); flex-shrink: 0; margin-top: 3px;"></i>
                    <div>
                        <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.3rem;">Bypass the Hotlines</strong>
                        <span style="color: rgba(255,255,255,0.6); font-size: 0.95rem;">Direct communication with faculty decision-makers.</span>
                    </div>
                </li>
                <li style="margin-bottom: 1.5rem; display: flex; gap: 1rem; align-items: flex-start;">
                    <i data-lucide="check-circle-2" style="color: var(--gold); flex-shrink: 0; margin-top: 3px;"></i>
                    <div>
                        <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.3rem;">Grade Negotiation</strong>
                        <span style="color: rgba(255,255,255,0.6); font-size: 0.95rem;">Expert advocacy for students who missed their offer by a single grade.</span>
                    </div>
                </li>
                <li style="display: flex; gap: 1rem; align-items: flex-start;">
                    <i data-lucide="check-circle-2" style="color: var(--gold); flex-shrink: 0; margin-top: 3px;"></i>
                    <div>
                        <strong style="display: block; font-size: 1.1rem; margin-bottom: 0.3rem;">Alternative Pathways</strong>
                        <span style="color: rgba(255,255,255,0.6); font-size: 0.95rem;">Immediate access to premium Foundation or International Year One options.</span>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</section>

<!-- OUR PROCESS -->
<section class="clearing-section">
    <div class="container">
        <div style="text-align: center; margin-bottom: 4rem;">
            <h2 style="font-family: var(--ff-head); font-size: 2.5rem; color: var(--navy);">Our 24-Hour Clearing Protocol</h2>
            <p style="font-size: 1.1rem; color: #666; max-width: 600px; margin: 1rem auto 0 auto;">How we secure your placement swiftly and discreetly.</p>
        </div>
        
        <div style="max-width: 800px; margin: 0 auto;">
            <div class="step-card">
                <span style="color: var(--gold); font-weight: bold; font-size: 0.9rem;">PHASE 01</span>
                <h3 style="font-family: var(--ff-head); font-size: 1.5rem; color: var(--navy); margin: 0.5rem 0;">Rapid Profile Assessment</h3>
                <p style="color: #555; margin: 0; line-height: 1.6;">Within hours of receiving your results, our consultants analyze your exact academic profile, identifying strengths that can be leveraged during faculty negotiations.</p>
            </div>
            
            <div class="step-card">
                <span style="color: var(--gold); font-weight: bold; font-size: 0.9rem;">PHASE 02</span>
                <h3 style="font-family: var(--ff-head); font-size: 1.5rem; color: var(--navy); margin: 0.5rem 0;">Strategic Matching & Shortlisting</h3>
                <p style="color: #555; margin: 0; line-height: 1.6;">We cross-reference your results with our internal database of available Clearing vacancies across elite institutions, presenting you with 3 to 5 realistic, premium options.</p>
            </div>
            
            <div class="step-card">
                <span style="color: var(--gold); font-weight: bold; font-size: 0.9rem;">PHASE 03</span>
                <h3 style="font-family: var(--ff-head); font-size: 1.5rem; color: var(--navy); margin: 0.5rem 0;">Direct Admissions Negotiation</h3>
                <p style="color: #555; margin: 0; line-height: 1.6;">We advocate on your behalf directly to our university contacts. We present your case, negotiate contextual factors, and bypass the standard UCAS queue.</p>
            </div>
            
            <div class="step-card">
                <span style="color: var(--gold); font-weight: bold; font-size: 0.9rem;">PHASE 04</span>
                <h3 style="font-family: var(--ff-head); font-size: 1.5rem; color: var(--navy); margin: 0.5rem 0;">Offer Confirmation</h3>
                <p style="color: #555; margin: 0; line-height: 1.6;">Once a verbal offer is secured, we guide you through the formal UCAS Hub process to lock in your placement instantly.</p>
            </div>
        </div>
    </div>
</section>

<!-- FINAL CTA -->
<section class="clearing-section" style="background: #fdfbf7; text-align: center; border-top: 1px solid rgba(0,0,0,0.05);">
    <div class="container">
        <h2 style="font-family: var(--ff-head); font-size: 2.2rem; color: var(--navy); margin-bottom: 1rem;">Don't leave your future to chance.</h2>
        <p style="font-size: 1.1rem; color: #555; max-width: 600px; margin: 0 auto 2rem auto;">Spaces at top-tier universities disappear within hours on results day. Register your interest early to ensure we can represent you the moment lines open.</p>
        <a href="register.html" class="btn btn-gold">Contact Admissions Team</a>
    </div>
</section>
"""


# Registries Header
header_registries = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Educational Awarding Bodies | Kensington Ivy</title>')
header_registries = re.sub(r'<style>.*?</style>', '', header_registries, flags=re.DOTALL)
header_registries = header_registries.replace('</head>', '<style>\nbody { background-color: var(--off, #faf9f6); padding-top: 100px; }\n.registry-row { display: flex; align-items: center; padding: 2rem; background: #fff; border-bottom: 1px solid rgba(0,0,0,0.05); transition: background 0.3s ease; }\n.registry-row:hover { background: #fdfbf7; }\n.reg-abbr { width: 80px; height: 80px; background: var(--navy); color: var(--gold); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: var(--ff-head); font-size: 1.5rem; flex-shrink: 0; margin-right: 2rem; }\n.reg-content h3 { font-family: var(--ff-head); font-size: 1.5rem; color: var(--navy); margin-bottom: 0.25rem; }\n.reg-content p { color: #666; font-size: 0.95rem; margin: 0; line-height: 1.5; }\n.reg-tags { display: flex; gap: 0.5rem; margin-top: 1rem; }\n.reg-tag { font-size: 0.75rem; padding: 0.25rem 0.75rem; background: rgba(201,162,88,0.1); color: #a87822; border-radius: 50px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; }\n</style>\n</head>')

registries_content = """
<section class="container" style="padding: 6rem 0; min-height: 60vh;">
    <div style="text-align: center; margin-bottom: 5rem;">
        <h1 style="font-family: var(--ff-head); font-size: 3.5rem; color: var(--navy); margin-bottom: 1.5rem;">UK Educational & Awarding Bodies</h1>
        <p style="font-size: 1.2rem; color: #555; max-width: 800px; margin: 0 auto; line-height: 1.8;">
            Kensington Ivy meticulously evaluates qualifications from all major UK examination boards. Our deep understanding of these distinct grading frameworks ensures we can optimally position your academic profile when negotiating with university admissions teams.
        </p>
    </div>
    
    <div style="border-top: 1px solid rgba(0,0,0,0.05); max-width: 900px; margin: 0 auto;">
        
        <div class="registry-row">
            <div class="reg-abbr">P/E</div>
            <div class="reg-content">
                <h3>Pearson Edexcel</h3>
                <p>The UK's largest awarding organization, offering academic and vocational qualifications in schools, colleges, and workplaces in the UK and abroad.</p>
                <div class="reg-tags">
                    <span class="reg-tag">A-Levels</span><span class="reg-tag">GCSEs</span><span class="reg-tag">BTEC Nationals</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">AQA</div>
            <div class="reg-content">
                <h3>Assessment and Qualifications Alliance (AQA)</h3>
                <p>An independent education charity and the largest provider of academic qualifications taught in schools and colleges in England.</p>
                <div class="reg-tags">
                    <span class="reg-tag">A-Levels</span><span class="reg-tag">GCSEs</span><span class="reg-tag">EPQ</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">OCR</div>
            <div class="reg-content">
                <h3>Oxford, Cambridge and RSA Examinations</h3>
                <p>A leading UK awarding body, providing a wide range of qualifications to meet the needs of learners of all ages and abilities.</p>
                <div class="reg-tags">
                    <span class="reg-tag">A-Levels</span><span class="reg-tag">Cambridge Nationals</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">CAIE</div>
            <div class="reg-content">
                <h3>Cambridge Assessment International Education</h3>
                <p>The world's largest provider of international education programmes and qualifications for 5 to 19 year olds, widely recognized by top-tier universities.</p>
                <div class="reg-tags">
                    <span class="reg-tag">International A-Levels</span><span class="reg-tag">IGCSE</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">IB</div>
            <div class="reg-content">
                <h3>International Baccalaureate Organization</h3>
                <p>A highly prestigious global educational foundation offering a highly respected Diploma Programme, highly valued by elite UK institutions.</p>
                <div class="reg-tags">
                    <span class="reg-tag">IB Diploma</span><span class="reg-tag">IB Career-related</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">WJEC</div>
            <div class="reg-content">
                <h3>Welsh Joint Education Committee (Eduqas)</h3>
                <p>Providing examinations, professional development and educational resources to schools and colleges in Wales, England and Northern Ireland.</p>
                <div class="reg-tags">
                    <span class="reg-tag">A-Levels</span><span class="reg-tag">Vocational</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">C&G</div>
            <div class="reg-content">
                <h3>City & Guilds</h3>
                <p>A global leader in skills development, providing services to training providers, employers, and trainees across a variety of sectors.</p>
                <div class="reg-tags">
                    <span class="reg-tag">T-Levels</span><span class="reg-tag">Vocational Tech</span>
                </div>
            </div>
        </div>
        
        <div class="registry-row">
            <div class="reg-abbr">NCFE</div>
            <div class="reg-content">
                <h3>Northern Council for Further Education</h3>
                <p>An educational charity and national awarding organization, advancing learning and designing core technical qualifications including T-Levels.</p>
                <div class="reg-tags">
                    <span class="reg-tag">T-Levels</span><span class="reg-tag">V-Certs</span>
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
