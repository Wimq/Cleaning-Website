import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

injection_code = """
<!-- Floating Cookie Button -->
<button id="floatingCookieBtn" onclick="document.getElementById('cookieBanner').classList.add('visible');" style="position: fixed; bottom: 20px; left: 20px; z-index: 9998; background: var(--navy); color: #fff; width: 50px; height: 50px; border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; border: 2px solid rgba(255,255,255,0.1); cursor: pointer; transition: all 0.3s ease;">
    <i data-lucide="cookie" style="width: 24px; height: 24px;"></i>
</button>

<!-- Accessibility Widget Trigger -->
<button id="accessibilityBtn" onclick="toggleAccessibilityPanel()" style="position: fixed; bottom: 20px; right: 20px; z-index: 9998; background: var(--gold); color: var(--navy); width: 60px; height: 60px; border-radius: 50%; box-shadow: 0 10px 25px rgba(201,162,88,0.4); display: flex; align-items: center; justify-content: center; border: none; cursor: pointer; transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
    <i data-lucide="accessibility" style="width: 32px; height: 32px;"></i>
</button>

<!-- Full Height Accessibility Side Panel -->
<div id="accSidePanelOverlay" onclick="toggleAccessibilityPanel()" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.4); z-index: 9999; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; backdrop-filter: blur(4px);"></div>
<div id="accSidePanel" style="position: fixed; top: 0; right: -450px; width: 400px; max-width: 100vw; height: 100vh; background: #fff; box-shadow: -10px 0 30px rgba(0,0,0,0.1); z-index: 10000; transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1); display: flex; flex-direction: column; overflow: hidden;">
    <div style="padding: 1rem 1.5rem; border-bottom: 1px solid rgba(0,0,0,0.05); display: flex; justify-content: space-between; align-items: center; background: #fff;">
        <h3 style="margin: 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem; font-family: var(--ff-head); color: var(--navy);"><i data-lucide="accessibility" style="color: var(--gold); width: 20px;"></i> Accessibility Suite</h3>
        <button onclick="toggleAccessibilityPanel()" style="background: rgba(10,17,40,0.05); border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border: none; color: var(--navy); cursor: pointer; transition: background 0.3s ease;"><i data-lucide="x" style="width: 16px;"></i></button>
    </div>
    
    <div style="flex: 1; overflow-y: auto; padding: 1.5rem; background: #fdfbf7;" class="acc-panel-scrollable">
        
        <!-- Translate Box -->
        <div class="acc-section-box">
            <div class="acc-section-header">Translate Page</div>
            <div style="padding: 1rem;">
                <div class="custom-select-wrapper">
                    <div class="gtranslate_wrapper"></div>
                </div>
            </div>
        </div>
        
        <!-- Color Scheme & Text Size Box -->
        <div class="acc-section-box">
            <div class="acc-section-header">Display Settings</div>
            
            <div style="padding: 1rem; border-bottom: 1px solid rgba(0,0,0,0.05);">
                <div style="display: flex; gap: 0.5rem; background: #fdfbf7; padding: 0.25rem; border-radius: 8px; border: 1px solid rgba(0,0,0,0.05);">
                    <button class="scheme-btn active" onclick="setColorScheme('light', this)" style="flex: 1; padding: 0.5rem; border-radius: 6px; border: none; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.05); cursor: pointer; font-size: 0.8rem; color: var(--navy); font-weight: 600; transition: all 0.2s;"><i data-lucide="sun" style="width: 14px; margin-bottom: 2px; display: block; margin: 0 auto 2px auto;"></i> Light</button>
                    <button class="scheme-btn" onclick="setColorScheme('dark', this)" style="flex: 1; padding: 0.5rem; border-radius: 6px; border: none; background: transparent; cursor: pointer; font-size: 0.8rem; color: #666; font-weight: 500; transition: all 0.2s;"><i data-lucide="moon" style="width: 14px; margin-bottom: 2px; display: block; margin: 0 auto 2px auto;"></i> Dark</button>
                    <button class="scheme-btn" onclick="setColorScheme('contrast', this)" style="flex: 1; padding: 0.5rem; border-radius: 6px; border: none; background: transparent; cursor: pointer; font-size: 0.8rem; color: #666; font-weight: 500; transition: all 0.2s;"><i data-lucide="contrast" style="width: 14px; margin-bottom: 2px; display: block; margin: 0 auto 2px auto;"></i> Contrast</button>
                </div>
            </div>

            <div style="padding: 1rem;">
                <div style="display: flex; gap: 0.5rem; background: #fdfbf7; padding: 0.25rem; border-radius: 8px; border: 1px solid rgba(0,0,0,0.05);">
                    <button onclick="changeFontSize(-1)" style="flex: 1; padding: 0.5rem; border-radius: 6px; border: none; background: transparent; cursor: pointer; font-size: 0.9rem; color: #666; font-weight: 600; transition: all 0.2s;">A-</button>
                    <button onclick="changeFontSize(0)" style="flex: 1; padding: 0.5rem; border-radius: 6px; border: none; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.05); cursor: pointer; font-size: 0.85rem; color: var(--navy); font-weight: 600; transition: all 0.2s;">Default</button>
                    <button onclick="changeFontSize(1)" style="flex: 1; padding: 0.5rem; border-radius: 6px; border: none; background: transparent; cursor: pointer; font-size: 1.1rem; color: #666; font-weight: 600; transition: all 0.2s;">A+</button>
                </div>
            </div>
        </div>
        
        <!-- Reading Tools Box -->
        <div class="acc-section-box" style="margin-bottom: 1rem;">
            <div class="acc-section-header">Reading Tools</div>
            
            <!-- Dyslexia Font -->
            <div class="acc-toggle-row">
                <div class="acc-toggle-info">
                    <i data-lucide="book-open"></i>
                    <div>
                        <span class="acc-toggle-title">Dyslexia Font</span>
                        <span class="acc-toggle-desc">Highly readable font</span>
                    </div>
                </div>
                <label class="ios-toggle">
                    <input type="checkbox" onchange="toggleAccClass('dyslexia-font', this)">
                    <span class="ios-slider"></span>
                </label>
            </div>

            <!-- Big Cursor -->
            <div class="acc-toggle-row">
                <div class="acc-toggle-info">
                    <i data-lucide="mouse-pointer-2"></i>
                    <div>
                        <span class="acc-toggle-title">Big Cursor</span>
                        <span class="acc-toggle-desc">Increases pointer size</span>
                    </div>
                </div>
                <label class="ios-toggle">
                    <input type="checkbox" onchange="toggleAccClass('big-cursor', this)">
                    <span class="ios-slider"></span>
                </label>
            </div>

            <!-- Highlight Links -->
            <div class="acc-toggle-row">
                <div class="acc-toggle-info">
                    <i data-lucide="link-2"></i>
                    <div>
                        <span class="acc-toggle-title">Highlight Links</span>
                        <span class="acc-toggle-desc">Highlights clickables</span>
                    </div>
                </div>
                <label class="ios-toggle">
                    <input type="checkbox" onchange="toggleAccClass('highlight-links', this)">
                    <span class="ios-slider"></span>
                </label>
            </div>

            <!-- Letter Spacing -->
            <div class="acc-toggle-row">
                <div class="acc-toggle-info">
                    <i data-lucide="space"></i>
                    <div>
                        <span class="acc-toggle-title">Letter Spacing</span>
                        <span class="acc-toggle-desc">Wider text spacing</span>
                    </div>
                </div>
                <label class="ios-toggle">
                    <input type="checkbox" onchange="toggleAccClass('high-spacing', this)">
                    <span class="ios-slider"></span>
                </label>
            </div>

            <!-- Stop Animations -->
            <div class="acc-toggle-row no-border">
                <div class="acc-toggle-info">
                    <i data-lucide="play-circle"></i>
                    <div>
                        <span class="acc-toggle-title">Stop Animations</span>
                        <span class="acc-toggle-desc">Disables transitions</span>
                    </div>
                </div>
                <label class="ios-toggle">
                    <input type="checkbox" onchange="toggleAccClass('no-animations', this)">
                    <span class="ios-slider"></span>
                </label>
            </div>
        </div>
        
        <button onclick="resetAllAccessibility()" style="width: 100%; padding: 0.75rem; background: #fff; border: 1px solid rgba(0,0,0,0.15); box-shadow: 0 2px 5px rgba(0,0,0,0.02); color: #d9534f; font-weight: 600; font-size: 0.9rem; border-radius: 12px; cursor: pointer; transition: all 0.2s;"><i data-lucide="rotate-ccw" style="width: 16px; vertical-align: middle; margin-right: 4px;"></i> Reset All Settings</button>
    </div>
</div>

<script>
    window.gtranslateSettings = {
        "default_language": "en",
        "native_language_names": true,
        "wrapper_selector": ".gtranslate_wrapper"
    };
</script>
<script src="https://cdn.gtranslate.net/widgets/latest/dropdown.js" defer></script>

<style>
    /* Premium iOS Style Boxes */
    .acc-section-box {
        background: #fff;
        border-radius: 12px;
        border: 1px solid rgba(0,0,0,0.15);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        overflow: hidden;
    }
    .acc-section-header {
        background: #fafafa;
        padding: 0.75rem 1rem;
        font-weight: 600;
        color: var(--navy);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 1px solid rgba(0,0,0,0.05);
    }
    .acc-toggle-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #fff;
        padding: 0.75rem 1rem;
        border-bottom: 1px solid rgba(0,0,0,0.05);
    }
    .acc-toggle-row.no-border {
        border-bottom: none;
    }

    /* Premium Styled Dropdown for GTranslate */
    .custom-select-wrapper {
        position: relative;
    }
    .custom-select-wrapper select {
        width: 100%;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        border: 1px solid rgba(0,0,0,0.1) !important;
        background: #fff url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="%230a1128" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>') no-repeat right 1rem center !important;
        font-family: var(--ff-body) !important;
        font-size: 0.9rem !important;
        color: var(--navy) !important;
        appearance: none !important;
        -webkit-appearance: none !important;
        cursor: pointer;
        font-weight: 500;
    }
    .custom-select-wrapper select:focus {
        outline: none;
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 2px rgba(201,162,88,0.2) !important;
    }

    .acc-toggle-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    .acc-toggle-info i {
        color: var(--gold);
        width: 18px;
        height: 18px;
    }
    .acc-toggle-title {
        display: block;
        font-weight: 600;
        color: var(--navy);
        font-size: 0.9rem;
    }
    .acc-toggle-desc {
        display: block;
        font-size: 0.7rem;
        color: #777;
        margin-top: 1px;
    }
    .ios-toggle {
        position: relative;
        display: inline-block;
        width: 44px;
        height: 24px;
        flex-shrink: 0;
    }
    .ios-toggle input { 
        opacity: 0;
        width: 0;
        height: 0;
    }
    .ios-slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #e4e4e4;
        transition: .4s;
        border-radius: 34px;
    }
    .ios-slider:before {
        position: absolute;
        content: "";
        height: 20px;
        width: 20px;
        left: 2px;
        bottom: 2px;
        background-color: white;
        transition: .3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .ios-toggle input:checked + .ios-slider {
        background-color: var(--gold);
    }
    .ios-toggle input:checked + .ios-slider:before {
        transform: translateX(20px);
    }
</style>

<script>
    function toggleAccessibilityPanel() {
        const panel = document.getElementById('accSidePanel');
        const overlay = document.getElementById('accSidePanelOverlay');
        if (panel.style.right === '0px') {
            panel.style.right = '-450px';
            overlay.style.opacity = '0';
            overlay.style.pointerEvents = 'none';
            document.body.style.overflow = ''; // Unlock scroll
        } else {
            panel.style.right = '0px';
            overlay.style.opacity = '1';
            overlay.style.pointerEvents = 'auto';
            document.body.style.overflow = 'hidden'; // Lock scroll to prevent background scrolling
        }
    }

    let currentZoom = 1;
    function changeFontSize(direction) {
        if (direction === 0) {
            currentZoom = 1;
        } else {
            currentZoom += direction * 0.1;
        }
        currentZoom = Math.max(0.8, Math.min(currentZoom, 1.5));
        document.body.style.zoom = currentZoom;
    }

    function setColorScheme(scheme, btnElement) {
        document.body.classList.remove('dark-mode', 'high-contrast');
        document.querySelectorAll('.scheme-btn').forEach(b => {
            b.classList.remove('active');
            b.style.background = 'transparent';
            b.style.color = '#666';
            b.style.boxShadow = 'none';
        });
        
        btnElement.classList.add('active');
        btnElement.style.background = '#fff';
        btnElement.style.color = 'var(--navy)';
        btnElement.style.boxShadow = '0 2px 5px rgba(0,0,0,0.05)';

        if (scheme === 'dark') {
            document.body.classList.add('dark-mode');
        } else if (scheme === 'contrast') {
            document.body.classList.add('high-contrast');
        }
        localStorage.setItem('ki_acc_scheme', scheme);
    }

    function toggleAccClass(className, inputElement) {
        if (inputElement.checked) {
            document.body.classList.add(className);
        } else {
            document.body.classList.remove(className);
        }
        
        // Save preferences
        const activeClasses = [];
        document.querySelectorAll('.ios-toggle input:checked').forEach(inp => {
            const attr = inp.getAttribute('onchange');
            const match = attr.match(/'([^']+)'/);
            if(match) activeClasses.push(match[1]);
        });
        localStorage.setItem('ki_acc_prefs', JSON.stringify(activeClasses));
    }
    
    function resetAllAccessibility() {
        changeFontSize(0);
        document.body.classList.remove('dyslexia-font', 'big-cursor', 'highlight-links', 'high-spacing', 'dark-mode', 'high-contrast', 'no-animations');
        document.querySelectorAll('.ios-toggle input').forEach(inp => inp.checked = false);
        
        const lightBtn = document.querySelector('.scheme-btn[onclick*="light"]');
        if(lightBtn) setColorScheme('light', lightBtn);

        localStorage.removeItem('ki_acc_prefs');
        localStorage.removeItem('ki_acc_scheme');
    }
    
    // Load preferences
    document.addEventListener('DOMContentLoaded', () => {
        const saved = localStorage.getItem('ki_acc_prefs');
        if(saved) {
            try {
                const classes = JSON.parse(saved);
                classes.forEach(c => {
                    document.body.classList.add(c);
                    const inp = document.querySelector(`.ios-toggle input[onchange*="${c}"]`);
                    if(inp) inp.checked = true;
                });
            } catch(e){}
        }
        
        const savedScheme = localStorage.getItem('ki_acc_scheme');
        if (savedScheme) {
            const btn = document.querySelector(`.scheme-btn[onclick*="${savedScheme}"]`);
            if (btn) setColorScheme(savedScheme, btn);
        }
    });
</script>
<style>
    /* Accessibility Classes applied to Body */
    body.dyslexia-font, body.dyslexia-font * {
        font-family: 'Comic Sans MS', 'OpenDyslexic', sans-serif !important;
    }
    body.big-cursor, body.big-cursor *, body.big-cursor a, body.big-cursor button {
        cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 32 32"><path d="M2 2 L12 30 L16 18 L28 14 Z" fill="black" stroke="white" stroke-width="2"/></svg>') 2 2, auto !important;
    }
    body.highlight-links a, body.highlight-links button, body.highlight-links .btn {
        text-decoration: underline !important;
        text-decoration-color: var(--gold) !important;
        text-decoration-thickness: 4px !important;
        background-color: rgba(201,162,88,0.1) !important;
        color: #000 !important;
    }
    body.high-spacing * {
        letter-spacing: 0.12em !important;
        word-spacing: 0.16em !important;
        line-height: 1.8 !important;
    }
    
    /* Dark Mode (Elegant Dark) */
    body.dark-mode {
        background: #121212 !important;
    }
    body.dark-mode, body.dark-mode p, body.dark-mode span, body.dark-mode div, body.dark-mode li {
        color: #e0e0e0 !important;
    }
    body.dark-mode h1, body.dark-mode h2, body.dark-mode h3, body.dark-mode h4, body.dark-mode h5, body.dark-mode h6, body.dark-mode strong {
        color: #ffffff !important;
    }
    body.dark-mode section, body.dark-mode header, body.dark-mode footer, body.dark-mode .course-card {
        background-color: #1a1a1a !important;
        border-color: #333 !important;
    }
    body.dark-mode div[style*="background: #fff"], body.dark-mode div[style*="background: #fdfbf7"] {
        background-color: #1a1a1a !important;
        border-color: #333 !important;
    }
    body.dark-mode a:not(.btn) {
        color: var(--gold) !important;
    }
    body.dark-mode #accSidePanel, body.dark-mode .acc-panel-scrollable, body.dark-mode .acc-section-header {
        background: #1e1e1e !important;
        color: #fff !important;
    }
    body.dark-mode .acc-section-box {
        background: #2a2a2a !important;
        border-color: #444 !important;
    }
    body.dark-mode .acc-toggle-row, body.dark-mode .custom-select-wrapper select {
        background: #2a2a2a !important;
        border-color: #444 !important;
        color: #fff !important;
    }
    body.dark-mode .acc-toggle-title {
        color: #fff !important;
    }
    body.dark-mode .scheme-btn {
        color: #fff !important;
    }
    body.dark-mode .scheme-btn.active {
        background: rgba(201,162,88,0.2) !important;
        color: var(--gold) !important;
    }
    
    /* High Contrast Mode (Maximum Legibility) */
    body.high-contrast {
        background: #000 !important;
    }
    body.high-contrast, body.high-contrast * {
        background-color: #000 !important;
        color: #fff !important;
        border-color: #fff !important;
    }
    body.high-contrast a, body.high-contrast a *, body.high-contrast button, body.high-contrast button * {
        color: #ffff00 !important;
        border-color: #ffff00 !important;
    }
    body.high-contrast img, body.high-contrast svg {
        background-color: transparent !important;
    }
    body.high-contrast #accSidePanel {
        background: #000 !important;
        border-left: 2px solid #fff !important;
    }
    
    body.no-animations * {
        transition: none !important;
        animation: none !important;
        scroll-behavior: auto !important;
    }
    #floatingCookieBtn:hover, #accessibilityBtn:hover {
        transform: scale(1.1);
    }
</style>
<script>
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
</script>
</body>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected v5
    if 'class="acc-section-box"' in content:
        continue

    # Clean out the v4 widget if it exists
    if '<!-- Accessibility Widget Trigger -->' in content:
        import re
        content = re.sub(r'<!-- Floating Cookie Button -->.*?</body>', '</body>', content, flags=re.DOTALL)

    # Only inject into files that have a closing body tag
    if '</body>' in content:
        content = content.replace('</body>', injection_code)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected v5 widgets into {file}")

