import os

with open('pages/find-courses.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

header_lines = lines[:198]  # up to </header>
footer_lines = lines[271:]  # from <footer ...> to end of file

header = "".join(header_lines)
footer = "".join(footer_lines)

# Fix title for clearing
header_clearing = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>Clearing Support | KensingtonIvy</title>')
# Remove secondary styling block from find-courses.html (from <style> to </style>)
import re
header_clearing = re.sub(r'<style>.*?</style>', '', header_clearing, flags=re.DOTALL)

# Add custom body background because the main site uses var(--off)
header_clearing = header_clearing.replace('</head>', '<style>body { background-color: var(--off, #faf9f6); padding-top: 100px; }</style>\n</head>')

header_registries = header.replace('<title>Find Courses | KensingtonIvy</title>', '<title>University Registries | KensingtonIvy</title>')
header_registries = re.sub(r'<style>.*?</style>', '', header_registries, flags=re.DOTALL)
header_registries = header_registries.replace('</head>', '<style>body { background-color: var(--off, #faf9f6); padding-top: 100px; }</style>\n</head>')


clearing_content = """
<section class="container" style="padding: 6rem 0; min-height: 60vh;">
    <h1 style="font-family: var(--ff-head); font-size: 3rem; color: var(--navy); margin-bottom: 1.5rem;">Elite UCAS Clearing Representation.</h1>
    <p style="font-size: 1.2rem; color: #555; max-width: 800px; line-height: 1.8; margin-bottom: 3rem;">
        The Clearing window is highly competitive and extremely time-sensitive. We act as your private admissions advocates, bypassing the standard queues to negotiate directly with university decision-makers. Whether you've missed your required grades or decided on a last-minute change of direction, our senior consultants secure premium placements in hours, not weeks.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
        <div style="background: #fff; padding: 2.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.5rem; margin-bottom: 1rem;"><i data-lucide="phone-call" style="color: var(--gold); vertical-align: middle; margin-right: 0.5rem;"></i> Direct Admissions Access</h3>
            <p style="color: #666; line-height: 1.6;">We don't wait on hold. We bypass the standard applicant hotlines and speak directly to our trusted contacts within university admissions boards.</p>
        </div>
        <div style="background: #fff; padding: 2.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.5rem; margin-bottom: 1rem;"><i data-lucide="file-check" style="color: var(--gold); vertical-align: middle; margin-right: 0.5rem;"></i> Rapid Grade-Negotiation</h3>
            <p style="color: #666; line-height: 1.6;">Missed your offer by a single grade? Our senior consultants excel at portfolio and profile negotiation, successfully advocating for students who fall marginally short.</p>
        </div>
        <div style="background: #fff; padding: 2.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-family: var(--ff-head); font-size: 1.5rem; margin-bottom: 1rem;"><i data-lucide="clock" style="color: var(--gold); vertical-align: middle; margin-right: 0.5rem;"></i> 24-Hour Turnaround</h3>
            <p style="color: #666; line-height: 1.6;">During the Clearing window, speed is everything. We guarantee an initial profile assessment and strategic action plan within hours of your enquiry.</p>
        </div>
    </div>
    
    <a href="register.html" class="btn btn-gold" style="font-size: 1.1rem; padding: 1rem 2rem; display: inline-flex; align-items: center; gap: 0.5rem;">REQUEST URGENT PLACEMENT REVIEW <i data-lucide="arrow-right"></i></a>
</section>
"""

registries_content = """
<section class="container" style="padding: 6rem 0; min-height: 60vh;">
    <h1 style="font-family: var(--ff-head); font-size: 3rem; color: var(--navy); margin-bottom: 1.5rem;">UK Educational Bodies</h1>
    <p style="font-size: 1.2rem; color: #555; max-width: 800px; line-height: 1.8; margin-bottom: 3rem;">
        Kensington Ivy holds deep-rooted relationships and aligns applications with the UK's most prestigious professional educational bodies and university registries. This extensive network allows us to ensure your academic profile meets the exact professional standards required for your future career.
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 4rem;">
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">General Medical Council (GMC)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">General Dental Council (GDC)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Solicitors Regulation Authority (SRA)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Bar Standards Board (BSB)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">British Psychological Society (BPS)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Royal Institute of British Architects (RIBA)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Institution of Engineering and Technology (IET)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">General Pharmaceutical Council (GPhC)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Nursing and Midwifery Council (NMC)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Health & Care Professions Council (HCPC)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">British Assoc. for Counselling (BACP)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Chartered Institute of Mgmt Accountants (CIMA)</h3>
        </div>
        <div style="background: #fff; padding: 1.5rem 2rem; border-left: 4px solid var(--gold); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
            <h3 style="color: var(--navy); font-size: 1.1rem; font-weight: 600;">Assoc. of Chartered Certified Accountants (ACCA)</h3>
        </div>
    </div>
</section>
"""

with open('pages/clearing-support.html', 'w', encoding='utf-8') as f:
    f.write(header_clearing + clearing_content + footer)

with open('pages/registries.html', 'w', encoding='utf-8') as f:
    f.write(header_registries + registries_content + footer)

