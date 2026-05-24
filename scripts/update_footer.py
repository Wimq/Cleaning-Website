import os
import glob
import re

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

footer_template = """<footer style="background: linear-gradient(to bottom, #111827, var(--navy)); padding: 6rem 0 3rem 0; color: #fff; border-top: 4px solid var(--gold); position: relative; overflow: hidden;">
    <!-- Background subtle glow -->
    <div style="position: absolute; top: 0; right: 10%; width: 300px; height: 300px; background: radial-gradient(circle, rgba(201,162,88,0.05) 0%, rgba(0,0,0,0) 70%); border-radius: 50%; pointer-events: none;"></div>

    <div class="container" style="position: relative; z-index: 2;">
        <!-- Pre-footer CTA -->
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 3rem; margin-bottom: 5rem; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem;">
            <div>
                <h3 style="font-family: var(--ff-head); font-size: 2rem; color: #fff; margin-bottom: 0.5rem;">Ready to secure your future?</h3>
                <p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin: 0;">Speak to our admissions experts today for a free consultation.</p>
            </div>
            <a href="{ROOT}pages/register.html" class="btn btn-gold" style="font-size: 1.1rem; padding: 1rem 2.5rem; border-radius: 50px;">Start Your Journey</a>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 4rem; margin-bottom: 4rem;">
            
            <div style="grid-column: span 1;">
                <a href="{ROOT}index.html" class="logo" style="display: block; margin-bottom: 1.5rem; text-decoration: none;">
                    <span style="font-family: var(--ff-head); font-weight: 800; font-size: 2.2rem; color: #fff; letter-spacing: -0.5px;">Kensington</span><span style="font-family: var(--ff-head); font-weight: 800; font-size: 2.2rem; color: var(--gold);">Ivy</span>
                </a>
                <p style="color: rgba(255,255,255,0.6); font-size: 0.95rem; line-height: 1.8; max-width: 320px; margin-bottom: 2.5rem;">The UK's premier university placement and admissions partner. Built on absolute academic excellence.</p>
                <div style="display: flex; gap: 1rem;">
                    <a href="#" aria-label="Instagram" style="color: rgba(255,255,255,0.5); transition: color 0.3s ease; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='rgba(255,255,255,0.5)'">
                        <i data-lucide="instagram" style="width: 24px; height: 24px; stroke-width: 1.5px;"></i>
                    </a>
                    <a href="#" aria-label="TikTok" style="color: rgba(255,255,255,0.5); transition: color 0.3s ease; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='rgba(255,255,255,0.5)'">
                        <svg viewBox="0 0 24 24" fill="currentColor" style="width: 22px; height: 22px;"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64 2.93 2.93 0 0 1 .88.13V9.4a6.84 6.84 0 0 0-1-.05A6.33 6.33 0 0 0 5 20.1a6.34 6.34 0 0 0 10.86-4.43v-7a8.16 8.16 0 0 0 4.77 1.52v-3.4a4.85 4.85 0 0 1-1-.1z"/></svg>
                    </a>
                    <a href="#" aria-label="LinkedIn" style="color: rgba(255,255,255,0.5); transition: color 0.3s ease; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='rgba(255,255,255,0.5)'">
                        <i data-lucide="linkedin" style="width: 24px; height: 24px; stroke-width: 1.5px;"></i>
                    </a>
                    <a href="https://uk.trustpilot.com/review/kensingtonivy.co.uk" target="_blank" aria-label="Trustpilot" style="color: rgba(255,255,255,0.5); transition: color 0.3s ease; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.color='#00b67a'" onmouseout="this.style.color='rgba(255,255,255,0.5)'">
                        <i data-lucide="star" style="width: 24px; height: 24px; stroke-width: 1.5px;"></i>
                    </a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.2rem; margin-bottom: 2rem; color: #fff; text-transform: uppercase; letter-spacing: 1px;">Navigation</h4>
                <div style="display: flex; flex-direction: column; gap: 1.2rem;">
                    <a href="{ROOT}index.html" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Home</a>
                    <a href="{ROOT}pages/about.html?v=3" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">About Us</a>
                    <a href="{ROOT}pages/registries.html" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">University Registries</a>
                    <a href="{ROOT}pages/foundation-years.html" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Foundation Years</a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.2rem; margin-bottom: 2rem; color: #fff; text-transform: uppercase; letter-spacing: 1px;">Legal</h4>
                <div style="display: flex; flex-direction: column; gap: 1.2rem;">
                    <a href="{ROOT}pages/legal/privacy.html" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Privacy Policy</a>
                    <a href="{ROOT}pages/legal/terms.html" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Website Terms</a>
                    <a href="{ROOT}pages/legal/cookies.html" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">Cookie Policy</a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.2rem; margin-bottom: 2rem; color: #fff; text-transform: uppercase; letter-spacing: 1px;">Contact</h4>
                <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                    <div style="display: flex; gap: 1rem; color: rgba(255,255,255,0.6); align-items: flex-start;">
                        <i data-lucide="map-pin" style="width: 20px; height: 20px; flex-shrink: 0; color: var(--gold); margin-top: 2px;"></i>
                        <p style="font-size: 0.95rem; margin: 0; line-height: 1.5;">453 South End Road,<br>Hornchurch, England, RM12 5NX</p>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: center;">
                        <i data-lucide="mail" style="width: 20px; height: 20px; flex-shrink: 0; color: var(--gold);"></i>
                        <a href="mailto:enquiries@kensingtonivy.co.uk" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">enquiries@kensingtonivy.co.uk</a>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: center;">
                        <i data-lucide="phone" style="width: 20px; height: 20px; flex-shrink: 0; color: var(--gold);"></i>
                        <a href="tel:02074440009" style="color: rgba(255,255,255,0.6); font-size: 0.95rem; text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">020 7444 0009</a>
                    </div>
                </div>
            </div>
        </div>

        <div style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; color: rgba(255,255,255,0.4); font-size: 0.85rem; flex-wrap: wrap; gap: 1rem;">
            <p style="margin: 0;">&copy; <span class="dynamic-year">2026</span> Kensington Ivy LTD (Company No. 17167406). All rights reserved.</p>
            <div style="opacity: 0.8;">
                <a href="https://www.dmca.com/Protection/Status.aspx?ID=f3d4db82-c26d-44f0-87c5-10d923a53d0b" title="DMCA.com Protection Status" class="dmca-badge" style="display: block;"> 
                    <img src="https://images.dmca.com/Badges/dmca_protected_sml_120n.png?ID=f3d4db82-c26d-44f0-87c5-10d923a53d0b" alt="DMCA.com Protection Status" style="display: block; border-radius: 4px;" />
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
    new_content = re.sub(r'<footer.*?</footer>', formatted_footer, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {rel_path}")
