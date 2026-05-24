import json
import random

courses = [
    { "title": "Medicine (MBBS)", "category": "Healthcare", "url": "course-details.html?course=Medicine%20(MBBS)", "desc": "Train for a career as a doctor with extensive clinical placements and hands-on anatomy." },
    { "title": "Law (LLB)", "category": "Humanities", "url": "course-details.html?course=Law%20(LLB)", "desc": "Develop rigorous analytical skills and prepare for a legal career with mock trials." },
    { "title": "Computer Science", "category": "STEM", "url": "course-details.html?course=Computer%20Science", "desc": "Master software engineering, AI, algorithms, and complex systems architecture." },
    { "title": "Business Management", "category": "Business", "url": "course-details.html?course=Business%20Management", "desc": "Learn global enterprise strategy, finance, and leadership in modern organizations." },
    { "title": "Engineering (BEng/MEng)", "category": "STEM", "url": "course-details.html?course=Engineering%20(BEng%2FMEng)", "desc": "Design the future across civil, mechanical, electrical and aerospace fields." }
]

base_subjects = [
    # Social Sciences
    ("Psychology", "Social Sciences", "Explore the human mind and behavior through scientific methods, clinical research, and cognitive analysis."),
    ("Sociology", "Social Sciences", "Examine society, human behavior, social structures, inequality, and institutional change."),
    ("Criminology", "Social Sciences", "Understand crime, criminal justice systems, policing, and their societal impact."),
    ("Anthropology", "Social Sciences", "Study human origins, cultures, societal development, and cross-cultural diversity."),
    ("Geography", "Social Sciences", "Physical earth sciences combined with human environment studies and spatial analysis."),
    ("International Relations", "Social Sciences", "Analyze global diplomacy, conflict resolution, and foreign policy frameworks."),
    ("Social Policy", "Social Sciences", "Examine welfare systems, public health policy, and social inequality."),
    ("Politics and International Studies", "Social Sciences", "Study political systems, governance, and global institutions."),
    ("Forensic Psychology", "Social Sciences", "Apply psychological principles to criminal investigation and the legal system."),
    ("Child Psychology", "Social Sciences", "Study cognitive, emotional, and social development from infancy to adolescence."),

    # Humanities
    ("History", "Humanities", "Study human events, civilizations, and societal evolution across eras and continents."),
    ("English Literature", "Humanities", "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."),
    ("Politics", "Humanities", "Study global governance, diplomacy, elections, and political systems."),
    ("Philosophy", "Humanities", "Explore fundamental questions of existence, ethics, logic, and epistemology."),
    ("Theology", "Humanities", "Study world religions, beliefs, sacred texts, and theological ethics."),
    ("Classics", "Humanities", "Study the literature, history, and culture of ancient Greece and Rome."),
    ("Linguistics", "Humanities", "The scientific study of language structure, phonetics, syntax, and semantics."),
    ("Modern Languages", "Humanities", "Master foreign languages and study global cultures, translation, and diplomacy."),
    ("English Language", "Humanities", "Explore the structure, history, and sociolinguistics of the English language."),
    ("Creative Writing", "Humanities", "Develop fiction, poetry, screenwriting, and non-fiction storytelling skills."),
    ("American Studies", "Humanities", "Study American history, culture, politics, and literature."),
    ("Ancient History", "Humanities", "Explore the civilizations of the ancient world from Mesopotamia to Rome."),
    ("Archaeology", "Humanities", "Investigate past cultures through material remains and fieldwork excavation."),
    ("French", "Humanities", "Master French language, literature, cinema, and Francophone cultures."),
    ("Spanish", "Humanities", "Study the Spanish language, Latin American literature, and Hispanic cultures."),
    ("German", "Humanities", "Explore German language, literature, philosophy, and Central European culture."),
    ("Arabic", "Humanities", "Study Arabic language, Islamic civilizations, and Middle Eastern politics."),
    ("Chinese Studies", "Humanities", "Mandarin language proficiency combined with East Asian history and politics."),
    ("Japanese Studies", "Humanities", "Study Japanese language, culture, anime industries, and East Asian business."),

    # Business
    ("Accounting", "Business", "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."),
    ("Economics", "Business", "Analyze markets, monetary policy, econometrics, and global financial structures."),
    ("Marketing", "Business", "Consumer behavior, digital strategy, brand management, and market research."),
    ("Human Resource Management", "Business", "Manage talent, recruitment, organizational behavior, and employment law."),
    ("International Business", "Business", "Global trade, cross-border strategy, supply chain, and international markets."),
    ("Entrepreneurship", "Business", "Learn to ideate, build, launch, and scale startup ventures and SMEs."),
    ("Event Management", "Business", "Plan and execute large-scale corporate events, festivals, and conferences."),
    ("Real Estate", "Business", "Property valuation, investment analysis, urban planning, and development finance."),
    ("Business Administration", "Business", "Comprehensive business operations, leadership, and organizational management."),
    ("Finance", "Business", "Investment banking, portfolio management, derivatives, and financial modeling."),
    ("Supply Chain Management", "Business", "Logistics, procurement, operations management, and global supply networks."),
    ("Hospitality Management", "Business", "Hotel operations, tourism economics, and service industry leadership."),
    ("Tourism Management", "Business", "Destination management, sustainable tourism, and leisure industry operations."),
    ("Retail Management", "Business", "Consumer retail strategy, e-commerce, merchandising, and brand operations."),
    ("Business Analytics", "Business", "Data-driven decision making, business intelligence, and predictive modeling."),
    ("Project Management", "Business", "Agile methodologies, risk management, and delivering complex projects on time."),
    ("Banking", "Business", "Retail and commercial banking, credit risk, and regulatory compliance."),
    ("Insurance", "Business", "Actuarial principles, underwriting, risk assessment, and claims management."),
    ("Public Relations", "Business", "Strategic communications, crisis management, and corporate reputation."),
    ("Advertising", "Business", "Creative campaigns, media buying, digital advertising, and consumer psychology."),

    # Sciences
    ("Mathematics", "Sciences", "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."),
    ("Physics", "Sciences", "Explore the fundamental principles governing matter, energy, and the universe."),
    ("Chemistry", "Sciences", "Study molecular interactions, organic synthesis, and advanced materials science."),
    ("Biology", "Sciences", "Study living organisms, ecology, evolution, and molecular biology."),
    ("Biomedical Sciences", "Sciences", "Investigate human biology, pathology of disease, and laboratory diagnostics."),
    ("Biochemistry", "Sciences", "Explore the chemical processes and molecular mechanisms within living organisms."),
    ("Zoology", "Sciences", "Study animal biology, behavior, ecology, and wildlife conservation."),
    ("Marine Biology", "Sciences", "Examine ocean ecosystems, marine organisms, and coastal conservation."),
    ("Environmental Science", "Sciences", "Address climate change, pollution, and ecological sustainability."),
    ("Geology", "Sciences", "Study the earth's physical structure, minerals, tectonics, and natural resources."),
    ("Astrophysics", "Sciences", "Explore the physical nature of stars, galaxies, dark matter, and the universe."),
    ("Genetics", "Sciences", "Study DNA, heredity, gene therapy, and genetic engineering technologies."),
    ("Sports Science", "Sciences", "The study of human performance, exercise physiology, and sports nutrition."),
    ("Neuroscience", "Sciences", "Investigate the nervous system, brain function, and neurological disorders."),
    ("Forensic Science", "Sciences", "Apply scientific techniques to criminal investigation and evidence analysis."),
    ("Microbiology", "Sciences", "Study microorganisms, infectious diseases, and antimicrobial resistance."),
    ("Ecology", "Sciences", "Study ecosystems, biodiversity, and environmental conservation strategies."),
    ("Pharmacology", "Sciences", "Study how drugs interact with biological systems and treat disease."),
    ("Nutrition", "Sciences", "Study human nutrition, diet science, and public health outcomes."),
    ("Food Science", "Sciences", "Study food production, safety, quality control, and nutritional biochemistry."),
    ("Actuarial Science", "Sciences", "Apply mathematics and statistics to assess financial risk and uncertainty."),
    ("Statistics", "Sciences", "Advanced statistical theory, probability, and data analysis methods."),
    ("Applied Mathematics", "Sciences", "Mathematical modeling applied to engineering, physics, and finance."),

    # STEM
    ("Aerospace Engineering", "STEM", "Design and develop aircraft, spacecraft, and satellite technologies."),
    ("Civil Engineering", "STEM", "Design and build bridges, highways, dams, and essential infrastructure."),
    ("Mechanical Engineering", "STEM", "Study mechanics, thermodynamics, robotics, and manufacturing systems."),
    ("Electrical Engineering", "STEM", "Develop electrical power systems, circuits, and renewable energy grids."),
    ("Chemical Engineering", "STEM", "Industrial process design, material synthesis, and sustainable manufacturing."),
    ("Cyber Security", "STEM", "Protect networks, systems, and data from digital threats and cyber attacks."),
    ("Data Science", "STEM", "Analyze big data, build machine learning models, and drive data strategy."),
    ("Software Engineering", "STEM", "Build scalable, production-grade software applications and distributed systems."),
    ("Artificial Intelligence", "STEM", "Develop intelligent systems, neural networks, and machine learning algorithms."),
    ("Information Technology", "STEM", "Manage digital infrastructure, cloud computing, and enterprise networking."),
    ("Architecture", "STEM", "Blend art and structural engineering to design physical spaces and cities."),
    ("Robotics", "STEM", "Design autonomous systems, mechatronics, and industrial automation."),
    ("Biomedical Engineering", "STEM", "Apply engineering principles to medical devices and healthcare technology."),
    ("Environmental Engineering", "STEM", "Design sustainable solutions for water, waste, and pollution control."),
    ("Automotive Engineering", "STEM", "Design and develop vehicles, powertrains, and electric mobility systems."),
    ("Marine Engineering", "STEM", "Design and maintain ships, submarines, and offshore energy platforms."),
    ("Renewable Energy Engineering", "STEM", "Solar, wind, and hydrogen energy systems design and implementation."),
    ("Telecommunications Engineering", "STEM", "Design communication networks, 5G systems, and signal processing."),
    ("Nuclear Engineering", "STEM", "Nuclear power generation, radiation safety, and reactor design."),
    ("Games Technology", "STEM", "Video game development, 3D engines, and interactive media programming."),
    ("Web Development", "STEM", "Full-stack development, frontend frameworks, and web application architecture."),
    ("Cloud Computing", "STEM", "AWS, Azure, and GCP infrastructure design and DevOps engineering."),
    ("Blockchain Technology", "STEM", "Distributed ledger technology, smart contracts, and decentralized applications."),

    # Healthcare
    ("Nursing", "Healthcare", "Provide frontline clinical care, patient assessment, and holistic support across specialties."),
    ("Dentistry", "Healthcare", "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."),
    ("Pharmacy", "Healthcare", "Study pharmaceutical sciences, drug dispensing, and patient-centered care."),
    ("Veterinary Medicine", "Healthcare", "Clinical training for the diagnosis, treatment, and care of animals."),
    ("Physiotherapy", "Healthcare", "Physical rehabilitation, musculoskeletal therapy, and movement science."),
    ("Radiography", "Healthcare", "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."),
    ("Paramedic Science", "Healthcare", "Emergency medical response, trauma care, and pre-hospital medicine."),
    ("Midwifery", "Healthcare", "Care for women during pregnancy, childbirth, and the postpartum period."),
    ("Optometry", "Healthcare", "Examine eyes for vision defects, prescribe lenses, and detect eye disease."),
    ("Occupational Therapy", "Healthcare", "Help patients overcome physical and psychological barriers to daily life."),
    ("Speech and Language Therapy", "Healthcare", "Diagnose and treat communication, speech, and swallowing disorders."),
    ("Dietetics", "Healthcare", "Clinical nutrition science, dietary interventions, and public health nutrition."),
    ("Public Health", "Healthcare", "Epidemiology, health promotion, and population-level disease prevention."),
    ("Mental Health Nursing", "Healthcare", "Specialist nursing care for patients with mental health conditions."),
    ("Adult Nursing", "Healthcare", "Clinical nursing care for adult patients across medical and surgical settings."),
    ("Children's Nursing", "Healthcare", "Specialist nursing care for infants, children, and young people."),
    ("Audiology", "Healthcare", "Assess and treat hearing and balance disorders across all ages."),
    ("Podiatry", "Healthcare", "Diagnose and treat conditions of the feet and lower limbs."),
    ("Biomedical Science", "Healthcare", "Laboratory diagnosis, blood sciences, and clinical pathology."),

    # Arts & Design
    ("Graphic Design", "Arts & Design", "Visual communication, branding, typography, and digital media design."),
    ("Fine Art", "Arts & Design", "Develop creative practice across painting, sculpture, and mixed media."),
    ("Fashion Design", "Arts & Design", "Create apparel, study textiles, pattern cutting, and the fashion industry."),
    ("Interior Design", "Arts & Design", "Design functional and aesthetic indoor spaces for residential and commercial use."),
    ("Product Design", "Arts & Design", "Conceptualize, prototype, and manufacture consumer goods and industrial products."),
    ("Animation", "Arts & Design", "2D and 3D visual storytelling, motion graphics, and character design."),
    ("Music", "Arts & Design", "Performance, composition, music technology, and music theory."),
    ("Drama and Theatre Studies", "Arts & Design", "Acting, directing, stage production, and dramatic literature."),
    ("Photography", "Arts & Design", "Master digital and analog photographic techniques and visual storytelling."),
    ("Illustration", "Arts & Design", "Editorial, children's book, and commercial illustration techniques."),
    ("Textile Design", "Arts & Design", "Fabric printing, weaving, sustainable textiles, and surface design."),
    ("Jewellery Design", "Arts & Design", "Gemology, metalwork, CAD jewelry design, and luxury brand development."),
    ("Game Design", "Arts & Design", "Game mechanics, level design, narrative design, and user experience."),
    ("Music Production", "Arts & Design", "Audio engineering, sound design, mixing, and mastering techniques."),
    ("Dance", "Arts & Design", "Contemporary dance, choreography, and performing arts practice."),
    ("Creative Arts", "Arts & Design", "Interdisciplinary creative practice across visual and performing arts."),

    # Media
    ("Film and Television", "Media", "Video production, directing, cinematography, and post-production editing."),
    ("Media Studies", "Media", "Analyze mass communication, digital culture, and media theory."),
    ("Journalism", "Media", "Investigative reporting, multimedia broadcasting, and digital journalism."),
    ("Broadcasting", "Media", "Radio and television production, live broadcasting, and media technology."),
    ("Digital Media", "Media", "Social media strategy, content creation, and digital platform management."),
    ("Public Relations and Communications", "Media", "Strategic communications, crisis management, and media relations."),
    ("Film Studies", "Media", "Critical analysis of cinema, film theory, and world cinema movements."),
    ("Publishing", "Media", "Editorial processes, book publishing, and digital content distribution."),

    # Education
    ("Primary Education", "Education", "Train to teach and inspire children aged 5-11 across the national curriculum."),
    ("Early Childhood Studies", "Education", "Study child development, early years pedagogy, and childcare policy."),
    ("Secondary Education", "Education", "Train to teach specialist subjects to students aged 11-18."),
    ("Special Educational Needs", "Education", "Support learners with additional needs, disabilities, and learning differences."),
    ("Education Studies", "Education", "Explore educational theory, policy, and learning across diverse contexts."),
    ("Teaching English as a Foreign Language", "Education", "Teach English language skills to non-native speakers worldwide."),
    ("Sport Coaching", "Education", "Develop athletic talent through evidence-based coaching methodologies."),
    ("Physical Education", "Education", "Train to teach PE and promote physical literacy in school settings."),

    # Public Sector
    ("Social Work", "Public Sector", "Support vulnerable individuals, families, and communities through intervention."),
    ("Policing", "Public Sector", "Law enforcement, forensic investigation, and community public safety."),
    ("Criminology and Policing", "Public Sector", "Criminal justice, crime prevention, and modern policing strategies."),
    ("Youth Work", "Public Sector", "Engage and empower young people through community programs and support."),
    ("Urban Planning", "Public Sector", "Design sustainable cities, housing policy, and urban regeneration."),
    ("Environmental Policy", "Public Sector", "Climate legislation, green policy development, and sustainability governance."),
    ("Disaster Management", "Public Sector", "Emergency planning, crisis response, and humanitarian coordination."),
    ("International Development", "Public Sector", "Global poverty reduction, NGO management, and sustainable development goals."),
]

modifiers = [
    " (BSc)",
    " (BA)",
    " (MSc)",
    " (MA)",
    " (Integrated Masters)",
    " with Professional Placement (BSc)",
    " with a Year in Industry (BA)",
    " with Study Abroad (MSc)",
    " with Foundation Year (BSc)",
    " and Management (MSc)",
    " and Finance (BSc)",
    " with Data Science (MSc)",
    " and International Relations (BA)",
    " (BSc Hons)",
    " (BA Hons)",
    " with Sandwich Year (BSc)",
    " (MRes)",
    " (Graduate Diploma)",
]

# Keep track of added titles to avoid exact duplicates
added_titles = set([c['title'] for c in courses])

target = 1000
while len(courses) < target:
    base = random.choice(base_subjects)
    mod = random.choice(modifiers)
    
    title = base[0] + mod
    if title in added_titles:
        continue
        
    url_course = title.replace(" ", "%20")
    courses.append({
        "title": title,
        "category": base[1],
        "url": f"course-details.html?course={url_course}",
        "desc": base[2]
    })
    added_titles.add(title)

# Shuffle generated ones for natural display, keep top 5 dedicated
generated = courses[5:]
random.shuffle(generated)
courses = courses[:5] + generated

js_content = f"const courseDatabase = {json.dumps(courses, indent=4)};\n"

with open("js/courses.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated exactly {len(courses)} courses in js/courses.js!")
