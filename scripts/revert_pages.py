import os
import re

with open('pages/find-courses.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = "".join(lines[:198])
footer = "".join(lines[271:])

# Clearing Support
header_clearing = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Clearing Support | Kensington Ivy</title>')
header_clearing = re.sub(r'<style>.*?</style>', '', header_clearing, flags=re.DOTALL)
header_clearing = header_clearing.replace('</head>', """<style>
body { background-color: var(--off, #faf9f6); }
.hero-clean { background: var(--navy); padding: 8rem 0 6rem 0; color: #fff; text-align: center; }
.hero-clean h1 { font-family: var(--ff-head); font-size: 3.5rem; margin-bottom: 1.5rem; }
.hero-clean p { font-size: 1.2rem; color: rgba(255,255,255,0.7); max-width: 700px; margin: 0 auto; }

.timeline-container { padding: 6rem 0; background: #fff; }
.step-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem; }
.step-card { background: var(--off, #faf9f6); padding: 2.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05); }
.step-num { font-family: var(--ff-head); font-size: 2rem; color: var(--gold); margin-bottom: 1rem; font-weight: 700; }
.step-title { font-family: var(--ff-head); font-size: 1.5rem; color: var(--navy); margin-bottom: 1rem; font-weight: 600; }
.step-desc { color: #666; line-height: 1.6; }

.cta-clean { text-align: center; padding: 6rem 0; background: var(--off, #faf9f6); }
.cta-clean h2 { font-family: var(--ff-head); font-size: 2.5rem; color: var(--navy); margin-bottom: 1.5rem; }
</style>
</head>""")

clearing_content = """
<section class="hero-clean">
    <div class="container">
        <h1>Urgent Clearing Representation</h1>
        <p>Missed your expected grades? We act as your private admissions advocates to bypass standard queues and secure premium placements within hours.</p>
    </div>
</section>

<section class="timeline-container">
    <div class="container">
        <div style="text-align: center; margin-bottom: 3rem;">
            <h2 style="font-family: var(--ff-head); font-size: 2.5rem; color: var(--navy);">Our 3-Step Protocol</h2>
            <p style="color: #666; font-size: 1.1rem; max-width: 600px; margin: 1rem auto 0;">A streamlined, time-critical process executed from the moment results are released.</p>
        </div>
        
        <div class="step-grid">
            <div class="step-card">
                <div class="step-num">01</div>
                <h3 class="step-title">Rapid Assessment</h3>
                <p class="step-desc">The moment results go live, our team analyzes your exact academic profile, cross-referencing your actual grades against elite clearing vacancies.</p>
            </div>
            <div class="step-card">
                <div class="step-num">02</div>
                <h3 class="step-title">Direct Negotiation</h3>
                <p class="step-desc">We bypass public hotlines. Our senior consultants speak directly to faculty admissions leads to negotiate conditional or unconditional verbal offers.</p>
            </div>
            <div class="step-card">
                <div class="step-num">03</div>
                <h3 class="step-title">Offer Confirmation</h3>
                <p class="step-desc">Once a verbal offer is secured, we guide you step-by-step through the official UCAS Hub to formally lock in your placement instantly.</p>
            </div>
        </div>
    </div>
</section>

<section class="cta-clean">
    <div class="container">
        <h2>Don't leave your future to chance.</h2>
        <p style="color: #666; max-width: 600px; margin: 0 auto 2rem; font-size: 1.1rem;">Spaces at top-tier universities disappear within hours. Register your interest early.</p>
        <a href="register.html" class="btn btn-gold" style="font-size: 1.1rem; padding: 1rem 2rem;">Register for Support</a>
    </div>
</section>
"""

# Registries Header
header_registries = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Awarding Bodies | Kensington Ivy</title>')
header_registries = re.sub(r'<style>.*?</style>', '', header_registries, flags=re.DOTALL)
header_registries = header_registries.replace('</head>', """<style>
body { background-color: var(--off, #faf9f6); }
.hero-clean { background: var(--navy); padding: 8rem 0 6rem 0; color: #fff; text-align: center; }
.hero-clean h1 { font-family: var(--ff-head); font-size: 3.5rem; margin-bottom: 1.5rem; }
.hero-clean p { font-size: 1.2rem; color: rgba(255,255,255,0.7); max-width: 700px; margin: 0 auto; }

.accordion-section { padding: 6rem 0; background: #fff; }
.accordion-item { border-bottom: 1px solid rgba(0,0,0,0.1); margin-bottom: 1rem; }
.accordion-header { width: 100%; text-align: left; background: none; border: none; padding: 1.5rem 0; font-family: var(--ff-head); font-size: 1.4rem; color: var(--navy); font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
.accordion-header:hover { color: var(--gold); }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }
.accordion-content-inner { padding-bottom: 1.5rem; color: #666; line-height: 1.6; }
.tag-container { margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }
.tag { padding: 0.25rem 0.75rem; background: rgba(201,162,88,0.1); color: var(--gold); border-radius: 50px; font-size: 0.8rem; font-weight: 600; }

.uni-section { padding: 6rem 0; background: var(--off, #faf9f6); }
.uni-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; margin-top: 3rem; }
.uni-card { background: #fff; padding: 1rem 1.5rem; border: 1px solid rgba(0,0,0,0.05); border-radius: 8px; font-weight: 500; color: var(--navy); display: flex; align-items: center; gap: 0.5rem; }
.uni-card i { color: var(--gold); }
</style>
</head>""")

registries_content = """
<section class="hero-clean">
    <div class="container">
        <h1>UK Awarding Bodies & Registries</h1>
        <p>We meticulously evaluate qualifications from all major examination boards to optimally position your academic profile.</p>
    </div>
</section>

<section class="accordion-section">
    <div class="container" style="max-width: 800px;">
        <h2 style="font-family: var(--ff-head); font-size: 2.5rem; color: var(--navy); margin-bottom: 2rem; text-align: center;">Examination Boards</h2>
        
        <div class="accordion-item">
            <button class="accordion-header">Pearson Edexcel <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>The UK's largest awarding organization, offering academic and vocational qualifications recognized globally by top-tier institutions.</p>
                    <div class="tag-container"><span class="tag">A-Levels</span><span class="tag">GCSEs</span><span class="tag">BTEC Nationals</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">Assessment & Qualifications Alliance (AQA) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>An independent education charity and the largest provider of academic qualifications taught in schools and colleges in England.</p>
                    <div class="tag-container"><span class="tag">A-Levels</span><span class="tag">GCSEs</span><span class="tag">EPQ</span></div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <button class="accordion-header">Oxford, Cambridge and RSA (OCR) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A leading UK awarding body providing a wide range of academic and vocational qualifications to meet diverse learner needs.</p>
                    <div class="tag-container"><span class="tag">A-Levels</span><span class="tag">Cambridge Nationals</span></div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <button class="accordion-header">Cambridge International Education (CAIE) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>The world's largest provider of international education programmes, highly valued by elite UK and global universities.</p>
                    <div class="tag-container"><span class="tag">Intl. A-Levels</span><span class="tag">IGCSE</span></div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <button class="accordion-header">International Baccalaureate (IB) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A highly prestigious global educational foundation offering a rigorous Diploma Programme celebrated by Ivy League and Russell Group universities.</p>
                    <div class="tag-container"><span class="tag">IB Diploma</span><span class="tag">Career-related</span></div>
                </div>
            </div>
        </div>

        <div class="accordion-item">
            <button class="accordion-header">Welsh Joint Education Committee (WJEC/Eduqas) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>Providing highly respected examinations and educational resources to schools across Wales, England, and Northern Ireland.</p>
                    <div class="tag-container"><span class="tag">A-Levels</span><span class="tag">Vocational</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">City & Guilds <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A global leader in skills development, providing industry-standard vocational and technical qualifications.</p>
                    <div class="tag-container"><span class="tag">T-Levels</span><span class="tag">NVQs</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">NCFE / CACHE <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A national awarding organisation advancing learning by designing high-quality technical and professional qualifications.</p>
                    <div class="tag-container"><span class="tag">T-Levels</span><span class="tag">V-Certs</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">Scottish Qualifications Authority (SQA) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>Scotland's national body for qualifications, responsible for developing and certifying qualifications in Scotland.</p>
                    <div class="tag-container"><span class="tag">Highers</span><span class="tag">Advanced Highers</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">CCEA <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>Northern Ireland's awarding body, advising the government on curriculum and examinations.</p>
                    <div class="tag-container"><span class="tag">A-Levels</span><span class="tag">GCSEs</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">UAL Awarding Body <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A specialist creative arts awarding body offering qualifications designed specifically for the creative industries.</p>
                    <div class="tag-container"><span class="tag">Art & Design</span><span class="tag">Performing Arts</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">VTCT <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A specialist awarding organisation providing qualifications for the hair, beauty, hospitality and sports industries.</p>
                    <div class="tag-container"><span class="tag">Hospitality</span><span class="tag">Beauty Therapy</span></div>
                </div>
            </div>
        </div>
        
        <div class="accordion-item">
            <button class="accordion-header">London Institute of Banking & Finance (LIBF) <i data-lucide="chevron-down"></i></button>
            <div class="accordion-content">
                <div class="accordion-content-inner">
                    <p>A specialist institute offering qualifications in financial services, banking, and business.</p>
                    <div class="tag-container"><span class="tag">Finance</span><span class="tag">Business</span></div>
                </div>
            </div>
        </div>

    </div>
</section>

<section class="uni-section">
    <div class="container">
        <h2 style="font-family: var(--ff-head); font-size: 2.5rem; color: var(--navy); margin-bottom: 1rem; text-align: center;">Our University Partners</h2>
        <p style="color: #666; text-align: center; max-width: 600px; margin: 0 auto;">We maintain relationships with over 130+ institutions across the UK.</p>
        
        <div class="uni-grid">
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Oxford</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Cambridge</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Imperial College</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> UCL</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> LSE</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> King's College</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Edinburgh</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Manchester</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Bristol</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Warwick</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Glasgow</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Birmingham</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Leeds</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Sheffield</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Nottingham</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Southampton</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Newcastle</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Exeter</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Queen Mary</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> York</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Cardiff</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Durham</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Liverpool</div>
            <div class="uni-card"><i data-lucide="check-circle" style="width:16px;"></i> Queen's Belfast</div>
            <div class="uni-card" style="justify-content: center; background: none; border: none;">...and many more</div>
        </div>
    </div>
</section>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const headers = document.querySelectorAll('.accordion-header');
        headers.forEach(header => {
            header.addEventListener('click', () => {
                const content = header.nextElementSibling;
                const icon = header.querySelector('i');
                if (content.style.maxHeight) {
                    content.style.maxHeight = null;
                    icon.style.transform = 'rotate(0deg)';
                } else {
                    // Close others
                    document.querySelectorAll('.accordion-content').forEach(c => c.style.maxHeight = null);
                    document.querySelectorAll('.accordion-header i').forEach(i => i.style.transform = 'rotate(0deg)');
                    
                    content.style.maxHeight = content.scrollHeight + "px";
                    icon.style.transform = 'rotate(180deg)';
                }
            });
        });
    });
</script>
"""

with open('pages/clearing-support.html', 'w', encoding='utf-8') as f:
    f.write(header_clearing + clearing_content + footer)

with open('pages/registries.html', 'w', encoding='utf-8') as f:
    f.write(header_registries + registries_content + footer)
