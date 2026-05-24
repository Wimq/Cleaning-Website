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
<div id="accSidePanelOverlay" onclick="toggleAccessibilityPanel()" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.5); z-index: 9999; opacity: 0; pointer-events: none; transition: opacity 0.3s ease; backdrop-filter: blur(4px);"></div>
<div id="accSidePanel" style="position: fixed; top: 0; right: -450px; width: 400px; max-width: 100vw; height: 100vh; background: #fff; box-shadow: -10px 0 30px rgba(0,0,0,0.2); z-index: 10000; transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1); display: flex; flex-direction: column;">
    <div style="padding: 1.5rem 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center; background: var(--navy); color: #fff;">
        <h3 style="margin: 0; font-size: 1.3rem; display: flex; align-items: center; gap: 0.75rem; font-family: var(--ff-head);"><i data-lucide="accessibility" style="color: var(--gold);"></i> Accessibility Suite</h3>
        <button onclick="toggleAccessibilityPanel()" style="background: rgba(255,255,255,0.1); border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border: none; color: #fff; cursor: pointer; transition: background 0.3s ease;"><i data-lucide="x" style="width: 18px;"></i></button>
    </div>
    
    <div style="flex: 1; overflow-y: auto; padding: 2rem; background: #faf9f6;" class="acc-panel-scrollable">
        
        <!-- Translate -->
        <div class="acc-section" style="margin-bottom: 2rem; background: #fff; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); border: 1px solid #eee;">
            <label style="display: block; font-weight: 600; color: var(--navy); margin-bottom: 1rem; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px;"><i data-lucide="globe-2" style="width: 16px; display: inline-block; vertical-align: middle; margin-right: 6px; color: var(--gold);"></i> Translate Page</label>
            <!-- Custom Styled Wrapper for GTranslate -->
            <div class="gtranslate_styled_container">
                <div class="gtranslate_wrapper"></div>
            </div>
        </div>
        
        <!-- Color Scheme -->
        <div class="acc-section" style="margin-bottom: 2rem; background: #fff; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); border: 1px solid #eee;">
            <label style="display: block; font-weight: 600; color: var(--navy); margin-bottom: 1rem; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px;"><i data-lucide="palette" style="width: 16px; display: inline-block; vertical-align: middle; margin-right: 6px; color: var(--gold);"></i> Color Scheme</label>
            <div style="display: flex; gap: 0.5rem;">
                <button class="scheme-btn active" onclick="setColorScheme('light', this)" style="flex: 1; padding: 0.75rem 0.5rem; border-radius: 8px; border: 1px solid var(--navy); background: rgba(10,17,40,0.05); cursor: pointer; font-size: 0.9rem; color: var(--navy); font-weight: 600; transition: all 0.2s;"><i data-lucide="sun" style="width: 18px; margin-bottom: 4px; display: block; margin: 0 auto 4px auto;"></i> Light</button>
                <button class="scheme-btn" onclick="setColorScheme('dark', this)" style="flex: 1; padding: 0.75rem 0.5rem; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 0.9rem; color: var(--navy); font-weight: 600; transition: all 0.2s;"><i data-lucide="moon" style="width: 18px; margin-bottom: 4px; display: block; margin: 0 auto 4px auto;"></i> Dark</button>
                <button class="scheme-btn" onclick="setColorScheme('contrast', this)" style="flex: 1; padding: 0.75rem 0.5rem; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 0.9rem; color: var(--navy); font-weight: 600; transition: all 0.2s;"><i data-lucide="contrast" style="width: 18px; margin-bottom: 4px; display: block; margin: 0 auto 4px auto;"></i> Contrast</button>
            </div>
        </div>

        <!-- Text Size -->
        <div class="acc-section" style="margin-bottom: 2rem; background: #fff; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); border: 1px solid #eee;">
            <label style="display: block; font-weight: 600; color: var(--navy); margin-bottom: 1rem; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px;"><i data-lucide="type" style="width: 16px; display: inline-block; vertical-align: middle; margin-right: 6px; color: var(--gold);"></i> Text Size</label>
            <div style="display: flex; gap: 1rem;">
                <button onclick="changeFontSize(-1)" style="flex: 1; padding: 0.75rem; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 1rem; color: var(--navy); font-weight: 600; transition: all 0.2s;">A-</button>
                <button onclick="changeFontSize(0)" style="flex: 1; padding: 0.75rem; border-radius: 8px; border: 1px solid var(--navy); background: rgba(10,17,40,0.05); cursor: pointer; font-size: 1rem; color: var(--navy); font-weight: 600; transition: all 0.2s;">Default</button>
                <button onclick="changeFontSize(1)" style="flex: 1; padding: 0.75rem; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 1.2rem; color: var(--navy); font-weight: 600; transition: all 0.2s;">A+</button>
            </div>
        </div>
        
        <label style="display: block; font-weight: 600; color: var(--navy); margin-bottom: 1rem; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px;"><i data-lucide="settings" style="width: 16px; display: inline-block; vertical-align: middle; margin-right: 6px; color: var(--gold);"></i> Viewing Tools</label>
        
        <!-- Toggles Grid -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 2rem;">
            <button class="acc-toggle" onclick="toggleAccClass('dyslexia-font', this)">
                <i data-lucide="book-open"></i> Dyslexia Font
            </button>
            <button class="acc-toggle" onclick="toggleAccClass('big-cursor', this)">
                <i data-lucide="mouse-pointer-2"></i> Big Cursor
            </button>
            <button class="acc-toggle" onclick="toggleAccClass('highlight-links', this)">
                <i data-lucide="link-2"></i> Highlight Links
            </button>
            <button class="acc-toggle" onclick="toggleAccClass('high-spacing', this)">
                <i data-lucide="space"></i> Letter Spacing
            </button>
            <button class="acc-toggle" onclick="toggleAccClass('no-animations', this)">
                <i data-lucide="play-circle"></i> Stop Animations
            </button>
        </div>
        
        <button onclick="resetAllAccessibility()" style="width: 100%; padding: 1rem; background: none; border: 1px dashed #ccc; color: #666; font-weight: 600; border-radius: 8px; cursor: pointer; margin-top: 1rem;"><i data-lucide="rotate-ccw" style="width: 16px; vertical-align: middle; margin-right: 6px;"></i> Reset All Settings</button>
    </div>
</div>

<script>
    window.gtranslateSettings = {
        "default_language": "en",
        "native_language_names": true,
        "wrapper_selector": ".gtranslate_wrapper",
        "flag_style": "2d" // simplified flags
    };
</script>
<!-- Using the modern flags style from GTranslate -->
<script src="https://cdn.gtranslate.net/widgets/latest/flags.js" defer></script>

<style>
    /* Premium Styling for GTranslate Flags */
    .gtranslate_styled_container {
        display: flex;
        justify-content: center;
        background: #fdfbf7;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    .gtranslate_wrapper a {
        display: inline-block;
        margin: 4px;
        border-radius: 4px;
        overflow: hidden;
        transition: transform 0.2s;
    }
    .gtranslate_wrapper a:hover {
        transform: scale(1.1);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
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
            b.style.background = '#fff';
            b.style.border = '1px solid #ddd';
        });
        
        btnElement.classList.add('active');
        btnElement.style.background = 'rgba(10,17,40,0.05)';
        btnElement.style.border = '1px solid var(--navy)';

        if (scheme === 'dark') {
            document.body.classList.add('dark-mode');
        } else if (scheme === 'contrast') {
            document.body.classList.add('high-contrast');
        }
        localStorage.setItem('ki_acc_scheme', scheme);
    }

    function toggleAccClass(className, btnElement) {
        document.body.classList.toggle(className);
        btnElement.classList.toggle('active');
        
        // Save preferences
        const activeClasses = [];
        document.querySelectorAll('.acc-toggle.active').forEach(b => {
            const attr = b.getAttribute('onclick');
            const match = attr.match(/'([^']+)'/);
            if(match) activeClasses.push(match[1]);
        });
        localStorage.setItem('ki_acc_prefs', JSON.stringify(activeClasses));
    }
    
    function resetAllAccessibility() {
        changeFontSize(0);
        document.body.classList.remove('dyslexia-font', 'big-cursor', 'highlight-links', 'high-spacing', 'dark-mode', 'high-contrast', 'no-animations');
        document.querySelectorAll('.acc-toggle').forEach(b => b.classList.remove('active'));
        
        const lightBtn = document.querySelector('.scheme-btn');
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
                    const btn = document.querySelector(`.acc-toggle[onclick*="${c}"]`);
                    if(btn) btn.classList.add('active');
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
    .acc-toggle {
        background: #fff;
        border: 1px solid #eee;
        padding: 1rem;
        border-radius: 12px;
        color: var(--navy);
        font-weight: 500;
        font-size: 0.9rem;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.75rem;
        transition: all 0.2s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.02);
    }
    .acc-toggle i {
        color: var(--gold);
        width: 24px;
        height: 24px;
        transition: transform 0.2s ease;
    }
    .acc-toggle:hover {
        border-color: var(--gold);
        transform: translateY(-2px);
    }
    .acc-toggle.active {
        background: var(--navy);
        border-color: var(--navy);
        color: #fff;
    }
    .acc-toggle.active i {
        color: #fff;
    }

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
        color: #e0e0e0 !important;
    }
    body.dark-mode section, body.dark-mode header, body.dark-mode footer, body.dark-mode .course-card {
        background-color: #121212 !important;
    }
    body.dark-mode div[style*="background: #fff"], body.dark-mode div[style*="background: #fdfbf7"] {
        background: #1e1e1e !important;
        border-color: #333 !important;
        color: #e0e0e0 !important;
    }
    body.dark-mode h1, body.dark-mode h2, body.dark-mode h3, body.dark-mode h4, body.dark-mode h5, body.dark-mode h6, body.dark-mode p {
        color: #e0e0e0 !important;
    }
    body.dark-mode .course-title, body.dark-mode .course-desc {
        color: #e0e0e0 !important;
    }
    body.dark-mode a {
        color: var(--gold) !important;
    }
    body.dark-mode #accSidePanel {
        background: #1e1e1e !important;
        color: #fff !important;
    }
    body.dark-mode .acc-panel-scrollable {
        background: #121212 !important;
    }
    body.dark-mode .acc-section, body.dark-mode .acc-toggle {
        background: #2a2a2a !important;
        border-color: #444 !important;
    }
    body.dark-mode .scheme-btn {
        background: #2a2a2a !important;
        border-color: #444 !important;
        color: #fff !important;
    }
    body.dark-mode .scheme-btn.active {
        background: rgba(201,162,88,0.2) !important;
        border-color: var(--gold) !important;
    }
    
    /* High Contrast Mode (Maximum Legibility) */
    body.high-contrast {
        background: #000 !important;
        color: #fff !important;
        filter: contrast(150%) !important;
    }
    body.high-contrast * {
        color: #fff !important;
        border-color: #fff !important;
    }
    body.high-contrast .btn-gold, body.high-contrast .btn-navy {
        background: #fff !important;
        color: #000 !important;
        border: 2px solid #000 !important;
    }
    body.high-contrast #accSidePanel {
        background: #000 !important;
        border-left: 2px solid #fff !important;
    }
    body.high-contrast .acc-section, body.high-contrast .acc-panel-scrollable {
        background: #000 !important;
        border-color: #fff !important;
    }
    body.high-contrast .acc-toggle, body.high-contrast .scheme-btn {
        background: #000 !important;
        border-color: #fff !important;
    }
    body.high-contrast .acc-toggle.active, body.high-contrast .scheme-btn.active {
        background: #fff !important;
        color: #000 !important;
    }
    body.high-contrast .acc-toggle.active i, body.high-contrast .scheme-btn.active i {
        color: #000 !important;
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

    # Skip if already injected v3
    if '<div id="accSidePanelOverlay"' in content and 'setColorScheme' in content:
        continue

    # Clean out the v2 widget if it exists
    if '<!-- Accessibility Widget Trigger -->' in content:
        import re
        content = re.sub(r'<!-- Floating Cookie Button -->.*?</body>', '</body>', content, flags=re.DOTALL)

    # Only inject into files that have a closing body tag
    if '</body>' in content:
        # Before we inject, make sure we only inject once
        content = content.replace('</body>', injection_code)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected v3 widgets into {file}")

