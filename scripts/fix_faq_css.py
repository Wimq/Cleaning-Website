import os
import re

old_css = """        .faq-trigger {
            width: 100%;
            padding: 2rem;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 1rem;
            background: none;
            border: none;
            cursor: pointer;
            text-align: left;
            font-family: var(--ff-head);
            font-size: 1.4rem;
            color: var(--navy);
            font-weight: 700;
            transition: var(--ease);
        }"""

new_css = """        .faq-trigger {
            width: 100%;
            padding: 1.25rem 1.5rem;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 1rem;
            background: none;
            border: none;
            cursor: pointer;
            text-align: left;
            font-family: var(--ff-body);
            font-size: 1.05rem;
            line-height: 1.4;
            color: var(--navy);
            font-weight: 600;
            transition: var(--ease);
        }"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need a robust regex replacement since whitespace might vary slightly
    
    # First, let's just do a string replacement for the exact old CSS if it exists
    new_content = content.replace(old_css, new_css)
    
    # Also handle the cases where padding was 1.25rem 2rem (the intermediate fix)
    intermediate_css_1 = """        .faq-trigger {
            width: 100%;
            padding: 1.25rem 2rem;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 1rem;
            background: none;
            border: none;
            cursor: pointer;
            text-align: left;
            font-family: var(--ff-head);
            font-size: 1.2rem;
            line-height: 1.2;
            color: var(--navy);
            font-weight: 700;
            transition: var(--ease);
        }"""
    
    new_content = new_content.replace(intermediate_css_1, new_css)
    
    # And the span hacks
    old_span_hack = """        .faq-trigger span {
            flex: 1;
            padding-left: 0.5rem;
            display: flex;
            align-items: center;
            margin-top: 2px; /* Micro-adjustment for the heading font baseline */
        }"""
    
    new_span = """        .faq-trigger span {
            flex: 1;
            padding-left: 0.5rem;
        }"""
    
    new_content = new_content.replace(old_span_hack, new_span)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.py'):
            if file == 'fix_faq_css.py': continue
            process_file(os.path.join(root, file))

print("Done")
