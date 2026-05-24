import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

script_tag = "\n<script>\n    document.querySelectorAll('.dynamic-year').forEach(el => el.textContent = new Date().getFullYear());\n</script>\n"

for filepath in html_files:
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'dynamic-year' not in content and '&copy; 2026' in content:
            content = content.replace('&copy; 2026', '&copy; <span class="dynamic-year">2026</span>')
            
            # Ensure we only append the script tag once before </body>
            if '</body>' in content:
                content = content.replace('</body>', script_tag + '</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Dynamic year injected successfully.")
