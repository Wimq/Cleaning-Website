import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

injection_code = """
<!-- Floating Cookie Button -->
<button id="floatingCookieBtn" onclick="document.getElementById('cookieBanner').classList.add('visible');" style="position: fixed; bottom: 20px; left: 20px; z-index: 9998; background: var(--navy); color: #fff; width: 50px; height: 50px; border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; border: 2px solid rgba(255,255,255,0.1); cursor: pointer; transition: all 0.3s ease;">
    <i data-lucide="cookie" style="width: 24px; height: 24px;"></i>
</button>

<!-- Accessibility Widget -->
<button id="accessibilityBtn" onclick="toggleAccessibilityModal()" style="position: fixed; bottom: 20px; right: 20px; z-index: 9998; background: var(--gold); color: var(--navy); width: 60px; height: 60px; border-radius: 50%; box-shadow: 0 10px 25px rgba(201,162,88,0.4); display: flex; align-items: center; justify-content: center; border: none; cursor: pointer; transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
    <i data-lucide="accessibility" style="width: 32px; height: 32px;"></i>
</button>

<!-- Glassmorphic Accessibility Modal -->
<div id="accessibilityModal" style="position: fixed; bottom: 90px; right: 20px; width: 350px; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.4); box-shadow: 0 20px 50px rgba(10,17,40,0.2); border-radius: 20px; z-index: 9999; padding: 2rem; transform: translateY(20px); opacity: 0; pointer-events: none; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
    <h3 style="font-family: var(--ff-head); color: var(--navy); font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;"><i data-lucide="settings-2" style="color: var(--gold);"></i> Accessibility</h3>
    
    <!-- Language Translate -->
    <div style="margin-bottom: 2rem;">
        <label style="display: block; font-size: 0.9rem; font-weight: 600; color: #555; margin-bottom: 0.5rem;">Translate Page (133 Languages)</label>
        <div class="gtranslate_wrapper"></div>
    </div>

    <!-- Text Size -->
    <div style="margin-bottom: 2rem;">
        <label style="display: block; font-size: 0.9rem; font-weight: 600; color: #555; margin-bottom: 0.5rem;">Text Size</label>
        <div style="display: flex; gap: 1rem;">
            <button onclick="changeFontSize(-1)" style="flex: 1; padding: 0.5rem; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 1rem; color: #333; font-weight: 600;">A-</button>
            <button onclick="changeFontSize(0)" style="flex: 1; padding: 0.5rem; border-radius: 8px; border: 1px solid #ddd; background: #fdfbf7; cursor: pointer; font-size: 1rem; color: #333; font-weight: 600;">Reset</button>
            <button onclick="changeFontSize(1)" style="flex: 1; padding: 0.5rem; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 1.2rem; color: #333; font-weight: 600;">A+</button>
        </div>
    </div>

    <!-- High Contrast -->
    <div>
        <label style="display: block; font-size: 0.9rem; font-weight: 600; color: #555; margin-bottom: 0.5rem;">High Contrast</label>
        <button onclick="toggleContrast()" id="contrastBtn" style="width: 100%; padding: 0.8rem; border-radius: 8px; border: none; background: var(--navy); color: #fff; cursor: pointer; font-weight: 600; transition: background 0.3s ease;">Enable High Contrast</button>
    </div>
</div>

<script>
    window.gtranslateSettings = {
        "default_language": "en",
        "native_language_names": true,
        "wrapper_selector": ".gtranslate_wrapper",
        "flag_style": "3d"
    };
</script>
<script src="https://cdn.gtranslate.net/widgets/latest/dropdown.js" defer></script>

<script>
    function toggleAccessibilityModal() {
        const modal = document.getElementById('accessibilityModal');
        const btn = document.getElementById('accessibilityBtn');
        if (modal.style.opacity === '0' || modal.style.opacity === '') {
            modal.style.opacity = '1';
            modal.style.pointerEvents = 'auto';
            modal.style.transform = 'translateY(0)';
            btn.style.transform = 'rotate(45deg) scale(1.1)';
        } else {
            modal.style.opacity = '0';
            modal.style.pointerEvents = 'none';
            modal.style.transform = 'translateY(20px)';
            btn.style.transform = 'rotate(0) scale(1)';
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

    function toggleContrast() {
        document.body.classList.toggle('high-contrast');
        const btn = document.getElementById('contrastBtn');
        if (document.body.classList.contains('high-contrast')) {
            btn.textContent = 'Disable High Contrast';
            btn.style.background = '#000';
            btn.style.color = '#fff';
            btn.style.border = '1px solid #fff';
        } else {
            btn.textContent = 'Enable High Contrast';
            btn.style.background = 'var(--navy)';
            btn.style.border = 'none';
        }
    }
</script>
<style>
    body.high-contrast {
        background: #000 !important;
        color: #fff !important;
        filter: contrast(120%) !important;
    }
    body.high-contrast * {
        color: #fff !important;
        border-color: #fff !important;
    }
    body.high-contrast .btn-gold {
        background: #fff !important;
        color: #000 !important;
    }
    body.high-contrast #accessibilityModal {
        background: #000 !important;
        border: 2px solid #fff !important;
    }
    #floatingCookieBtn:hover {
        background: var(--gold) !important;
        color: var(--navy) !important;
        border-color: var(--gold) !important;
        transform: scale(1.1);
    }
</style>
</body>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected
    if 'id="accessibilityBtn"' in content:
        continue

    # Only inject into files that have a closing body tag
    if '</body>' in content:
        # Before we inject, make sure we only inject once
        content = content.replace('</body>', injection_code)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected widgets into {file}")

