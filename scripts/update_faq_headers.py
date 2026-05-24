import os
import glob

def get_faq_header():
    return """<header class="header">
    <div class="container header-inner">
        <a href="../../index.html" class="logo">
            <span class="logo-text">Kensington</span><span class="logo-accent">Ivy</span>
        </a>
        <nav class="top-links" style="gap: 2rem;">
            <a href="faq.html" style="color: var(--navy); font-weight: 500;">Help Center</a>
            <a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../about.html" style="color: var(--navy); font-weight: 500;">About Us</a>
        </nav>
        <div style="display: flex; gap: 1rem; align-items: center;">
            <a href="../register.html" class="btn btn-gold">Apply Now</a>
            <button class="menu-toggle" onclick="document.querySelector('.top-links').classList.toggle('active')" aria-label="Toggle Menu">
                <i data-lucide="menu"></i>
            </button>
        </div>
    </div>
</header>"""

def replace_navbar(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the old navbar. It starts with <nav class="navbar" and ends with </nav>
    start_tag = '<nav class="navbar"'
    end_tag = '</nav>'
    
    start_idx = content.find(start_tag)
    if start_idx != -1:
        end_idx = content.find(end_tag, start_idx) + len(end_tag)
        new_content = content[:start_idx] + get_faq_header() + content[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
        return

    # In sub pages, the old navbar might not exist, but let's check
    print(f"No <nav> found in {filepath}")

faq_files = glob.glob('pages/faq/*.html')
for f in faq_files:
    replace_navbar(f)
