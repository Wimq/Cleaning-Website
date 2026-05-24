import os
import glob
import re

css_replacements = {
    '.faq-trigger {\n            width: 100%;\n            padding: 1.25rem 1.5rem;\n            display: flex;\n            justify-content: flex-start;\n            align-items: center;\n            gap: 1rem;': 
    '.faq-trigger {\n            width: 100%;\n            padding: 1.25rem 1.5rem;\n            display: flex;\n            justify-content: space-between;\n            align-items: center;\n            gap: 0;',

    '.faq-trigger::before {\n            counter-increment: faq-counter;\n            content: "Q" counter(faq-counter);\n            background: rgba(201,162,88,0.1);\n            color: var(--gold);\n            padding: 0.4rem 0.8rem;\n            border-radius: 8px;\n            font-size: 0.9rem;\n            font-family: var(--ff-body);\n            font-weight: 800;\n        }':
    '.faq-trigger::before {\n            counter-increment: faq-counter;\n            content: "Q" counter(faq-counter);\n            background: rgba(201,162,88,0.1);\n            color: var(--gold);\n            padding: 0.4rem 0;\n            border-radius: 8px;\n            font-size: 0.9rem;\n            font-family: var(--ff-body);\n            font-weight: 800;\n            flex: 0 0 50px;\n            text-align: center;\n            display: flex;\n            justify-content: center;\n            align-items: center;\n        }',

    '.faq-trigger span {\n            flex: 1;\n            padding: 0 1rem;\n            text-align: center;\n        }':
    '.faq-trigger span {\n            flex-grow: 1;\n            text-align: left;\n            margin-left: 1.5rem;\n            padding: 0;\n        }'
}

def update_files():
    faq_files = glob.glob('pages/faq/faq-*.html')
    for filepath in faq_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for old, new in css_replacements.items():
            content = content.replace(old, new)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

if __name__ == '__main__':
    update_files()
    print("Done applying new layout.")
