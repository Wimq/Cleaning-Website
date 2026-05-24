import os
import glob
import re

seo_tags = """    <!-- SEO & Open Graph -->
    <link rel="canonical" href="https://www.kensingtonivy.co.uk/">
    <meta property="og:title" content="Kensington Ivy | Elite University Placement">
    <meta property="og:description" content="UK's premier university admissions consultancy. We match students with their courses of choice and secure placements at leading institutions.">
    <meta property="og:url" content="https://www.kensingtonivy.co.uk/">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://www.kensingtonivy.co.uk/assets/og-image.jpg">
"""

def add_seo_to_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if "<!-- SEO & Open Graph -->" in content:
        return
        
    # Inject before </head>
    if "</head>" in content:
        new_content = content.replace("</head>", seo_tags + "</head>")
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Injected SEO tags into {filepath}")

targets = [
    'index.html',
    'pages/find-courses.html',
    'pages/registries.html',
    'pages/about.html',
    'pages/hire-staff.html'
]

for t in targets:
    if os.path.exists(t):
        add_seo_to_file(t)
