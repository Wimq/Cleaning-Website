import os

course_data = {
    "medicine": {
        "title": "Medicine (MBBS & MBChB)",
        "meta_desc": "Secure your place on a Medicine degree at a leading UK medical school.",
        "duration": "5-6 Years",
        "offer": "AAA (incl. Chemistry & Biology)",
        "ucat": "Required",
        "overview": "Medicine remains one of the most competitive degree programs in the United Kingdom. With strict quotas for international students and extremely high grade and aptitude thresholds for all applicants, obtaining an offer requires careful strategy, dedication, and clinical precision. At Kensington Ivy, our admissions specialists include qualified doctors and medical school graduates. We have successfully guided applicants to top-ranked UK medical schools, helping them stand out from thousands of candidates.",
        "modules": [
            "Anatomy and Physiology",
            "Pathology and Disease",
            "Clinical Pharmacology",
            "Medical Ethics and Law",
            "Primary Care and General Practice",
            "Surgery and Anesthetics"
        ],
        "career": "Graduates enter the Foundation Programme (FY1 & FY2) to become fully registered medical practitioners. Opportunities range from General Practice to highly specialized fields such as Neurosurgery, Cardiology, and Pediatrics."
    },
    "law": {
        "title": "Law (LLB & LLM)",
        "meta_desc": "Study Law at a top-tier UK university. Expert admissions support for LLB programs.",
        "duration": "3 Years (LLB)",
        "offer": "A*AA - AAA",
        "ucat": "LNAT Required (for top tiers)",
        "overview": "A Law degree from a UK university is globally respected, providing a rigorous intellectual foundation in analytical thinking, argumentation, and legal principles. Whether you intend to practice as a solicitor or barrister, or use your legal training in corporate finance, politics, or international relations, securing a place at a top-tier institution is highly competitive.",
        "modules": [
            "Criminal Law",
            "Contract Law",
            "Constitutional & Administrative Law",
            "Tort Law",
            "Property & Land Law",
            "Equity & Trusts"
        ],
        "career": "Most graduates progress to the LPC (Legal Practice Course) or SQE (Solicitors Qualifying Examination) to become solicitors, or the BPTC to become barristers. Others enter investment banking, management consulting, or the civil service."
    },
    "engineering": {
        "title": "Engineering (BEng & MEng)",
        "meta_desc": "Engineering placement across Civil, Mechanical, and Aerospace disciplines.",
        "duration": "3-4 Years",
        "offer": "A*AA (incl. Maths & Physics)",
        "ucat": "Not Required",
        "overview": "Engineering drives global innovation. From designing sustainable infrastructure and advanced robotics to aerospace exploration and renewable energy systems, a UK engineering degree equips you with world-class technical and problem-solving skills. Universities look for exceptional mathematical ability and a genuine passion for understanding how the physical world works.",
        "modules": [
            "Engineering Mathematics",
            "Thermodynamics and Fluid Mechanics",
            "Structural Analysis",
            "Materials Science",
            "Control Systems & Robotics",
            "Computer-Aided Design (CAD)"
        ],
        "career": "Engineers are in exceptionally high demand globally. Graduates work in aerospace, automotive, civil infrastructure, tech, and renewable energy sectors, often securing high-paying graduate roles immediately upon completion."
    },
    "computer-science": {
        "title": "Computer Science (BSc & MSci)",
        "meta_desc": "Computer Science placement for top UK universities. Master software and AI.",
        "duration": "3-4 Years",
        "offer": "A*A*A (incl. Maths/Further Maths)",
        "ucat": "TMUA/STEP (for top tiers)",
        "overview": "Computer Science is the fastest-growing and most dynamic field in the modern economy. A degree in this discipline goes far beyond programming—it encompasses artificial intelligence, machine learning, cryptography, algorithmic theory, and complex systems architecture. Admissions tutors look for exceptional logical reasoning and mathematical prowess.",
        "modules": [
            "Algorithms and Data Structures",
            "Object-Oriented Programming",
            "Artificial Intelligence & Machine Learning",
            "Computer Architecture & Operating Systems",
            "Cybersecurity & Cryptography",
            "Software Engineering"
        ],
        "career": "Graduates are heavily recruited by FAANG companies (Facebook, Amazon, Apple, Netflix, Google), financial tech firms, and hedge funds for roles as Software Engineers, Data Scientists, and Security Analysts."
    },
    "business-management": {
        "title": "Business & Management (BSc & BA)",
        "meta_desc": "Business Management placement. Learn global enterprise strategy and finance.",
        "duration": "3 Years",
        "offer": "AAA - AAB",
        "ucat": "Not Required",
        "overview": "Business Management provides a comprehensive understanding of how organizations operate, grow, and adapt in a globalized economy. You will study a blend of economics, finance, human resources, and marketing. Top UK business schools offer unparalleled networking opportunities and often include a year in industry to build your corporate CV before you even graduate.",
        "modules": [
            "Micro & Macro Economics",
            "Financial & Management Accounting",
            "Organizational Behavior",
            "Marketing Strategy",
            "Corporate Finance",
            "International Business Law"
        ],
        "career": "Business graduates enter prestigious graduate schemes in management consulting (MBB), investment banking, accounting (Big 4), fast-moving consumer goods (FMCG), and tech management."
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} University Placement | KensingtonIvy</title>
    <meta name="description" content="{meta}">
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/layout.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .course-hero {{
            background: var(--navy);
            color: #fff;
            padding: 8rem 0 5rem 0;
            position: relative;
        }}
        .course-hero-content {{
            max-width: 800px;
        }}
        .course-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255,255,255,0.1);
            padding: 0.5rem 1rem;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-right: 1rem;
            margin-bottom: 1rem;
        }}
        .course-body {{
            padding: 5rem 0;
            background: var(--off);
        }}
        .course-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 4rem;
        }}
        @media (max-width: 900px) {{
            .course-grid {{
                grid-template-columns: 1fr;
            }}
        }}
        .content-section {{
            background: #fff;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            margin-bottom: 2rem;
        }}
        .content-section h2 {{
            color: var(--navy);
            font-family: var(--ff-head);
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }}
        .content-section p {{
            color: #555;
            line-height: 1.7;
            margin-bottom: 1.5rem;
            font-size: 1.05rem;
        }}
        .module-list {{
            list-style: none;
            padding: 0;
        }}
        .module-list li {{
            padding: 1rem;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
            gap: 1rem;
            color: #444;
            font-weight: 500;
        }}
        .module-list li i {{
            color: var(--gold);
        }}
        .sticky-card {{
            position: sticky;
            top: 2rem;
            background: #fff;
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.06);
            border-top: 4px solid var(--gold);
        }}
        .sticky-card h3 {{
            font-family: var(--ff-head);
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--navy);
        }}
        .stat-row {{
            display: flex;
            justify-content: space-between;
            padding: 1rem 0;
            border-bottom: 1px solid #eee;
            font-size: 0.95rem;
        }}
        .stat-label {{
            color: #666;
        }}
        .stat-val {{
            font-weight: 600;
            color: var(--navy);
        }}
    </style>
</head>
<body>
<header class="header">
    <div class="container header-inner">
        <a href="../../index.html" class="logo"><span class="logo-text">Kensington</span><span class="logo-accent">Ivy</span></a>
        <nav class="top-links" style="gap: 2rem;">
            <a href="../find-courses.html" style="color: var(--navy); font-weight: 500;">Find Courses</a>
            <a href="../faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../about.html" style="color: var(--navy); font-weight: 500;">About Us</a>
        </nav>
        <div style="display: flex; gap: 1rem; align-items: center;">
            <a href="../register.html?course={url_enc}" class="btn btn-gold" style="gap: 0.5rem;">Get My Place <i data-lucide="arrow-right" style="width:15px;height:15px;"></i></a>
            <button class="menu-toggle" onclick="document.querySelector('.top-links').classList.toggle('active')" aria-label="Toggle Menu">
                <i data-lucide="menu"></i>
            </button>
        </div>
    </div>
</header>

<section class="course-hero">
    <div class="container">
        <a href="../find-courses.html" style="color: var(--gold); text-decoration: none; font-weight: 600; font-size: 0.9rem; margin-bottom: 1.5rem; display: inline-block;">&larr; Back to Course Search</a>
        <div class="course-hero-content">
            <h1 style="font-family: var(--ff-head); font-size: 4rem; line-height: 1.1; margin-bottom: 2rem;">{title}</h1>
            <div>
                <span class="course-badge"><i data-lucide="clock" style="width:16px;"></i> {duration}</span>
                <span class="course-badge"><i data-lucide="award" style="width:16px;"></i> Typical Offer: {offer}</span>
                <span class="course-badge"><i data-lucide="file-text" style="width:16px;"></i> Admissions Test: {ucat}</span>
            </div>
        </div>
    </div>
</section>

<section class="course-body">
    <div class="container">
        <div class="course-grid">
            <div class="course-main">
                <div class="content-section">
                    <h2>Course Overview</h2>
                    <p>{overview}</p>
                </div>
                
                <div style="background: rgba(201, 162, 88, 0.1); border-left: 4px solid var(--gold); padding: 1.5rem 2rem; border-radius: 8px; margin-bottom: 2rem;">
                    <h4 style="color: var(--navy); margin-bottom: 0.5rem; font-family: var(--ff-head); font-size: 1.2rem;">Not Meeting the Grades?</h4>
                    <p style="margin: 0; color: #444; font-size: 0.95rem; line-height: 1.6;">Kensington Ivy holds exclusive partnerships with several institutions, allowing us to secure placements for students who may not meet standard entry thresholds. <a href="../register.html?course={url_enc}" style="color: var(--gold); font-weight: 600; text-decoration: underline;">Contact us</a> to see if you are eligible with your current qualifications.</p>
                </div>
                
                <div class="content-section">
                    <h2>Core Modules & Structure</h2>
                    <p>While exact module structures vary between leading UK universities, a rigorous degree in {title} will typically cover the following core areas in your first two years:</p>
                    <ul class="module-list">
                        {modules_html}
                    </ul>
                </div>
                
                <div class="content-section">
                    <h2>Graduate Prospects & Careers</h2>
                    <p>{career}</p>
                </div>
            </div>
            
            <div class="course-sidebar">
                <div class="sticky-card">
                    <h3>Ready to Apply?</h3>
                    <p style="color: #555; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Secure your place at a top-tier UK university. Our admissions consultants are ready to review your academic profile.</p>
                    
                    <div class="stat-row">
                        <span class="stat-label">Intake</span>
                        <span class="stat-val">September 2026</span>
                    </div>
                    <div class="stat-row">
                        <span class="stat-label">Study Mode</span>
                        <span class="stat-val">Full-Time</span>
                    </div>
                    <div class="stat-row" style="margin-bottom: 2rem;">
                        <span class="stat-label">Location</span>
                        <span class="stat-val">UK Nationwide</span>
                    </div>
                    
                    <a href="../register.html?course={url_enc}" class="btn" style="background: var(--navy); color: #fff; width: 100%; justify-content: center;">Enquire Now</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FOOTER -->
<footer style="background: var(--navy); padding: 7rem 0 4rem 0; color: #fff; border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 4rem;">
            
            <div style="grid-column: span 1;">
                <a href="../../index.html" class="logo" style="display: block; margin-bottom: 1.5rem;">
                    <span style="font-family: var(--ff-head); font-weight: 800; font-size: 1.8rem; color: #fff;">Kensington</span><span style="font-family: var(--ff-head); font-weight: 800; font-size: 1.8rem; color: var(--gold);">Ivy</span>
                </a>
                <p style="color: rgba(255,255,255,0.6); font-size: 0.95rem; line-height: 1.6; max-width: 320px;">UK's trusted university placement and admissions partner. Built on academic excellence, we help students secure places in their chosen courses across the country.</p>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.3rem; margin-bottom: 2rem; color: #fff;">Menu</h4>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <a href="../../index.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Home</a>
                    <a href="../about.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">About Us</a>
                    <a href="../faq/faq.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">University Registries</a>
                    <a href="../hire-staff.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Request Placement</a>
                </div>
            </div>

            <div>
                <h4 style="font-family: var(--ff-head); font-size: 1.3rem; margin-bottom: 2rem; color: #fff;">Legal</h4>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <a href="../legal/privacy.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Privacy Policy</a>
                    <a href="../legal/terms.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Website Terms</a>
                    <a href="../legal/cookies.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Cookie Policy</a>
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

        <div style="margin-top: 5rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: flex-end; color: rgba(255,255,255,0.5); font-size: 0.85rem;">
            <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                <p>Kensington Ivy LTD is a company registered in England and Wales (Company No. 17167406) | ICO Registration No. ZC148985.</p>
                <p>&copy; <span class="dynamic-year">2026</span> Kensington Ivy LTD. All rights reserved.</p>
            </div>
            
            <div style="opacity: 0.6; transition: var(--ease);">
                <a href="//www.dmca.com/Protection/Status.aspx?ID=f3d4db82-c26d-44f0-87c5-10d923a53d0b" title="DMCA.com Protection Status" class="dmca-badge"> 
                    <img src="https://images.dmca.com/Badges/dmca_protected_sml_120n.png?ID=f3d4db82-c26d-44f0-87c5-10d923a53d0b" alt="DMCA.com Protection Status" style="display: block;" />
                </a>
            </div>
        </div>
    </div>
</footer>
<script>lucide.createIcons();</script>
<script>document.querySelectorAll('.dynamic-year').forEach(el => el.textContent = new Date().getFullYear());</script>
</body>
</html>
"""

import urllib.parse

for key, data in course_data.items():
    mods_html = "\n".join([f'<li><i data-lucide="check-circle"></i> {m}</li>' for m in data["modules"]])
    
    html = template.format(
        title=data["title"],
        meta=data["meta_desc"],
        duration=data["duration"],
        offer=data["offer"],
        ucat=data["ucat"],
        overview=data["overview"],
        modules_html=mods_html,
        career=data["career"],
        url_enc=urllib.parse.quote(data["title"])
    )
    
    fpath = f"pages/courses/{key}.html"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Rebuilt {fpath}")

print("All course pages successfully redesigned.")
