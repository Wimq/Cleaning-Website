import os
import glob
import re

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

footer_template = """<footer style="background: var(--navy); padding: 5rem 0 3rem 0; color: #fff;">
    <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 4rem; margin-bottom: 4rem;">
            
            <div style="grid-column: span 1;">
                <a href="{ROOT}index.html" class="logo" style="display: block; margin-bottom: 1.5rem;">
                    <span style="font-family: var(--ff-head); font-weight: 800; font-size: 2rem; color: #fff;">Kensington</span><span style="font-family: var(--ff-head); font-weight: 800; font-size: 2rem; color: var(--gold);">Ivy</span>
                </a>
                <p style="color: rgba(255,255,255,0.7); font-size: 0.95rem; line-height: 1.6; max-width: 320px; margin-bottom: 2rem;">UK's trusted university placement and admissions partner. Built on academic excellence.</p>
                <div style="display: flex; gap: 1rem;">
                    <a href="#" aria-label="Instagram" style="width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; color: #fff; transition: background 0.3s ease;"><i data-lucide="instagram" style="width: 20px;"></i></a>
                    <a href="#" aria-label="TikTok" style="width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; color: #fff; transition: background 0.3s ease;">
                        <svg viewBox="0 0 24 24" fill="currentColor" style="width: 20px; height: 20px;"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"/></svg>
                    </a>
                    <a href="#" aria-label="LinkedIn" style="width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; color: #fff; transition: background 0.3s ease;"><i data-lucide="linkedin" style="width: 20px;"></i></a>
                    <a href="https://uk.trustpilot.com/review/kensingtonivy.co.uk" target="_blank" aria-label="Trustpilot" style="width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; color: #00b67a; transition: background 0.3s ease;"><i data-lucide="star" style="width: 20px; fill: #00b67a;"></i></a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.3rem; margin-bottom: 2rem; color: #fff;">Menu</h4>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <a href="{ROOT}index.html" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">Home</a>
                    <a href="{ROOT}pages/about.html?v=3" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">About Us</a>
                    <a href="{ROOT}pages/registries.html" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">University Registries</a>
                    <a href="{ROOT}pages/foundation-years.html" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">Foundation Years</a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.3rem; margin-bottom: 2rem; color: #fff;">Legal</h4>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <a href="{ROOT}pages/legal/privacy.html" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">Privacy Policy</a>
                    <a href="{ROOT}pages/legal/terms.html" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">Website Terms</a>
                    <a href="{ROOT}pages/legal/cookies.html" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; transition: color 0.3s ease;">Cookie Policy</a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.3rem; margin-bottom: 2rem; color: #fff;">Contact Us</h4>
                <div style="display: flex; flex-direction: column; gap: 1.2rem;">
                    <div style="display: flex; gap: 1rem; color: rgba(255,255,255,0.7);">
                        <i data-lucide="map-pin" style="width: 20px; flex-shrink: 0; color: var(--gold);"></i>
                        <p style="font-size: 0.95rem;">453 South End Road,<br>Hornchurch, England, RM12 5NX</p>
                    </div>
                    <div style="display: flex; gap: 1rem;">
                        <i data-lucide="mail" style="width: 20px; flex-shrink: 0; color: var(--gold);"></i>
                        <a href="mailto:enquiries@kensingtonivy.co.uk" style="color: rgba(255,255,255,0.7); font-size: 0.95rem; text-decoration: underline;">enquiries@kensingtonivy.co.uk</a>
                    </div>
                    <div style="display: flex; gap: 1rem;">
                        <i data-lucide="phone" style="width: 20px; flex-shrink: 0; color: var(--gold);"></i>
                        <a href="tel:02074440009" style="color: rgba(255,255,255,0.7); font-size: 0.95rem;">020 7444 0009</a>
                    </div>
                </div>
            </div>
        </div>

        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; color: rgba(255,255,255,0.5); font-size: 0.85rem; flex-wrap: wrap; gap: 1rem;">
            <p>&copy; <span class="dynamic-year">2026</span> Kensington Ivy LTD (Company No. 17167406). All rights reserved.</p>
            <div style="opacity: 0.6;">
                <a href="https://www.dmca.com/Protection/Status.aspx?ID=f3d4db82-c26d-44f0-87c5-10d923a53d0b" title="DMCA.com Protection Status" class="dmca-badge"> 
                    <img src="https://images.dmca.com/Badges/dmca_protected_sml_120n.png?ID=f3d4db82-c26d-44f0-87c5-10d923a53d0b" alt="DMCA.com Protection Status" style="display: block;" />
                </a>
            </div>
        </div>
    </div>
</footer>"""

for file_path in html_files:
    if "node_modules" in file_path or ".antigravityignore" in file_path:
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine depth for root prefix
    rel_path = os.path.relpath(file_path, workspace)
    depth = rel_path.count(os.sep)
    
    root_prefix = "../" * depth
    if root_prefix == "":
        root_prefix = "" # for index.html at root, it's just "pages/..."

    formatted_footer = footer_template.replace("{ROOT}", root_prefix)

    # Regex to find footer tag and all its contents
    # This regex is a bit tricky with nested tags, but we know the footer ends with </footer>
    new_content = re.sub(r'<footer.*?</footer>', formatted_footer, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {rel_path}")
