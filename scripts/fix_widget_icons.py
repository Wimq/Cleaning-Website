import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # We need to make sure lucide.createIcons() is called for the newly injected widgets.
    # The widgets were injected right before </body>.
    # We can inject a small script right before </body> if it's not already there.
    
    fix_script = """<script>
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
</script>
</body>"""

    # If the file has the widgets but not the fix script
    if 'id="accessibilityBtn"' in content and 'lucide.createIcons();\n    }\n</script>\n</body>' not in content:
        content = content.replace('</body>', fix_script)
        
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed icons in {file}")
