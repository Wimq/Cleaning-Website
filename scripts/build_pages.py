import os
import re

# Read index.html for base template
with open('index.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Extract header (up to the end of <nav class="secondary-nav"> block)
header_match = re.search(r'(.*?<\/nav>)', base_html, re.DOTALL)
header = header_match.group(1) if header_match else ""

# Fix page title for new pages
header_clearing = re.sub(r'<title>.*?</title>', '<title>Clearing Support | Kensington Ivy</title>', header)
header_registries = re.sub(r'<title>.*?</title>', '<title>University Registries | Kensington Ivy</title>', header)

# Extract footer
footer_match = re.search(r'(<footer class="footer">.*)', base_html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

def fix_paths(html_str):
    html_str = html_str.replace('href="css/', 'href="../css/')
    html_str = html_str.replace('src="assets/', 'src="../assets/')
    html_str = html_str.replace('href="pages/', 'href=""')
    html_str = html_str.replace('href="index.html"', 'href="../index.html"')
    return html_str

# Safer path fixing
def fix_paths_safe(html_str):
    h = html_str.replace('href="css/', 'href="../css/')
    h = h.replace('src="assets/', 'src="../assets/')
    h = h.replace('href="pages/', 'href=""')
    h = h.replace('href="index.html"', 'href="../index.html"')
    return h

header_clearing = fix_paths_safe(header_clearing)
header_registries = fix_paths_safe(header_registries)
footer = fix_paths_safe(footer)

clearing_content = """
<section class="container" style="padding: 8rem 0; min-height: 60vh;">
    <h1 style="font-family: var(--ff-head); font-size: 3rem; color: var(--navy); margin-bottom: 1.5rem;">Elite UCAS Clearing Representation.</h1>
    <p style="font-size: 1.2rem; color: #555; max-width: 800px; line-height: 1.8; margin-bottom: 3rem;">
        The Clearing window is highly competitive and extremely time-sensitive. We act as your private admissions advocates, bypassing the standard queues to negotiate directly with university decision-makers. Whether you've missed your required grades or decided on a last-minute change of direction, our senior consultants secure premium placements in hours, not weeks.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
        <div style="background: #fdfbf7; padding: 2rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05);">
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.5rem; margin-bottom: 1rem;"><i data-lucide="phone-call" style="color: var(--gold); vertical-align: middle; margin-right: 0.5rem;"></i> Direct Admissions Access</h3>
            <p style="color: #666; line-height: 1.6;">We don't wait on hold. We bypass the standard applicant hotlines and speak directly to our trusted contacts within university admissions boards.</p>
        </div>
        <div style="background: #fdfbf7; padding: 2rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05);">
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.5rem; margin-bottom: 1rem;"><i data-lucide="file-check" style="color: var(--gold); vertical-align: middle; margin-right: 0.5rem;"></i> Rapid Grade-Negotiation</h3>
            <p style="color: #666; line-height: 1.6;">Missed your offer by a single grade? Our senior consultants excel at portfolio and profile negotiation, successfully advocating for students who fall marginally short.</p>
        </div>
        <div style="background: #fdfbf7; padding: 2rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05);">
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.5rem; margin-bottom: 1rem;"><i data-lucide="clock" style="color: var(--gold); vertical-align: middle; margin-right: 0.5rem;"></i> 24-Hour Turnaround</h3>
            <p style="color: #666; line-height: 1.6;">During the Clearing window, speed is everything. We guarantee an initial profile assessment and strategic action plan within hours of your enquiry.</p>
        </div>
    </div>
    
    <a href="register.html" class="btn btn-gold" style="font-size: 1.1rem; padding: 1rem 2rem;">Request Urgent Placement Review <i data-lucide="arrow-right"></i></a>
</section>
"""

registries_content = """
<section class="container" style="padding: 8rem 0; min-height: 60vh;">
    <h1 style="font-family: var(--ff-head); font-size: 3rem; color: var(--navy); margin-bottom: 1.5rem;">University Registries & Partners</h1>
    <p style="font-size: 1.2rem; color: #555; max-width: 800px; line-height: 1.8; margin-bottom: 3rem;">
        Kensington Ivy holds direct partnerships and deep-rooted relationships with the UK's most prestigious educational bodies and university registries. This extensive network allows us to advocate for our students directly at the board level, bypassing traditional application bottlenecks.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
        <div style="text-align: center; padding: 3rem; background: #fff; border: 1px solid rgba(0,0,0,0.05); border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <div style="width: 80px; height: 80px; background: rgba(201,162,88,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem auto;">
                <i data-lucide="building-2" style="width: 40px; height: 40px; color: var(--gold);"></i>
            </div>
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.3rem;">Russell Group Institutions</h3>
        </div>
        <div style="text-align: center; padding: 3rem; background: #fff; border: 1px solid rgba(0,0,0,0.05); border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <div style="width: 80px; height: 80px; background: rgba(201,162,88,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem auto;">
                <i data-lucide="landmark" style="width: 40px; height: 40px; color: var(--gold);"></i>
            </div>
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.3rem;">Medical & Dental Schools Council</h3>
        </div>
        <div style="text-align: center; padding: 3rem; background: #fff; border: 1px solid rgba(0,0,0,0.05); border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <div style="width: 80px; height: 80px; background: rgba(201,162,88,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem auto;">
                <i data-lucide="gavel" style="width: 40px; height: 40px; color: var(--gold);"></i>
            </div>
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.3rem;">UK Law Societies</h3>
        </div>
        <div style="text-align: center; padding: 3rem; background: #fff; border: 1px solid rgba(0,0,0,0.05); border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <div style="width: 80px; height: 80px; background: rgba(201,162,88,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem auto;">
                <i data-lucide="globe-2" style="width: 40px; height: 40px; color: var(--gold);"></i>
            </div>
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.3rem;">International Pathway Providers</h3>
        </div>
    </div>
    
    <div style="background: var(--navy); border-radius: 20px; padding: 4rem; text-align: center; color: #fff; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient(circle at center, rgba(201,162,88,0.1) 0%, transparent 70%);"></div>
        <div style="position: relative; z-index: 2;">
            <h2 style="font-family: var(--ff-head); font-size: 2.5rem; margin-bottom: 1rem;">Are you an educational body?</h2>
            <p style="font-size: 1.1rem; color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 2rem auto;">Partner with Kensington Ivy to gain access to our rigorous pipeline of pre-vetted, high-achieving domestic and international students.</p>
            <a href="register.html?course=Partnership%20Enquiry" class="btn btn-gold" style="padding: 1rem 2.5rem; font-size: 1.1rem;">Discuss Partnership</a>
        </div>
    </div>
</section>
"""

with open('pages/clearing-support.html', 'w', encoding='utf-8') as f:
    f.write(header_clearing + clearing_content + footer)

with open('pages/registries.html', 'w', encoding='utf-8') as f:
    f.write(header_registries + registries_content + footer)

# Fix the global links in index.html and responsive/index.html via simple python replace
for file in ['index.html', 'responsive/index.html']:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the FAQ link for University Registries with registries.html
        content = content.replace('href="pages/faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>', 'href="pages/registries.html" style="color: var(--navy); font-weight: 500;">University Registries</a>')
        content = content.replace('href="../pages/faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>', 'href="../pages/registries.html" style="color: var(--navy); font-weight: 500;">University Registries</a>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
