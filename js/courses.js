const courseDatabase = [
    {
        "title": "Medicine (MBBS)",
        "category": "Healthcare",
        "url": "course-details.html?course=Medicine%20(MBBS)",
        "desc": "Train for a career as a doctor with extensive clinical placements and hands-on anatomy."
    },
    {
        "title": "Law (LLB)",
        "category": "Humanities",
        "url": "course-details.html?course=Law%20(LLB)",
        "desc": "Develop rigorous analytical skills and prepare for a legal career with mock trials."
    },
    {
        "title": "Computer Science",
        "category": "STEM",
        "url": "course-details.html?course=Computer%20Science",
        "desc": "Master software engineering, AI, algorithms, and complex systems architecture."
    },
    {
        "title": "Business Management",
        "category": "Business",
        "url": "course-details.html?course=Business%20Management",
        "desc": "Learn global enterprise strategy, finance, and leadership in modern organizations."
    },
    {
        "title": "Engineering (BEng/MEng)",
        "category": "STEM",
        "url": "course-details.html?course=Engineering%20(BEng%2FMEng)",
        "desc": "Design the future across civil, mechanical, electrical and aerospace fields."
    },
    {
        "title": "Games Technology (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20(BA%20Hons)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Automotive Engineering with Data Science (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20with%20Data%20Science%20(MSc)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Biochemistry (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Biochemistry%20(MA)",
        "desc": "Explore the chemical processes and molecular mechanisms within living organisms."
    },
    {
        "title": "International Development with Study Abroad (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20with%20Study%20Abroad%20(MSc)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "Project Management with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Project%20Management%20with%20Study%20Abroad%20(MSc)",
        "desc": "Agile methodologies, risk management, and delivering complex projects on time."
    },
    {
        "title": "Cyber Security with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Cyber%20Security%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Protect networks, systems, and data from digital threats and cyber attacks."
    },
    {
        "title": "Youth Work with Data Science (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Youth%20Work%20with%20Data%20Science%20(MSc)",
        "desc": "Engage and empower young people through community programs and support."
    },
    {
        "title": "Real Estate (MRes)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20(MRes)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Modern Languages with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20with%20Study%20Abroad%20(MSc)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "Environmental Policy with Foundation Year (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20with%20Foundation%20Year%20(BSc)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "Modern Languages (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20(MA)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "French and Management (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=French%20and%20Management%20(MSc)",
        "desc": "Master French language, literature, cinema, and Francophone cultures."
    },
    {
        "title": "Politics and International Studies with a Year in Industry (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Politics%20and%20International%20Studies%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Study political systems, governance, and global institutions."
    },
    {
        "title": "Criminology (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20(BSc)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Child Psychology (MA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Child%20Psychology%20(MA)",
        "desc": "Study cognitive, emotional, and social development from infancy to adolescence."
    },
    {
        "title": "Electrical Engineering (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20(BSc)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Real Estate and Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20and%20Management%20(MSc)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Politics with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20with%20Foundation%20Year%20(BSc)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Media Studies with Study Abroad (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20with%20Study%20Abroad%20(MSc)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Automotive Engineering (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(BSc%20Hons)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Primary Education with a Year in Industry (BA)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "Marketing with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Marketing%20with%20Foundation%20Year%20(BSc)",
        "desc": "Consumer behavior, digital strategy, brand management, and market research."
    },
    {
        "title": "Physical Education (MRes)",
        "category": "Education",
        "url": "course-details.html?course=Physical%20Education%20(MRes)",
        "desc": "Train to teach PE and promote physical literacy in school settings."
    },
    {
        "title": "Spanish (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20(MA)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Illustration and Management (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Illustration%20and%20Management%20(MSc)",
        "desc": "Editorial, children's book, and commercial illustration techniques."
    },
    {
        "title": "Hospitality Management (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20(BA%20Hons)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "Geography (BSc Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20(BSc%20Hons)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Insurance (Integrated Masters)",
        "category": "Business",
        "url": "course-details.html?course=Insurance%20(Integrated%20Masters)",
        "desc": "Actuarial principles, underwriting, risk assessment, and claims management."
    },
    {
        "title": "Game Design (MRes)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20(MRes)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Public Relations and Communications with a Year in Industry (BA)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Environmental Science with Foundation Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Environmental%20Science%20with%20Foundation%20Year%20(BSc)",
        "desc": "Address climate change, pollution, and ecological sustainability."
    },
    {
        "title": "Nuclear Engineering with Sandwich Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Accounting and Finance (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Accounting%20and%20Finance%20(BSc)",
        "desc": "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."
    },
    {
        "title": "Children's Nursing with Professional Placement (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Children's%20Nursing%20with%20Professional%20Placement%20(BSc)",
        "desc": "Specialist nursing care for infants, children, and young people."
    },
    {
        "title": "Anthropology (BA Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20(BA%20Hons)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Public Health and Management (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Public%20Health%20and%20Management%20(MSc)",
        "desc": "Epidemiology, health promotion, and population-level disease prevention."
    },
    {
        "title": "Youth Work (BA Hons)",
        "category": "Public Sector",
        "url": "course-details.html?course=Youth%20Work%20(BA%20Hons)",
        "desc": "Engage and empower young people through community programs and support."
    },
    {
        "title": "Criminology and Policing with Sandwich Year (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Philosophy with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20with%20Study%20Abroad%20(MSc)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Business Administration (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20(Graduate%20Diploma)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Creative Writing with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Creative%20Writing%20with%20Study%20Abroad%20(MSc)",
        "desc": "Develop fiction, poetry, screenwriting, and non-fiction storytelling skills."
    },
    {
        "title": "Data Science with Sandwich Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Data%20Science%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Analyze big data, build machine learning models, and drive data strategy."
    },
    {
        "title": "French (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=French%20(Graduate%20Diploma)",
        "desc": "Master French language, literature, cinema, and Francophone cultures."
    },
    {
        "title": "Business Administration with Professional Placement (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20with%20Professional%20Placement%20(BSc)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Secondary Education with Sandwich Year (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "History (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20(BSc)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "Human Resource Management with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Human%20Resource%20Management%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Manage talent, recruitment, organizational behavior, and employment law."
    },
    {
        "title": "Optometry with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20with%20Data%20Science%20(MSc)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Paramedic Science (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20(BSc%20Hons)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Jewellery Design with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20with%20Data%20Science%20(MSc)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Ecology (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Ecology%20(BA)",
        "desc": "Study ecosystems, biodiversity, and environmental conservation strategies."
    },
    {
        "title": "Astrophysics with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Astrophysics%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Explore the physical nature of stars, galaxies, dark matter, and the universe."
    },
    {
        "title": "Architecture (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20(BA)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Chinese Studies and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Chinese%20Studies%20and%20International%20Relations%20(BA)",
        "desc": "Mandarin language proficiency combined with East Asian history and politics."
    },
    {
        "title": "Music Production with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20with%20Foundation%20Year%20(BSc)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Physiotherapy and Finance (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Physiotherapy%20and%20Finance%20(BSc)",
        "desc": "Physical rehabilitation, musculoskeletal therapy, and movement science."
    },
    {
        "title": "Pharmacy with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Pharmacy%20with%20Data%20Science%20(MSc)",
        "desc": "Study pharmaceutical sciences, drug dispensing, and patient-centered care."
    },
    {
        "title": "Geography and International Relations (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20and%20International%20Relations%20(BA)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Data Science (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Data%20Science%20(BSc%20Hons)",
        "desc": "Analyze big data, build machine learning models, and drive data strategy."
    },
    {
        "title": "Games Technology with Study Abroad (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20with%20Study%20Abroad%20(MSc)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Photography and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20and%20Finance%20(BSc)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Paramedic Science with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20with%20Data%20Science%20(MSc)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Podiatry (BA Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20(BA%20Hons)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Criminology and Policing (BA Hons)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20(BA%20Hons)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Primary Education (Integrated Masters)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20(Integrated%20Masters)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "Journalism with Data Science (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20with%20Data%20Science%20(MSc)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "Film Studies (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20(MSc)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Neuroscience with Data Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20with%20Data%20Science%20(MSc)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Mechanical Engineering with Professional Placement (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "Economics with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20with%20Foundation%20Year%20(BSc)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "Animation (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20(BSc%20Hons)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Arabic (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=Arabic%20(Graduate%20Diploma)",
        "desc": "Study Arabic language, Islamic civilizations, and Middle Eastern politics."
    },
    {
        "title": "Classics and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Classics%20and%20Finance%20(BSc)",
        "desc": "Study the literature, history, and culture of ancient Greece and Rome."
    },
    {
        "title": "Mathematics with Study Abroad (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20with%20Study%20Abroad%20(MSc)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Marine Biology and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20and%20Management%20(MSc)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Drama and Theatre Studies (MRes)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Drama%20and%20Theatre%20Studies%20(MRes)",
        "desc": "Acting, directing, stage production, and dramatic literature."
    },
    {
        "title": "Forensic Science with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Classics (BA Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Classics%20(BA%20Hons)",
        "desc": "Study the literature, history, and culture of ancient Greece and Rome."
    },
    {
        "title": "Textile Design and Management (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Textile%20Design%20and%20Management%20(MSc)",
        "desc": "Fabric printing, weaving, sustainable textiles, and surface design."
    },
    {
        "title": "Games Technology and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20and%20Finance%20(BSc)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Film and Television with Professional Placement (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20with%20Professional%20Placement%20(BSc)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Biomedical Sciences (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20(MRes)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Human Resource Management (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Human%20Resource%20Management%20(BA%20Hons)",
        "desc": "Manage talent, recruitment, organizational behavior, and employment law."
    },
    {
        "title": "Photography (Graduate Diploma)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20(Graduate%20Diploma)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Mathematics (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20(BA%20Hons)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Blockchain Technology with Data Science (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20with%20Data%20Science%20(MSc)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Broadcasting with Data Science (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Broadcasting%20with%20Data%20Science%20(MSc)",
        "desc": "Radio and television production, live broadcasting, and media technology."
    },
    {
        "title": "Criminology (Integrated Masters)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20(Integrated%20Masters)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Dentistry with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Philosophy (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20(Integrated%20Masters)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Retail Management and Finance (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20and%20Finance%20(BSc)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Journalism (MA)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20(MA)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "International Relations (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=International%20Relations%20(BSc)",
        "desc": "Analyze global diplomacy, conflict resolution, and foreign policy frameworks."
    },
    {
        "title": "Biochemistry and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biochemistry%20and%20Management%20(MSc)",
        "desc": "Explore the chemical processes and molecular mechanisms within living organisms."
    },
    {
        "title": "Business Analytics with Sandwich Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Analytics%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Data-driven decision making, business intelligence, and predictive modeling."
    },
    {
        "title": "Artificial Intelligence and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20and%20Finance%20(BSc)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Nutrition (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Nutrition%20(BSc)",
        "desc": "Study human nutrition, diet science, and public health outcomes."
    },
    {
        "title": "Classics (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=Classics%20(MA)",
        "desc": "Study the literature, history, and culture of ancient Greece and Rome."
    },
    {
        "title": "Web Development (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20(BA%20Hons)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Web Development and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20and%20International%20Relations%20(BA)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Biomedical Sciences (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20(Integrated%20Masters)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "International Development and Finance (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20and%20Finance%20(BSc)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "International Business (MSc)",
        "category": "Business",
        "url": "course-details.html?course=International%20Business%20(MSc)",
        "desc": "Global trade, cross-border strategy, supply chain, and international markets."
    },
    {
        "title": "Film Studies (MA)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20(MA)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Social Policy with a Year in Industry (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Social%20Policy%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Examine welfare systems, public health policy, and social inequality."
    },
    {
        "title": "History (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20(Integrated%20Masters)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "Sociology (BSc Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20(BSc%20Hons)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Product Design with a Year in Industry (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Mathematics with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "English Literature with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20with%20Professional%20Placement%20(BSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Ecology with Foundation Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Ecology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Study ecosystems, biodiversity, and environmental conservation strategies."
    },
    {
        "title": "Entrepreneurship and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Entrepreneurship%20and%20International%20Relations%20(BA)",
        "desc": "Learn to ideate, build, launch, and scale startup ventures and SMEs."
    },
    {
        "title": "Marine Engineering (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20(MSc)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Chemistry and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Chemistry%20and%20Management%20(MSc)",
        "desc": "Study molecular interactions, organic synthesis, and advanced materials science."
    },
    {
        "title": "Biology (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Biology%20(Integrated%20Masters)",
        "desc": "Study living organisms, ecology, evolution, and molecular biology."
    },
    {
        "title": "Nursing with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Fine Art (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20(MSc)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Banking and Finance (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Banking%20and%20Finance%20(BSc)",
        "desc": "Retail and commercial banking, credit risk, and regulatory compliance."
    },
    {
        "title": "Nutrition and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Nutrition%20and%20International%20Relations%20(BA)",
        "desc": "Study human nutrition, diet science, and public health outcomes."
    },
    {
        "title": "Neuroscience and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20and%20Finance%20(BSc)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Automotive Engineering with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20with%20Foundation%20Year%20(BSc)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Astrophysics (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Astrophysics%20(MSc)",
        "desc": "Explore the physical nature of stars, galaxies, dark matter, and the universe."
    },
    {
        "title": "Primary Education (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20(BSc)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "Chemistry (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Chemistry%20(Integrated%20Masters)",
        "desc": "Study molecular interactions, organic synthesis, and advanced materials science."
    },
    {
        "title": "Game Design (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20(BA)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Actuarial Science with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Actuarial%20Science%20with%20Professional%20Placement%20(BSc)",
        "desc": "Apply mathematics and statistics to assess financial risk and uncertainty."
    },
    {
        "title": "Adult Nursing (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Adult%20Nursing%20(Graduate%20Diploma)",
        "desc": "Clinical nursing care for adult patients across medical and surgical settings."
    },
    {
        "title": "Optometry (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20(BSc)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Film Studies (Integrated Masters)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20(Integrated%20Masters)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Disaster Management (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Disaster%20Management%20(MSc)",
        "desc": "Emergency planning, crisis response, and humanitarian coordination."
    },
    {
        "title": "Blockchain Technology with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Public Relations and Communications (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20(BSc)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Physics and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20and%20Management%20(MSc)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Jewellery Design with a Year in Industry (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Business Administration (BA)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20(BA)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Criminology and Policing and Finance (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20and%20Finance%20(BSc)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Animation and International Relations (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20and%20International%20Relations%20(BA)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Biomedical Science (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Biomedical%20Science%20(Integrated%20Masters)",
        "desc": "Laboratory diagnosis, blood sciences, and clinical pathology."
    },
    {
        "title": "Disaster Management and Finance (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Disaster%20Management%20and%20Finance%20(BSc)",
        "desc": "Emergency planning, crisis response, and humanitarian coordination."
    },
    {
        "title": "Food Science (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20(MA)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Publishing (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20(MSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Dietetics and Management (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dietetics%20and%20Management%20(MSc)",
        "desc": "Clinical nutrition science, dietary interventions, and public health nutrition."
    },
    {
        "title": "Retail Management with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20with%20Study%20Abroad%20(MSc)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Civil Engineering (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Civil%20Engineering%20(BSc)",
        "desc": "Design and build bridges, highways, dams, and essential infrastructure."
    },
    {
        "title": "Games Technology with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Food Science with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Public Relations and Communications (MRes)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20(MRes)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Textile Design with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Textile%20Design%20with%20Data%20Science%20(MSc)",
        "desc": "Fabric printing, weaving, sustainable textiles, and surface design."
    },
    {
        "title": "Drama and Theatre Studies with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Drama%20and%20Theatre%20Studies%20with%20Data%20Science%20(MSc)",
        "desc": "Acting, directing, stage production, and dramatic literature."
    },
    {
        "title": "Film and Television (BA Hons)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20(BA%20Hons)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Media Studies and International Relations (BA)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20and%20International%20Relations%20(BA)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Urban Planning with Foundation Year (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20with%20Foundation%20Year%20(BSc)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Public Health (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Public%20Health%20(BA)",
        "desc": "Epidemiology, health promotion, and population-level disease prevention."
    },
    {
        "title": "Fashion Design with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20with%20Foundation%20Year%20(BSc)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Midwifery (MA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Midwifery%20(MA)",
        "desc": "Care for women during pregnancy, childbirth, and the postpartum period."
    },
    {
        "title": "Public Relations and Communications and Management (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20and%20Management%20(MSc)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Politics and International Studies (MRes)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Politics%20and%20International%20Studies%20(MRes)",
        "desc": "Study political systems, governance, and global institutions."
    },
    {
        "title": "Film and Television (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20(BSc)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Arabic with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Arabic%20with%20Foundation%20Year%20(BSc)",
        "desc": "Study Arabic language, Islamic civilizations, and Middle Eastern politics."
    },
    {
        "title": "Environmental Policy (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20(MSc)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "Paramedic Science and Management (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20and%20Management%20(MSc)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Insurance (MA)",
        "category": "Business",
        "url": "course-details.html?course=Insurance%20(MA)",
        "desc": "Actuarial principles, underwriting, risk assessment, and claims management."
    },
    {
        "title": "Nutrition (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Nutrition%20(MA)",
        "desc": "Study human nutrition, diet science, and public health outcomes."
    },
    {
        "title": "Economics (MRes)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20(MRes)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "Broadcasting (BSc Hons)",
        "category": "Media",
        "url": "course-details.html?course=Broadcasting%20(BSc%20Hons)",
        "desc": "Radio and television production, live broadcasting, and media technology."
    },
    {
        "title": "Environmental Science (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Environmental%20Science%20(BA)",
        "desc": "Address climate change, pollution, and ecological sustainability."
    },
    {
        "title": "Marine Biology (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20(MSc)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Advertising (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20(BA%20Hons)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Real Estate and Finance (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20and%20Finance%20(BSc)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Business Analytics (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Analytics%20(BA%20Hons)",
        "desc": "Data-driven decision making, business intelligence, and predictive modeling."
    },
    {
        "title": "Child Psychology and International Relations (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Child%20Psychology%20and%20International%20Relations%20(BA)",
        "desc": "Study cognitive, emotional, and social development from infancy to adolescence."
    },
    {
        "title": "Politics and International Studies (BA Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Politics%20and%20International%20Studies%20(BA%20Hons)",
        "desc": "Study political systems, governance, and global institutions."
    },
    {
        "title": "Dietetics (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dietetics%20(Graduate%20Diploma)",
        "desc": "Clinical nutrition science, dietary interventions, and public health nutrition."
    },
    {
        "title": "Game Design with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20with%20Foundation%20Year%20(BSc)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Product Design (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20(BSc)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Data Science (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Data%20Science%20(BSc)",
        "desc": "Analyze big data, build machine learning models, and drive data strategy."
    },
    {
        "title": "Mental Health Nursing with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20with%20Data%20Science%20(MSc)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Creative Writing (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Creative%20Writing%20(BA)",
        "desc": "Develop fiction, poetry, screenwriting, and non-fiction storytelling skills."
    },
    {
        "title": "Blockchain Technology (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20(MA)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Special Educational Needs (Integrated Masters)",
        "category": "Education",
        "url": "course-details.html?course=Special%20Educational%20Needs%20(Integrated%20Masters)",
        "desc": "Support learners with additional needs, disabilities, and learning differences."
    },
    {
        "title": "Tourism Management (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Tourism%20Management%20(Graduate%20Diploma)",
        "desc": "Destination management, sustainable tourism, and leisure industry operations."
    },
    {
        "title": "Photography with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Classics (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Classics%20(BSc%20Hons)",
        "desc": "Study the literature, history, and culture of ancient Greece and Rome."
    },
    {
        "title": "Media Studies with Sandwich Year (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Insurance (BA)",
        "category": "Business",
        "url": "course-details.html?course=Insurance%20(BA)",
        "desc": "Actuarial principles, underwriting, risk assessment, and claims management."
    },
    {
        "title": "Secondary Education with Professional Placement (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20with%20Professional%20Placement%20(BSc)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "Classics with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Classics%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study the literature, history, and culture of ancient Greece and Rome."
    },
    {
        "title": "Robotics with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Film and Television (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20(MSc)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Retail Management and Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20and%20Management%20(MSc)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Arabic and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Arabic%20and%20International%20Relations%20(BA)",
        "desc": "Study Arabic language, Islamic civilizations, and Middle Eastern politics."
    },
    {
        "title": "Podiatry with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20with%20Study%20Abroad%20(MSc)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Biology with Study Abroad (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biology%20with%20Study%20Abroad%20(MSc)",
        "desc": "Study living organisms, ecology, evolution, and molecular biology."
    },
    {
        "title": "Product Design (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20(BA)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Criminology and Policing (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20(MSc)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Occupational Therapy with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Public Relations (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20(BA%20Hons)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Radiography (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20(Graduate%20Diploma)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Sports Science with Foundation Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20with%20Foundation%20Year%20(BSc)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Geology (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Geology%20(BSc%20Hons)",
        "desc": "Study the earth's physical structure, minerals, tectonics, and natural resources."
    },
    {
        "title": "Textile Design with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Textile%20Design%20with%20Study%20Abroad%20(MSc)",
        "desc": "Fabric printing, weaving, sustainable textiles, and surface design."
    },
    {
        "title": "Applied Mathematics (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Applied%20Mathematics%20(BA)",
        "desc": "Mathematical modeling applied to engineering, physics, and finance."
    },
    {
        "title": "Secondary Education and Finance (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20and%20Finance%20(BSc)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "Children's Nursing (MA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Children's%20Nursing%20(MA)",
        "desc": "Specialist nursing care for infants, children, and young people."
    },
    {
        "title": "Spanish (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20(MRes)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Film and Television (BA)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20(BA)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "French (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=French%20(MA)",
        "desc": "Master French language, literature, cinema, and Francophone cultures."
    },
    {
        "title": "Publishing and Management (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20and%20Management%20(MSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Nursing (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20(BSc)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Radiography with Professional Placement (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20with%20Professional%20Placement%20(BSc)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "International Relations with Foundation Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=International%20Relations%20with%20Foundation%20Year%20(BSc)",
        "desc": "Analyze global diplomacy, conflict resolution, and foreign policy frameworks."
    },
    {
        "title": "Education Studies (BA)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20(BA)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Business Administration with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20with%20Study%20Abroad%20(MSc)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Radiography (BA Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20(BA%20Hons)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Civil Engineering (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Civil%20Engineering%20(MSc)",
        "desc": "Design and build bridges, highways, dams, and essential infrastructure."
    },
    {
        "title": "Sports Science with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20with%20Sandwich%20Year%20(BSc)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Speech and Language Therapy and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Speech%20and%20Language%20Therapy%20and%20International%20Relations%20(BA)",
        "desc": "Diagnose and treat communication, speech, and swallowing disorders."
    },
    {
        "title": "Disaster Management (MRes)",
        "category": "Public Sector",
        "url": "course-details.html?course=Disaster%20Management%20(MRes)",
        "desc": "Emergency planning, crisis response, and humanitarian coordination."
    },
    {
        "title": "Economics with Professional Placement (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20with%20Professional%20Placement%20(BSc)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "Actuarial Science (Graduate Diploma)",
        "category": "Sciences",
        "url": "course-details.html?course=Actuarial%20Science%20(Graduate%20Diploma)",
        "desc": "Apply mathematics and statistics to assess financial risk and uncertainty."
    },
    {
        "title": "Interior Design with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20with%20Professional%20Placement%20(BSc)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Architecture with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "English Literature and Management (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20and%20Management%20(MSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "French with a Year in Industry (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=French%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Master French language, literature, cinema, and Francophone cultures."
    },
    {
        "title": "English Literature with Sandwich Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Sociology (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20(BA)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Advertising (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20(BSc%20Hons)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Audiology with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20with%20Data%20Science%20(MSc)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Food Science (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20(BA%20Hons)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Mental Health Nursing with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20with%20Study%20Abroad%20(MSc)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Mental Health Nursing with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20with%20Foundation%20Year%20(BSc)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Event Management with Sandwich Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Event%20Management%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Plan and execute large-scale corporate events, festivals, and conferences."
    },
    {
        "title": "English Literature (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20(MSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Ancient History (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=Ancient%20History%20(Integrated%20Masters)",
        "desc": "Explore the civilizations of the ancient world from Mesopotamia to Rome."
    },
    {
        "title": "Automotive Engineering (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(BA%20Hons)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Optometry with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20with%20Foundation%20Year%20(BSc)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Adult Nursing with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Adult%20Nursing%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Clinical nursing care for adult patients across medical and surgical settings."
    },
    {
        "title": "Dentistry (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20(BSc)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Chinese Studies with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Chinese%20Studies%20with%20Professional%20Placement%20(BSc)",
        "desc": "Mandarin language proficiency combined with East Asian history and politics."
    },
    {
        "title": "Creative Writing with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Creative%20Writing%20with%20Professional%20Placement%20(BSc)",
        "desc": "Develop fiction, poetry, screenwriting, and non-fiction storytelling skills."
    },
    {
        "title": "German and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=German%20and%20International%20Relations%20(BA)",
        "desc": "Explore German language, literature, philosophy, and Central European culture."
    },
    {
        "title": "Politics (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20(BSc%20Hons)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Sociology with Sandwich Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Social Policy with Sandwich Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Social%20Policy%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Examine welfare systems, public health policy, and social inequality."
    },
    {
        "title": "Pharmacology with Foundation Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Pharmacology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Study how drugs interact with biological systems and treat disease."
    },
    {
        "title": "Sports Science and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20and%20Finance%20(BSc)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Anthropology (Graduate Diploma)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20(Graduate%20Diploma)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Robotics with Sandwich Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Criminology and International Relations (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20and%20International%20Relations%20(BA)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Nuclear Engineering with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Forensic Psychology and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20and%20Management%20(MSc)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Statistics (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Statistics%20(Integrated%20Masters)",
        "desc": "Advanced statistical theory, probability, and data analysis methods."
    },
    {
        "title": "Japanese Studies and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20and%20International%20Relations%20(BA)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Illustration (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Illustration%20(BSc)",
        "desc": "Editorial, children's book, and commercial illustration techniques."
    },
    {
        "title": "Audiology with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20with%20Study%20Abroad%20(MSc)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Robotics (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20(MRes)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Arabic (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Arabic%20(BSc)",
        "desc": "Study Arabic language, Islamic civilizations, and Middle Eastern politics."
    },
    {
        "title": "Philosophy (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20(MSc)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Pharmacology (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Pharmacology%20(BA)",
        "desc": "Study how drugs interact with biological systems and treat disease."
    },
    {
        "title": "Jewellery Design with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20with%20Foundation%20Year%20(BSc)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "History with a Year in Industry (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "Music (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20(Integrated%20Masters)",
        "desc": "Performance, composition, music technology, and music theory."
    },
    {
        "title": "Animation with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20with%20Sandwich%20Year%20(BSc)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Geology with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Geology%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study the earth's physical structure, minerals, tectonics, and natural resources."
    },
    {
        "title": "Teaching English as a Foreign Language and International Relations (BA)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20and%20International%20Relations%20(BA)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Occupational Therapy (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20(BSc)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Biomedical Sciences with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Geology (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Geology%20(MSc)",
        "desc": "Study the earth's physical structure, minerals, tectonics, and natural resources."
    },
    {
        "title": "Forensic Psychology with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Chemistry (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Chemistry%20(BSc%20Hons)",
        "desc": "Study molecular interactions, organic synthesis, and advanced materials science."
    },
    {
        "title": "Criminology with a Year in Industry (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Social Policy (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Social%20Policy%20(MSc)",
        "desc": "Examine welfare systems, public health policy, and social inequality."
    },
    {
        "title": "Spanish with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Film Studies and Finance (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20and%20Finance%20(BSc)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Archaeology with Data Science (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Archaeology%20with%20Data%20Science%20(MSc)",
        "desc": "Investigate past cultures through material remains and fieldwork excavation."
    },
    {
        "title": "Politics (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20(Integrated%20Masters)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Information Technology (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Information%20Technology%20(BA%20Hons)",
        "desc": "Manage digital infrastructure, cloud computing, and enterprise networking."
    },
    {
        "title": "Ancient History and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Ancient%20History%20and%20International%20Relations%20(BA)",
        "desc": "Explore the civilizations of the ancient world from Mesopotamia to Rome."
    },
    {
        "title": "Robotics (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20(BSc)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Geology (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Geology%20(MA)",
        "desc": "Study the earth's physical structure, minerals, tectonics, and natural resources."
    },
    {
        "title": "Chemical Engineering with Sandwich Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Chemical%20Engineering%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Industrial process design, material synthesis, and sustainable manufacturing."
    },
    {
        "title": "Journalism (Integrated Masters)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20(Integrated%20Masters)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "Astrophysics with Study Abroad (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Astrophysics%20with%20Study%20Abroad%20(MSc)",
        "desc": "Explore the physical nature of stars, galaxies, dark matter, and the universe."
    },
    {
        "title": "Artificial Intelligence (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20(Integrated%20Masters)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Primary Education with Study Abroad (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20with%20Study%20Abroad%20(MSc)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "English Language with Data Science (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20with%20Data%20Science%20(MSc)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Forensic Psychology with Data Science (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20with%20Data%20Science%20(MSc)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Veterinary Medicine (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20(BSc)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Microbiology with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Hospitality Management and Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20and%20Management%20(MSc)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "Graphic Design and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Graphic%20Design%20and%20Finance%20(BSc)",
        "desc": "Visual communication, branding, typography, and digital media design."
    },
    {
        "title": "Mechanical Engineering (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20(BA%20Hons)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "Paramedic Science with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20with%20Foundation%20Year%20(BSc)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "History (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20(BSc%20Hons)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "Chemical Engineering (Graduate Diploma)",
        "category": "STEM",
        "url": "course-details.html?course=Chemical%20Engineering%20(Graduate%20Diploma)",
        "desc": "Industrial process design, material synthesis, and sustainable manufacturing."
    },
    {
        "title": "Radiography (MRes)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20(MRes)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Event Management (MRes)",
        "category": "Business",
        "url": "course-details.html?course=Event%20Management%20(MRes)",
        "desc": "Plan and execute large-scale corporate events, festivals, and conferences."
    },
    {
        "title": "Politics and International Studies with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Politics%20and%20International%20Studies%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study political systems, governance, and global institutions."
    },
    {
        "title": "Psychology with Foundation Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Psychology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Explore the human mind and behavior through scientific methods, clinical research, and cognitive analysis."
    },
    {
        "title": "Game Design and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20and%20Finance%20(BSc)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Dietetics with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dietetics%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Clinical nutrition science, dietary interventions, and public health nutrition."
    },
    {
        "title": "Physical Education with Foundation Year (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Physical%20Education%20with%20Foundation%20Year%20(BSc)",
        "desc": "Train to teach PE and promote physical literacy in school settings."
    },
    {
        "title": "Chemistry with Data Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Chemistry%20with%20Data%20Science%20(MSc)",
        "desc": "Study molecular interactions, organic synthesis, and advanced materials science."
    },
    {
        "title": "Nuclear Engineering (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20(BSc%20Hons)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Illustration with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Illustration%20with%20Study%20Abroad%20(MSc)",
        "desc": "Editorial, children's book, and commercial illustration techniques."
    },
    {
        "title": "Physiotherapy and Management (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Physiotherapy%20and%20Management%20(MSc)",
        "desc": "Physical rehabilitation, musculoskeletal therapy, and movement science."
    },
    {
        "title": "English Language (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20(MA)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Graphic Design (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Graphic%20Design%20(BSc%20Hons)",
        "desc": "Visual communication, branding, typography, and digital media design."
    },
    {
        "title": "History with Sandwich Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "Physical Education (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Physical%20Education%20(MSc)",
        "desc": "Train to teach PE and promote physical literacy in school settings."
    },
    {
        "title": "Linguistics with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Linguistics%20with%20Foundation%20Year%20(BSc)",
        "desc": "The scientific study of language structure, phonetics, syntax, and semantics."
    },
    {
        "title": "Forensic Science and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20and%20International%20Relations%20(BA)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Biomedical Engineering with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Biomedical%20Engineering%20with%20Foundation%20Year%20(BSc)",
        "desc": "Apply engineering principles to medical devices and healthcare technology."
    },
    {
        "title": "Marine Biology with Study Abroad (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20with%20Study%20Abroad%20(MSc)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Business Analytics (MRes)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Analytics%20(MRes)",
        "desc": "Data-driven decision making, business intelligence, and predictive modeling."
    },
    {
        "title": "Pharmacology (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Pharmacology%20(MRes)",
        "desc": "Study how drugs interact with biological systems and treat disease."
    },
    {
        "title": "Music Production (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20(BA)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Microbiology and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20and%20International%20Relations%20(BA)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Food Science (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20(Integrated%20Masters)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Interior Design (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20(BA)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Occupational Therapy (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20(Graduate%20Diploma)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Early Childhood Studies (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Early%20Childhood%20Studies%20(MSc)",
        "desc": "Study child development, early years pedagogy, and childcare policy."
    },
    {
        "title": "Finance (MA)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20(MA)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Education Studies with Data Science (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20with%20Data%20Science%20(MSc)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Optometry and Finance (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20and%20Finance%20(BSc)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Automotive Engineering (Graduate Diploma)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(Graduate%20Diploma)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Genetics with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Genetics%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study DNA, heredity, gene therapy, and genetic engineering technologies."
    },
    {
        "title": "Audiology (MA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20(MA)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Audiology with Professional Placement (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Veterinary Medicine with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20with%20Foundation%20Year%20(BSc)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Neuroscience (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20(Integrated%20Masters)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Data Science (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Data%20Science%20(MA)",
        "desc": "Analyze big data, build machine learning models, and drive data strategy."
    },
    {
        "title": "Economics and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20and%20International%20Relations%20(BA)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "Speech and Language Therapy (MRes)",
        "category": "Healthcare",
        "url": "course-details.html?course=Speech%20and%20Language%20Therapy%20(MRes)",
        "desc": "Diagnose and treat communication, speech, and swallowing disorders."
    },
    {
        "title": "Business Administration (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20(BSc%20Hons)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Artificial Intelligence with Data Science (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20with%20Data%20Science%20(MSc)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Dietetics (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dietetics%20(BSc)",
        "desc": "Clinical nutrition science, dietary interventions, and public health nutrition."
    },
    {
        "title": "Environmental Policy with Data Science (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20with%20Data%20Science%20(MSc)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "Cyber Security and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Cyber%20Security%20and%20Finance%20(BSc)",
        "desc": "Protect networks, systems, and data from digital threats and cyber attacks."
    },
    {
        "title": "Criminology with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Digital Media with Data Science (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20with%20Data%20Science%20(MSc)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Architecture (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20(MA)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Banking with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Banking%20with%20Study%20Abroad%20(MSc)",
        "desc": "Retail and commercial banking, credit risk, and regulatory compliance."
    },
    {
        "title": "Criminology (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20(MSc)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "English Literature and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20and%20Finance%20(BSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Electrical Engineering with Professional Placement (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20with%20Professional%20Placement%20(BSc)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Ecology and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Ecology%20and%20Finance%20(BSc)",
        "desc": "Study ecosystems, biodiversity, and environmental conservation strategies."
    },
    {
        "title": "Nuclear Engineering (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20(MA)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Film and Television (BSc Hons)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20(BSc%20Hons)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Fine Art with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Physics with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20with%20Professional%20Placement%20(BSc)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Marine Biology (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20(Integrated%20Masters)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Neuroscience with Study Abroad (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20with%20Study%20Abroad%20(MSc)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Dentistry with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20with%20Data%20Science%20(MSc)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Adult Nursing and Finance (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Adult%20Nursing%20and%20Finance%20(BSc)",
        "desc": "Clinical nursing care for adult patients across medical and surgical settings."
    },
    {
        "title": "Optometry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20(BA)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Politics and International Studies (Integrated Masters)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Politics%20and%20International%20Studies%20(Integrated%20Masters)",
        "desc": "Study political systems, governance, and global institutions."
    },
    {
        "title": "Blockchain Technology (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20(MRes)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Occupational Therapy (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20(MSc)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Finance with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Environmental Science (Graduate Diploma)",
        "category": "Sciences",
        "url": "course-details.html?course=Environmental%20Science%20(Graduate%20Diploma)",
        "desc": "Address climate change, pollution, and ecological sustainability."
    },
    {
        "title": "Philosophy and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20and%20International%20Relations%20(BA)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Applied Mathematics (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Applied%20Mathematics%20(Integrated%20Masters)",
        "desc": "Mathematical modeling applied to engineering, physics, and finance."
    },
    {
        "title": "Sports Science (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20(MA)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Criminology and Policing (BSc Hons)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20(BSc%20Hons)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Film Studies (BSc Hons)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20(BSc%20Hons)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Pharmacy with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Pharmacy%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study pharmaceutical sciences, drug dispensing, and patient-centered care."
    },
    {
        "title": "Data Science (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Data%20Science%20(MSc)",
        "desc": "Analyze big data, build machine learning models, and drive data strategy."
    },
    {
        "title": "Marketing (MA)",
        "category": "Business",
        "url": "course-details.html?course=Marketing%20(MA)",
        "desc": "Consumer behavior, digital strategy, brand management, and market research."
    },
    {
        "title": "Politics with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20with%20Study%20Abroad%20(MSc)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Film and Television with Foundation Year (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20with%20Foundation%20Year%20(BSc)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Robotics with Study Abroad (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20with%20Study%20Abroad%20(MSc)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Criminology and Policing (MRes)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20(MRes)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Aerospace Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Aerospace%20Engineering%20(BA)",
        "desc": "Design and develop aircraft, spacecraft, and satellite technologies."
    },
    {
        "title": "Robotics with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20with%20Foundation%20Year%20(BSc)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Special Educational Needs with Data Science (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Special%20Educational%20Needs%20with%20Data%20Science%20(MSc)",
        "desc": "Support learners with additional needs, disabilities, and learning differences."
    },
    {
        "title": "Policing with a Year in Industry (BA)",
        "category": "Public Sector",
        "url": "course-details.html?course=Policing%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Law enforcement, forensic investigation, and community public safety."
    },
    {
        "title": "Digital Media (Graduate Diploma)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20(Graduate%20Diploma)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "American Studies (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=American%20Studies%20(MRes)",
        "desc": "Study American history, culture, politics, and literature."
    },
    {
        "title": "Astrophysics and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Astrophysics%20and%20Finance%20(BSc)",
        "desc": "Explore the physical nature of stars, galaxies, dark matter, and the universe."
    },
    {
        "title": "Automotive Engineering and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20and%20International%20Relations%20(BA)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Fine Art with a Year in Industry (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Dentistry (BA Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20(BA%20Hons)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Finance with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20with%20Foundation%20Year%20(BSc)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Primary Education (MRes)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20(MRes)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "International Development (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20(MSc)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "Product Design (MA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20(MA)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Philosophy with Data Science (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20with%20Data%20Science%20(MSc)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Sociology and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20and%20Management%20(MSc)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Urban Planning (Integrated Masters)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20(Integrated%20Masters)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Psychology and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Psychology%20and%20Management%20(MSc)",
        "desc": "Explore the human mind and behavior through scientific methods, clinical research, and cognitive analysis."
    },
    {
        "title": "Animation with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20with%20Study%20Abroad%20(MSc)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Aerospace Engineering (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Aerospace%20Engineering%20(MRes)",
        "desc": "Design and develop aircraft, spacecraft, and satellite technologies."
    },
    {
        "title": "Photography (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20(BSc%20Hons)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Information Technology (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Information%20Technology%20(Integrated%20Masters)",
        "desc": "Manage digital infrastructure, cloud computing, and enterprise networking."
    },
    {
        "title": "Dance (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Dance%20(BSc%20Hons)",
        "desc": "Contemporary dance, choreography, and performing arts practice."
    },
    {
        "title": "Ancient History with Sandwich Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Ancient%20History%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Explore the civilizations of the ancient world from Mesopotamia to Rome."
    },
    {
        "title": "Mental Health Nursing (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20(MSc)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Anthropology with Data Science (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20with%20Data%20Science%20(MSc)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Environmental Engineering and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Environmental%20Engineering%20and%20Finance%20(BSc)",
        "desc": "Design sustainable solutions for water, waste, and pollution control."
    },
    {
        "title": "Politics (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20(Graduate%20Diploma)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Creative Arts with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Creative%20Arts%20with%20Data%20Science%20(MSc)",
        "desc": "Interdisciplinary creative practice across visual and performing arts."
    },
    {
        "title": "Blockchain Technology (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20(Integrated%20Masters)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Dance and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Dance%20and%20Finance%20(BSc)",
        "desc": "Contemporary dance, choreography, and performing arts practice."
    },
    {
        "title": "Nutrition (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Nutrition%20(Integrated%20Masters)",
        "desc": "Study human nutrition, diet science, and public health outcomes."
    },
    {
        "title": "Modern Languages and Management (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20and%20Management%20(MSc)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "Podiatry (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20(Integrated%20Masters)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Early Childhood Studies and Finance (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Early%20Childhood%20Studies%20and%20Finance%20(BSc)",
        "desc": "Study child development, early years pedagogy, and childcare policy."
    },
    {
        "title": "Mathematics and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20and%20International%20Relations%20(BA)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Software Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Software%20Engineering%20(BA)",
        "desc": "Build scalable, production-grade software applications and distributed systems."
    },
    {
        "title": "Education Studies and International Relations (BA)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20and%20International%20Relations%20(BA)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Graphic Design and Management (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Graphic%20Design%20and%20Management%20(MSc)",
        "desc": "Visual communication, branding, typography, and digital media design."
    },
    {
        "title": "Criminology and Policing and International Relations (BA)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20and%20International%20Relations%20(BA)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Business Administration (Integrated Masters)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20(Integrated%20Masters)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Sports Science with Study Abroad (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20with%20Study%20Abroad%20(MSc)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Creative Arts and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Creative%20Arts%20and%20Finance%20(BSc)",
        "desc": "Interdisciplinary creative practice across visual and performing arts."
    },
    {
        "title": "Politics (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20(BSc)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Primary Education with Professional Placement (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20with%20Professional%20Placement%20(BSc)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "Philosophy (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20(MA)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Environmental Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Environmental%20Engineering%20(BA)",
        "desc": "Design sustainable solutions for water, waste, and pollution control."
    },
    {
        "title": "Biomedical Sciences (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20(MSc)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Renewable Energy Engineering (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Renewable%20Energy%20Engineering%20(BSc%20Hons)",
        "desc": "Solar, wind, and hydrogen energy systems design and implementation."
    },
    {
        "title": "Digital Media (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20(BSc)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Forensic Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20(MSc)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Biomedical Engineering with Study Abroad (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Biomedical%20Engineering%20with%20Study%20Abroad%20(MSc)",
        "desc": "Apply engineering principles to medical devices and healthcare technology."
    },
    {
        "title": "Fine Art (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20(Integrated%20Masters)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Marine Biology (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20(BSc)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Urban Planning (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20(MSc)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Economics (BA)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20(BA)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "Media Studies with Professional Placement (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20with%20Professional%20Placement%20(BSc)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Electrical Engineering with Study Abroad (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20with%20Study%20Abroad%20(MSc)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "German (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=German%20(MSc)",
        "desc": "Explore German language, literature, philosophy, and Central European culture."
    },
    {
        "title": "Public Relations (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20(BSc)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Music (BA Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20(BA%20Hons)",
        "desc": "Performance, composition, music technology, and music theory."
    },
    {
        "title": "Speech and Language Therapy (BA Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Speech%20and%20Language%20Therapy%20(BA%20Hons)",
        "desc": "Diagnose and treat communication, speech, and swallowing disorders."
    },
    {
        "title": "Creative Arts (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Creative%20Arts%20(MSc)",
        "desc": "Interdisciplinary creative practice across visual and performing arts."
    },
    {
        "title": "Anthropology with Sandwich Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Sport Coaching (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Sport%20Coaching%20(BSc)",
        "desc": "Develop athletic talent through evidence-based coaching methodologies."
    },
    {
        "title": "Policing with Professional Placement (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Policing%20with%20Professional%20Placement%20(BSc)",
        "desc": "Law enforcement, forensic investigation, and community public safety."
    },
    {
        "title": "Electrical Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20(BA)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Microbiology and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20and%20Finance%20(BSc)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Drama and Theatre Studies (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Drama%20and%20Theatre%20Studies%20(Integrated%20Masters)",
        "desc": "Acting, directing, stage production, and dramatic literature."
    },
    {
        "title": "Software Engineering (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Software%20Engineering%20(Integrated%20Masters)",
        "desc": "Build scalable, production-grade software applications and distributed systems."
    },
    {
        "title": "Nursing with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20with%20Data%20Science%20(MSc)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Genetics (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Genetics%20(Integrated%20Masters)",
        "desc": "Study DNA, heredity, gene therapy, and genetic engineering technologies."
    },
    {
        "title": "Graphic Design with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Graphic%20Design%20with%20Data%20Science%20(MSc)",
        "desc": "Visual communication, branding, typography, and digital media design."
    },
    {
        "title": "Marine Biology (Graduate Diploma)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20(Graduate%20Diploma)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Biomedical Sciences (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20(BSc)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Japanese Studies (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20(BA)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Civil Engineering and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Civil%20Engineering%20and%20Finance%20(BSc)",
        "desc": "Design and build bridges, highways, dams, and essential infrastructure."
    },
    {
        "title": "Primary Education and Finance (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20and%20Finance%20(BSc)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "German (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=German%20(MRes)",
        "desc": "Explore German language, literature, philosophy, and Central European culture."
    },
    {
        "title": "Advertising with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "German with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=German%20with%20Foundation%20Year%20(BSc)",
        "desc": "Explore German language, literature, philosophy, and Central European culture."
    },
    {
        "title": "Hospitality Management and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20and%20International%20Relations%20(BA)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "Sport Coaching (BA Hons)",
        "category": "Education",
        "url": "course-details.html?course=Sport%20Coaching%20(BA%20Hons)",
        "desc": "Develop athletic talent through evidence-based coaching methodologies."
    },
    {
        "title": "Artificial Intelligence (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20(BSc%20Hons)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Interior Design and Management (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20and%20Management%20(MSc)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Hospitality Management (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20(BSc%20Hons)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "Geography (MA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20(MA)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Forensic Science (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20(BA%20Hons)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Nutrition (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Nutrition%20(BSc%20Hons)",
        "desc": "Study human nutrition, diet science, and public health outcomes."
    },
    {
        "title": "Social Policy with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Social%20Policy%20with%20Professional%20Placement%20(BSc)",
        "desc": "Examine welfare systems, public health policy, and social inequality."
    },
    {
        "title": "Real Estate with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20with%20Data%20Science%20(MSc)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Publishing with Foundation Year (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20with%20Foundation%20Year%20(BSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Creative Arts (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Creative%20Arts%20(Integrated%20Masters)",
        "desc": "Interdisciplinary creative practice across visual and performing arts."
    },
    {
        "title": "Advertising (MRes)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20(MRes)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Biomedical Science with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Biomedical%20Science%20with%20Data%20Science%20(MSc)",
        "desc": "Laboratory diagnosis, blood sciences, and clinical pathology."
    },
    {
        "title": "Pharmacy (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Pharmacy%20(BSc%20Hons)",
        "desc": "Study pharmaceutical sciences, drug dispensing, and patient-centered care."
    },
    {
        "title": "Hospitality Management (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20(Graduate%20Diploma)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "Audiology (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20(BSc%20Hons)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Civil Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Civil%20Engineering%20(BA)",
        "desc": "Design and build bridges, highways, dams, and essential infrastructure."
    },
    {
        "title": "Software Engineering with Sandwich Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Software%20Engineering%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Build scalable, production-grade software applications and distributed systems."
    },
    {
        "title": "Forensic Science with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Primary Education (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Primary%20Education%20(MSc)",
        "desc": "Train to teach and inspire children aged 5-11 across the national curriculum."
    },
    {
        "title": "Advertising (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20(Graduate%20Diploma)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Software Engineering (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Software%20Engineering%20(MSc)",
        "desc": "Build scalable, production-grade software applications and distributed systems."
    },
    {
        "title": "English Literature with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20with%20Study%20Abroad%20(MSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Policing with Study Abroad (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Policing%20with%20Study%20Abroad%20(MSc)",
        "desc": "Law enforcement, forensic investigation, and community public safety."
    },
    {
        "title": "Marine Engineering with Professional Placement (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20with%20Professional%20Placement%20(BSc)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Sociology (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20(MSc)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Environmental Policy with Study Abroad (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20with%20Study%20Abroad%20(MSc)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "Automotive Engineering (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(BSc)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Biomedical Sciences (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20(MA)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Psychology (BSc Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Psychology%20(BSc%20Hons)",
        "desc": "Explore the human mind and behavior through scientific methods, clinical research, and cognitive analysis."
    },
    {
        "title": "Geography and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20and%20Management%20(MSc)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Games Technology (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20(BSc)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Applied Mathematics and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Applied%20Mathematics%20and%20Finance%20(BSc)",
        "desc": "Mathematical modeling applied to engineering, physics, and finance."
    },
    {
        "title": "Publishing with Study Abroad (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20with%20Study%20Abroad%20(MSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Youth Work with Sandwich Year (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Youth%20Work%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Engage and empower young people through community programs and support."
    },
    {
        "title": "Product Design with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20with%20Professional%20Placement%20(BSc)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "German (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=German%20(BSc)",
        "desc": "Explore German language, literature, philosophy, and Central European culture."
    },
    {
        "title": "Information Technology and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Information%20Technology%20and%20Management%20(MSc)",
        "desc": "Manage digital infrastructure, cloud computing, and enterprise networking."
    },
    {
        "title": "Real Estate with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Ancient History (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=Ancient%20History%20(Graduate%20Diploma)",
        "desc": "Explore the civilizations of the ancient world from Mesopotamia to Rome."
    },
    {
        "title": "Music with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20with%20Professional%20Placement%20(BSc)",
        "desc": "Performance, composition, music technology, and music theory."
    },
    {
        "title": "Dentistry (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20(BSc%20Hons)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Biochemistry (Graduate Diploma)",
        "category": "Sciences",
        "url": "course-details.html?course=Biochemistry%20(Graduate%20Diploma)",
        "desc": "Explore the chemical processes and molecular mechanisms within living organisms."
    },
    {
        "title": "Forensic Psychology (MRes)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20(MRes)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Animation with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20with%20Foundation%20Year%20(BSc)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Philosophy and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20and%20Finance%20(BSc)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Public Relations with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Mental Health Nursing (MRes)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20(MRes)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Fine Art (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20(BSc%20Hons)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Business Administration and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20and%20International%20Relations%20(BA)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Photography (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20(MSc)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Automotive Engineering with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Politics and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Politics%20and%20Finance%20(BSc)",
        "desc": "Study global governance, diplomacy, elections, and political systems."
    },
    {
        "title": "Architecture and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20and%20International%20Relations%20(BA)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Modern Languages and International Relations (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20and%20International%20Relations%20(BA)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "Youth Work with Foundation Year (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Youth%20Work%20with%20Foundation%20Year%20(BSc)",
        "desc": "Engage and empower young people through community programs and support."
    },
    {
        "title": "Architecture with Study Abroad (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20with%20Study%20Abroad%20(MSc)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Renewable Energy Engineering and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Renewable%20Energy%20Engineering%20and%20Finance%20(BSc)",
        "desc": "Solar, wind, and hydrogen energy systems design and implementation."
    },
    {
        "title": "Biomedical Science with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Biomedical%20Science%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Laboratory diagnosis, blood sciences, and clinical pathology."
    },
    {
        "title": "Sports Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20(MSc)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Teaching English as a Foreign Language (BA Hons)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20(BA%20Hons)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Public Relations (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20(MSc)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Aerospace Engineering (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Aerospace%20Engineering%20(Integrated%20Masters)",
        "desc": "Design and develop aircraft, spacecraft, and satellite technologies."
    },
    {
        "title": "Cyber Security with Data Science (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Cyber%20Security%20with%20Data%20Science%20(MSc)",
        "desc": "Protect networks, systems, and data from digital threats and cyber attacks."
    },
    {
        "title": "Textile Design (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Textile%20Design%20(BSc%20Hons)",
        "desc": "Fabric printing, weaving, sustainable textiles, and surface design."
    },
    {
        "title": "Renewable Energy Engineering with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Renewable%20Energy%20Engineering%20with%20Foundation%20Year%20(BSc)",
        "desc": "Solar, wind, and hydrogen energy systems design and implementation."
    },
    {
        "title": "Physics and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20and%20Finance%20(BSc)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Geography (MRes)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20(MRes)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Product Design (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20(Integrated%20Masters)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Biomedical Sciences with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Project Management (MA)",
        "category": "Business",
        "url": "course-details.html?course=Project%20Management%20(MA)",
        "desc": "Agile methodologies, risk management, and delivering complex projects on time."
    },
    {
        "title": "Fashion Design with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Veterinary Medicine (MRes)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20(MRes)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Nuclear Engineering and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20and%20International%20Relations%20(BA)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Occupational Therapy with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20with%20Data%20Science%20(MSc)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Philosophy (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20(Graduate%20Diploma)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "History (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20(MRes)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "International Business (Integrated Masters)",
        "category": "Business",
        "url": "course-details.html?course=International%20Business%20(Integrated%20Masters)",
        "desc": "Global trade, cross-border strategy, supply chain, and international markets."
    },
    {
        "title": "Music Production (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20(Integrated%20Masters)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Illustration (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Illustration%20(BA)",
        "desc": "Editorial, children's book, and commercial illustration techniques."
    },
    {
        "title": "Advertising with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20with%20Study%20Abroad%20(MSc)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Event Management (MA)",
        "category": "Business",
        "url": "course-details.html?course=Event%20Management%20(MA)",
        "desc": "Plan and execute large-scale corporate events, festivals, and conferences."
    },
    {
        "title": "Renewable Energy Engineering (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Renewable%20Energy%20Engineering%20(Integrated%20Masters)",
        "desc": "Solar, wind, and hydrogen energy systems design and implementation."
    },
    {
        "title": "Social Work with Professional Placement (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Social%20Work%20with%20Professional%20Placement%20(BSc)",
        "desc": "Support vulnerable individuals, families, and communities through intervention."
    },
    {
        "title": "Podiatry and Finance (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20and%20Finance%20(BSc)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Supply Chain Management (BA)",
        "category": "Business",
        "url": "course-details.html?course=Supply%20Chain%20Management%20(BA)",
        "desc": "Logistics, procurement, operations management, and global supply networks."
    },
    {
        "title": "Architecture (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20(BSc%20Hons)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Artificial Intelligence (Graduate Diploma)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20(Graduate%20Diploma)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Microbiology (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20(BA)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Fashion Design with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20with%20Data%20Science%20(MSc)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Physics with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Geology and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Geology%20and%20Finance%20(BSc)",
        "desc": "Study the earth's physical structure, minerals, tectonics, and natural resources."
    },
    {
        "title": "Journalism with Professional Placement (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20with%20Professional%20Placement%20(BSc)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "Game Design with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20with%20Professional%20Placement%20(BSc)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Midwifery with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Midwifery%20with%20Study%20Abroad%20(MSc)",
        "desc": "Care for women during pregnancy, childbirth, and the postpartum period."
    },
    {
        "title": "Web Development and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20and%20Management%20(MSc)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Actuarial Science (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Actuarial%20Science%20(BA%20Hons)",
        "desc": "Apply mathematics and statistics to assess financial risk and uncertainty."
    },
    {
        "title": "Podiatry with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20with%20Foundation%20Year%20(BSc)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Marine Engineering and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20and%20Finance%20(BSc)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Physical Education with Data Science (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Physical%20Education%20with%20Data%20Science%20(MSc)",
        "desc": "Train to teach PE and promote physical literacy in school settings."
    },
    {
        "title": "Occupational Therapy with Professional Placement (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20with%20Professional%20Placement%20(BSc)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Accounting with Sandwich Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Accounting%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."
    },
    {
        "title": "Secondary Education (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20(MSc)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "Publishing (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20(BSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Special Educational Needs and International Relations (BA)",
        "category": "Education",
        "url": "course-details.html?course=Special%20Educational%20Needs%20and%20International%20Relations%20(BA)",
        "desc": "Support learners with additional needs, disabilities, and learning differences."
    },
    {
        "title": "Fashion Design (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20(MSc)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Education Studies (Integrated Masters)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20(Integrated%20Masters)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Microbiology (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20(BA%20Hons)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Nursing with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Criminology and Policing with Study Abroad (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20with%20Study%20Abroad%20(MSc)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Nursing (MA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20(MA)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Publishing (BA)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20(BA)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Modern Languages (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20(BA)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "Actuarial Science (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Actuarial%20Science%20(MA)",
        "desc": "Apply mathematics and statistics to assess financial risk and uncertainty."
    },
    {
        "title": "Cyber Security (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Cyber%20Security%20(BSc%20Hons)",
        "desc": "Protect networks, systems, and data from digital threats and cyber attacks."
    },
    {
        "title": "Criminology and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20and%20Management%20(MSc)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Dance and Management (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Dance%20and%20Management%20(MSc)",
        "desc": "Contemporary dance, choreography, and performing arts practice."
    },
    {
        "title": "Anthropology (Integrated Masters)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20(Integrated%20Masters)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Speech and Language Therapy (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Speech%20and%20Language%20Therapy%20(BSc)",
        "desc": "Diagnose and treat communication, speech, and swallowing disorders."
    },
    {
        "title": "Tourism Management with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Tourism%20Management%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Destination management, sustainable tourism, and leisure industry operations."
    },
    {
        "title": "Veterinary Medicine with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Astrophysics (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Astrophysics%20(MRes)",
        "desc": "Explore the physical nature of stars, galaxies, dark matter, and the universe."
    },
    {
        "title": "Japanese Studies (BA Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20(BA%20Hons)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Sport Coaching and Finance (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Sport%20Coaching%20and%20Finance%20(BSc)",
        "desc": "Develop athletic talent through evidence-based coaching methodologies."
    },
    {
        "title": "Photography (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20(Integrated%20Masters)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Dentistry with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20with%20Foundation%20Year%20(BSc)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Product Design (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20(MSc)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Biomedical Sciences with Data Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20with%20Data%20Science%20(MSc)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Finance with Sandwich Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Biology and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biology%20and%20Finance%20(BSc)",
        "desc": "Study living organisms, ecology, evolution, and molecular biology."
    },
    {
        "title": "Games Technology with Professional Placement (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Modern Languages (BA Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20(BA%20Hons)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "Chinese Studies (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=Chinese%20Studies%20(MRes)",
        "desc": "Mandarin language proficiency combined with East Asian history and politics."
    },
    {
        "title": "Jewellery Design with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20with%20Study%20Abroad%20(MSc)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Economics (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20(BA%20Hons)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "English Language with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20with%20Study%20Abroad%20(MSc)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Human Resource Management with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Human%20Resource%20Management%20with%20Study%20Abroad%20(MSc)",
        "desc": "Manage talent, recruitment, organizational behavior, and employment law."
    },
    {
        "title": "Disaster Management (Graduate Diploma)",
        "category": "Public Sector",
        "url": "course-details.html?course=Disaster%20Management%20(Graduate%20Diploma)",
        "desc": "Emergency planning, crisis response, and humanitarian coordination."
    },
    {
        "title": "Broadcasting (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Broadcasting%20(MSc)",
        "desc": "Radio and television production, live broadcasting, and media technology."
    },
    {
        "title": "Politics and International Studies (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Politics%20and%20International%20Studies%20(MSc)",
        "desc": "Study political systems, governance, and global institutions."
    },
    {
        "title": "Retail Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20(MSc)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Electrical Engineering with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20with%20Foundation%20Year%20(BSc)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Philosophy with Sandwich Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Philosophy%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Explore fundamental questions of existence, ethics, logic, and epistemology."
    },
    {
        "title": "Environmental Science with Data Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Environmental%20Science%20with%20Data%20Science%20(MSc)",
        "desc": "Address climate change, pollution, and ecological sustainability."
    },
    {
        "title": "Environmental Policy and Finance (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20and%20Finance%20(BSc)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "Disaster Management with a Year in Industry (BA)",
        "category": "Public Sector",
        "url": "course-details.html?course=Disaster%20Management%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Emergency planning, crisis response, and humanitarian coordination."
    },
    {
        "title": "French (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=French%20(BSc%20Hons)",
        "desc": "Master French language, literature, cinema, and Francophone cultures."
    },
    {
        "title": "Interior Design (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20(BSc%20Hons)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "French (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=French%20(Integrated%20Masters)",
        "desc": "Master French language, literature, cinema, and Francophone cultures."
    },
    {
        "title": "Biochemistry (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biochemistry%20(MSc)",
        "desc": "Explore the chemical processes and molecular mechanisms within living organisms."
    },
    {
        "title": "Neuroscience (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20(BSc%20Hons)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Public Relations and Finance (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20and%20Finance%20(BSc)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Dietetics (MA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dietetics%20(MA)",
        "desc": "Clinical nutrition science, dietary interventions, and public health nutrition."
    },
    {
        "title": "Project Management (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Project%20Management%20(BSc%20Hons)",
        "desc": "Agile methodologies, risk management, and delivering complex projects on time."
    },
    {
        "title": "Music Production (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20(BSc%20Hons)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Graphic Design with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Graphic%20Design%20with%20Study%20Abroad%20(MSc)",
        "desc": "Visual communication, branding, typography, and digital media design."
    },
    {
        "title": "Zoology (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Zoology%20(BSc)",
        "desc": "Study animal biology, behavior, ecology, and wildlife conservation."
    },
    {
        "title": "Digital Media (BA)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20(BA)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Banking with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Banking%20with%20Data%20Science%20(MSc)",
        "desc": "Retail and commercial banking, credit risk, and regulatory compliance."
    },
    {
        "title": "Jewellery Design with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20with%20Professional%20Placement%20(BSc)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Chemical Engineering with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Chemical%20Engineering%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Industrial process design, material synthesis, and sustainable manufacturing."
    },
    {
        "title": "Speech and Language Therapy with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Speech%20and%20Language%20Therapy%20with%20Foundation%20Year%20(BSc)",
        "desc": "Diagnose and treat communication, speech, and swallowing disorders."
    },
    {
        "title": "Japanese Studies with a Year in Industry (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Finance (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20(MSc)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Actuarial Science (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Actuarial%20Science%20(BSc%20Hons)",
        "desc": "Apply mathematics and statistics to assess financial risk and uncertainty."
    },
    {
        "title": "Social Work and Management (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Social%20Work%20and%20Management%20(MSc)",
        "desc": "Support vulnerable individuals, families, and communities through intervention."
    },
    {
        "title": "Fine Art with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20with%20Foundation%20Year%20(BSc)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Neuroscience (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20(MA)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Spanish with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20with%20Foundation%20Year%20(BSc)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Dance with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Dance%20with%20Professional%20Placement%20(BSc)",
        "desc": "Contemporary dance, choreography, and performing arts practice."
    },
    {
        "title": "Digital Media with Study Abroad (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20with%20Study%20Abroad%20(MSc)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Electrical Engineering with Sandwich Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Marketing (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Marketing%20(BSc%20Hons)",
        "desc": "Consumer behavior, digital strategy, brand management, and market research."
    },
    {
        "title": "Sociology with Foundation Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Web Development (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20(MSc)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Archaeology (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=Archaeology%20(MA)",
        "desc": "Investigate past cultures through material remains and fieldwork excavation."
    },
    {
        "title": "Film and Television with Data Science (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20with%20Data%20Science%20(MSc)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "English Literature (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20(BSc)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Anthropology with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Film Studies (Graduate Diploma)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20(Graduate%20Diploma)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Creative Writing (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=Creative%20Writing%20(MRes)",
        "desc": "Develop fiction, poetry, screenwriting, and non-fiction storytelling skills."
    },
    {
        "title": "Nursing (MRes)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20(MRes)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Nursing with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20with%20Study%20Abroad%20(MSc)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Accounting with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Accounting%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."
    },
    {
        "title": "International Relations (Integrated Masters)",
        "category": "Social Sciences",
        "url": "course-details.html?course=International%20Relations%20(Integrated%20Masters)",
        "desc": "Analyze global diplomacy, conflict resolution, and foreign policy frameworks."
    },
    {
        "title": "Human Resource Management with Professional Placement (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Human%20Resource%20Management%20with%20Professional%20Placement%20(BSc)",
        "desc": "Manage talent, recruitment, organizational behavior, and employment law."
    },
    {
        "title": "Robotics (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20(MSc)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Statistics and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Statistics%20and%20Finance%20(BSc)",
        "desc": "Advanced statistical theory, probability, and data analysis methods."
    },
    {
        "title": "Policing and Management (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Policing%20and%20Management%20(MSc)",
        "desc": "Law enforcement, forensic investigation, and community public safety."
    },
    {
        "title": "Neuroscience and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20and%20International%20Relations%20(BA)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Mathematics (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20(BSc%20Hons)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Public Relations (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20(BSc%20Hons)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Robotics (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Robotics%20(MA)",
        "desc": "Design autonomous systems, mechatronics, and industrial automation."
    },
    {
        "title": "Geography (Graduate Diploma)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20(Graduate%20Diploma)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Spanish with a Year in Industry (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Publishing with Sandwich Year (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Film and Television (Graduate Diploma)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20(Graduate%20Diploma)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Drama and Theatre Studies with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Drama%20and%20Theatre%20Studies%20with%20Study%20Abroad%20(MSc)",
        "desc": "Acting, directing, stage production, and dramatic literature."
    },
    {
        "title": "Child Psychology (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Child%20Psychology%20(BSc)",
        "desc": "Study cognitive, emotional, and social development from infancy to adolescence."
    },
    {
        "title": "Linguistics (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=Linguistics%20(Integrated%20Masters)",
        "desc": "The scientific study of language structure, phonetics, syntax, and semantics."
    },
    {
        "title": "Radiography with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20with%20Data%20Science%20(MSc)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Pharmacy and Management (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Pharmacy%20and%20Management%20(MSc)",
        "desc": "Study pharmaceutical sciences, drug dispensing, and patient-centered care."
    },
    {
        "title": "Human Resource Management with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Human%20Resource%20Management%20with%20Foundation%20Year%20(BSc)",
        "desc": "Manage talent, recruitment, organizational behavior, and employment law."
    },
    {
        "title": "Biology (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biology%20(BSc)",
        "desc": "Study living organisms, ecology, evolution, and molecular biology."
    },
    {
        "title": "Actuarial Science (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Actuarial%20Science%20(BSc)",
        "desc": "Apply mathematics and statistics to assess financial risk and uncertainty."
    },
    {
        "title": "Radiography with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Nursing with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Nursing%20with%20Foundation%20Year%20(BSc)",
        "desc": "Provide frontline clinical care, patient assessment, and holistic support across specialties."
    },
    {
        "title": "Real Estate (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20(MSc)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Environmental Policy with a Year in Industry (BA)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "Paramedic Science (MRes)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20(MRes)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Physiotherapy (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Physiotherapy%20(MSc)",
        "desc": "Physical rehabilitation, musculoskeletal therapy, and movement science."
    },
    {
        "title": "Fine Art (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20(BA)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Fashion Design (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20(BSc%20Hons)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Physics (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20(MA)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Sociology with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Sociology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Examine society, human behavior, social structures, inequality, and institutional change."
    },
    {
        "title": "Renewable Energy Engineering (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Renewable%20Energy%20Engineering%20(BA%20Hons)",
        "desc": "Solar, wind, and hydrogen energy systems design and implementation."
    },
    {
        "title": "Product Design with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20with%20Foundation%20Year%20(BSc)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Marketing (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Marketing%20(BA%20Hons)",
        "desc": "Consumer behavior, digital strategy, brand management, and market research."
    },
    {
        "title": "Anthropology and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20and%20Management%20(MSc)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Environmental Policy (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Environmental%20Policy%20(BSc)",
        "desc": "Climate legislation, green policy development, and sustainability governance."
    },
    {
        "title": "American Studies and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=American%20Studies%20and%20Finance%20(BSc)",
        "desc": "Study American history, culture, politics, and literature."
    },
    {
        "title": "Event Management (BA)",
        "category": "Business",
        "url": "course-details.html?course=Event%20Management%20(BA)",
        "desc": "Plan and execute large-scale corporate events, festivals, and conferences."
    },
    {
        "title": "International Relations (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=International%20Relations%20(BA)",
        "desc": "Analyze global diplomacy, conflict resolution, and foreign policy frameworks."
    },
    {
        "title": "Games Technology and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20and%20International%20Relations%20(BA)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Game Design and International Relations (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20and%20International%20Relations%20(BA)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Teaching English as a Foreign Language with Data Science (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20with%20Data%20Science%20(MSc)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Retail Management with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20with%20Data%20Science%20(MSc)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Jewellery Design with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Advertising (MA)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20(MA)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Drama and Theatre Studies (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Drama%20and%20Theatre%20Studies%20(BSc%20Hons)",
        "desc": "Acting, directing, stage production, and dramatic literature."
    },
    {
        "title": "Chemistry (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Chemistry%20(BSc)",
        "desc": "Study molecular interactions, organic synthesis, and advanced materials science."
    },
    {
        "title": "Jewellery Design (Graduate Diploma)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20(Graduate%20Diploma)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Accounting (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Accounting%20(MSc)",
        "desc": "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."
    },
    {
        "title": "English Language (BA Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20(BA%20Hons)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Interior Design (MRes)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20(MRes)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Cloud Computing and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Cloud%20Computing%20and%20Management%20(MSc)",
        "desc": "AWS, Azure, and GCP infrastructure design and DevOps engineering."
    },
    {
        "title": "Forensic Psychology with a Year in Industry (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Business Analytics with Professional Placement (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Analytics%20with%20Professional%20Placement%20(BSc)",
        "desc": "Data-driven decision making, business intelligence, and predictive modeling."
    },
    {
        "title": "Hospitality Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20(MSc)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "Retail Management (Integrated Masters)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20(Integrated%20Masters)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Business Analytics with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Analytics%20with%20Data%20Science%20(MSc)",
        "desc": "Data-driven decision making, business intelligence, and predictive modeling."
    },
    {
        "title": "Electrical Engineering with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Marine Engineering (BSc Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20(BSc%20Hons)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Blockchain Technology (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20(BA%20Hons)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Mechanical Engineering (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20(MA)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "Automotive Engineering (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(MRes)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Public Relations with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20with%20Foundation%20Year%20(BSc)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Advertising with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20with%20Foundation%20Year%20(BSc)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "Electrical Engineering (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20(MSc)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Paramedic Science with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Economics (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Economics%20(BSc)",
        "desc": "Analyze markets, monetary policy, econometrics, and global financial structures."
    },
    {
        "title": "Podiatry and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20and%20International%20Relations%20(BA)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Marine Biology with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20with%20Professional%20Placement%20(BSc)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Psychology with Data Science (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Psychology%20with%20Data%20Science%20(MSc)",
        "desc": "Explore the human mind and behavior through scientific methods, clinical research, and cognitive analysis."
    },
    {
        "title": "Architecture (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20(MSc)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Textile Design (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Textile%20Design%20(BSc)",
        "desc": "Fabric printing, weaving, sustainable textiles, and surface design."
    },
    {
        "title": "Criminology and Policing with Data Science (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20with%20Data%20Science%20(MSc)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Journalism (MRes)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20(MRes)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "Public Relations and Communications with Professional Placement (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20with%20Professional%20Placement%20(BSc)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Urban Planning (BSc Hons)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20(BSc%20Hons)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Secondary Education (BA Hons)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20(BA%20Hons)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "Statistics (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Statistics%20(MSc)",
        "desc": "Advanced statistical theory, probability, and data analysis methods."
    },
    {
        "title": "Biology (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Biology%20(BA%20Hons)",
        "desc": "Study living organisms, ecology, evolution, and molecular biology."
    },
    {
        "title": "Paramedic Science with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Microbiology (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20(MA)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "English Language (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20(BSc%20Hons)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Software Engineering (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Software%20Engineering%20(MRes)",
        "desc": "Build scalable, production-grade software applications and distributed systems."
    },
    {
        "title": "Media Studies and Management (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20and%20Management%20(MSc)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Fine Art with Data Science (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20with%20Data%20Science%20(MSc)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Microbiology with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Zoology and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Zoology%20and%20Finance%20(BSc)",
        "desc": "Study animal biology, behavior, ecology, and wildlife conservation."
    },
    {
        "title": "Jewellery Design and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20and%20Finance%20(BSc)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Photography (BA Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Photography%20(BA%20Hons)",
        "desc": "Master digital and analog photographic techniques and visual storytelling."
    },
    {
        "title": "Hospitality Management (MA)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20(MA)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "History and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=History%20and%20Finance%20(BSc)",
        "desc": "Study human events, civilizations, and societal evolution across eras and continents."
    },
    {
        "title": "Retail Management with Foundation Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20with%20Foundation%20Year%20(BSc)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Artificial Intelligence (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20(MSc)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Advertising (BA)",
        "category": "Business",
        "url": "course-details.html?course=Advertising%20(BA)",
        "desc": "Creative campaigns, media buying, digital advertising, and consumer psychology."
    },
    {
        "title": "English Language with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20with%20Foundation%20Year%20(BSc)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "International Business and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=International%20Business%20and%20International%20Relations%20(BA)",
        "desc": "Global trade, cross-border strategy, supply chain, and international markets."
    },
    {
        "title": "Dance (Graduate Diploma)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Dance%20(Graduate%20Diploma)",
        "desc": "Contemporary dance, choreography, and performing arts practice."
    },
    {
        "title": "Project Management with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Project%20Management%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Agile methodologies, risk management, and delivering complex projects on time."
    },
    {
        "title": "Interior Design (Integrated Masters)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20(Integrated%20Masters)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Optometry with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20with%20Study%20Abroad%20(MSc)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Music and International Relations (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20and%20International%20Relations%20(BA)",
        "desc": "Performance, composition, music technology, and music theory."
    },
    {
        "title": "German (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=German%20(Graduate%20Diploma)",
        "desc": "Explore German language, literature, philosophy, and Central European culture."
    },
    {
        "title": "Zoology (MA)",
        "category": "Sciences",
        "url": "course-details.html?course=Zoology%20(MA)",
        "desc": "Study animal biology, behavior, ecology, and wildlife conservation."
    },
    {
        "title": "Modern Languages with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Modern%20Languages%20with%20Foundation%20Year%20(BSc)",
        "desc": "Master foreign languages and study global cultures, translation, and diplomacy."
    },
    {
        "title": "Biomedical Science (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Biomedical%20Science%20(BSc)",
        "desc": "Laboratory diagnosis, blood sciences, and clinical pathology."
    },
    {
        "title": "Mental Health Nursing (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20(Graduate%20Diploma)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Mechanical Engineering and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20and%20Finance%20(BSc)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "Ecology (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Ecology%20(Integrated%20Masters)",
        "desc": "Study ecosystems, biodiversity, and environmental conservation strategies."
    },
    {
        "title": "Physiotherapy with Foundation Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Physiotherapy%20with%20Foundation%20Year%20(BSc)",
        "desc": "Physical rehabilitation, musculoskeletal therapy, and movement science."
    },
    {
        "title": "Game Design (BSc Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20(BSc%20Hons)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Optometry with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Supply Chain Management with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Supply%20Chain%20Management%20with%20Study%20Abroad%20(MSc)",
        "desc": "Logistics, procurement, operations management, and global supply networks."
    },
    {
        "title": "Biomedical Engineering (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Biomedical%20Engineering%20(MA)",
        "desc": "Apply engineering principles to medical devices and healthcare technology."
    },
    {
        "title": "Public Relations and Communications (BA Hons)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20(BA%20Hons)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Environmental Science (BA Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Environmental%20Science%20(BA%20Hons)",
        "desc": "Address climate change, pollution, and ecological sustainability."
    },
    {
        "title": "Cloud Computing and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Cloud%20Computing%20and%20International%20Relations%20(BA)",
        "desc": "AWS, Azure, and GCP infrastructure design and DevOps engineering."
    },
    {
        "title": "Occupational Therapy and Management (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20and%20Management%20(MSc)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Zoology with Sandwich Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Zoology%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study animal biology, behavior, ecology, and wildlife conservation."
    },
    {
        "title": "Supply Chain Management and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Supply%20Chain%20Management%20and%20International%20Relations%20(BA)",
        "desc": "Logistics, procurement, operations management, and global supply networks."
    },
    {
        "title": "Spanish (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20(BSc)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Food Science with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Fine Art with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fine%20Art%20with%20Study%20Abroad%20(MSc)",
        "desc": "Develop creative practice across painting, sculpture, and mixed media."
    },
    {
        "title": "Policing (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Policing%20(MSc)",
        "desc": "Law enforcement, forensic investigation, and community public safety."
    },
    {
        "title": "Dance with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Dance%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Contemporary dance, choreography, and performing arts practice."
    },
    {
        "title": "Mechanical Engineering (Graduate Diploma)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20(Graduate%20Diploma)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "Youth Work with Study Abroad (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Youth%20Work%20with%20Study%20Abroad%20(MSc)",
        "desc": "Engage and empower young people through community programs and support."
    },
    {
        "title": "Criminology with Foundation Year (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Criminology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Understand crime, criminal justice systems, policing, and their societal impact."
    },
    {
        "title": "Disaster Management (BA Hons)",
        "category": "Public Sector",
        "url": "course-details.html?course=Disaster%20Management%20(BA%20Hons)",
        "desc": "Emergency planning, crisis response, and humanitarian coordination."
    },
    {
        "title": "Physics (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20(MRes)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Theology with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Theology%20with%20Foundation%20Year%20(BSc)",
        "desc": "Study world religions, beliefs, sacred texts, and theological ethics."
    },
    {
        "title": "Finance and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20and%20International%20Relations%20(BA)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Adult Nursing (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Adult%20Nursing%20(BSc%20Hons)",
        "desc": "Clinical nursing care for adult patients across medical and surgical settings."
    },
    {
        "title": "Adult Nursing (BA Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Adult%20Nursing%20(BA%20Hons)",
        "desc": "Clinical nursing care for adult patients across medical and surgical settings."
    },
    {
        "title": "Chinese Studies with Foundation Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Chinese%20Studies%20with%20Foundation%20Year%20(BSc)",
        "desc": "Mandarin language proficiency combined with East Asian history and politics."
    },
    {
        "title": "Dentistry (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20(Graduate%20Diploma)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Environmental Science and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Environmental%20Science%20and%20International%20Relations%20(BA)",
        "desc": "Address climate change, pollution, and ecological sustainability."
    },
    {
        "title": "Podiatry with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Jewellery Design (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20(BA)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "American Studies (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=American%20Studies%20(BSc)",
        "desc": "Study American history, culture, politics, and literature."
    },
    {
        "title": "Audiology with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Tourism Management (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Tourism%20Management%20(BSc%20Hons)",
        "desc": "Destination management, sustainable tourism, and leisure industry operations."
    },
    {
        "title": "Public Health (Graduate Diploma)",
        "category": "Healthcare",
        "url": "course-details.html?course=Public%20Health%20(Graduate%20Diploma)",
        "desc": "Epidemiology, health promotion, and population-level disease prevention."
    },
    {
        "title": "Music Production with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20with%20Professional%20Placement%20(BSc)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Linguistics (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Linguistics%20(MSc)",
        "desc": "The scientific study of language structure, phonetics, syntax, and semantics."
    },
    {
        "title": "Publishing and Finance (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Publishing%20and%20Finance%20(BSc)",
        "desc": "Editorial processes, book publishing, and digital content distribution."
    },
    {
        "title": "Biomedical Engineering (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Biomedical%20Engineering%20(Integrated%20Masters)",
        "desc": "Apply engineering principles to medical devices and healthcare technology."
    },
    {
        "title": "Urban Planning (BA Hons)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20(BA%20Hons)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Anthropology (MRes)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20(MRes)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Insurance (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Insurance%20(BSc%20Hons)",
        "desc": "Actuarial principles, underwriting, risk assessment, and claims management."
    },
    {
        "title": "Geography with Professional Placement (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20with%20Professional%20Placement%20(BSc)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Banking with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Banking%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Retail and commercial banking, credit risk, and regulatory compliance."
    },
    {
        "title": "Policing (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Policing%20(BSc)",
        "desc": "Law enforcement, forensic investigation, and community public safety."
    },
    {
        "title": "Game Design with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Event Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Event%20Management%20(MSc)",
        "desc": "Plan and execute large-scale corporate events, festivals, and conferences."
    },
    {
        "title": "Food Science and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20and%20Management%20(MSc)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Real Estate (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20(Graduate%20Diploma)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Chinese Studies (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Chinese%20Studies%20(BA)",
        "desc": "Mandarin language proficiency combined with East Asian history and politics."
    },
    {
        "title": "Social Work and International Relations (BA)",
        "category": "Public Sector",
        "url": "course-details.html?course=Social%20Work%20and%20International%20Relations%20(BA)",
        "desc": "Support vulnerable individuals, families, and communities through intervention."
    },
    {
        "title": "Project Management (Integrated Masters)",
        "category": "Business",
        "url": "course-details.html?course=Project%20Management%20(Integrated%20Masters)",
        "desc": "Agile methodologies, risk management, and delivering complex projects on time."
    },
    {
        "title": "American Studies with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=American%20Studies%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study American history, culture, politics, and literature."
    },
    {
        "title": "Geography with Study Abroad (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Geography%20with%20Study%20Abroad%20(MSc)",
        "desc": "Physical earth sciences combined with human environment studies and spatial analysis."
    },
    {
        "title": "Sports Science with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Sports%20Science%20with%20Professional%20Placement%20(BSc)",
        "desc": "The study of human performance, exercise physiology, and sports nutrition."
    },
    {
        "title": "Music Production and International Relations (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20and%20International%20Relations%20(BA)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Aerospace Engineering (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Aerospace%20Engineering%20(BA%20Hons)",
        "desc": "Design and develop aircraft, spacecraft, and satellite technologies."
    },
    {
        "title": "Nuclear Engineering and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20and%20Management%20(MSc)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Finance with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20with%20Data%20Science%20(MSc)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Theology with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Theology%20with%20Study%20Abroad%20(MSc)",
        "desc": "Study world religions, beliefs, sacred texts, and theological ethics."
    },
    {
        "title": "Product Design with Sandwich Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Product%20Design%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Conceptualize, prototype, and manufacture consumer goods and industrial products."
    },
    {
        "title": "Business Administration with Sandwich Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Teaching English as a Foreign Language (Integrated Masters)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20(Integrated%20Masters)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Japanese Studies with Sandwich Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Marine Biology and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Marine%20Biology%20and%20International%20Relations%20(BA)",
        "desc": "Examine ocean ecosystems, marine organisms, and coastal conservation."
    },
    {
        "title": "Teaching English as a Foreign Language with Sandwich Year (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Children's Nursing (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Children's%20Nursing%20(MSc)",
        "desc": "Specialist nursing care for infants, children, and young people."
    },
    {
        "title": "Web Development with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20with%20Foundation%20Year%20(BSc)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Arabic with Study Abroad (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Arabic%20with%20Study%20Abroad%20(MSc)",
        "desc": "Study Arabic language, Islamic civilizations, and Middle Eastern politics."
    },
    {
        "title": "Mathematics (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20(BA)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Ancient History with Professional Placement (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Ancient%20History%20with%20Professional%20Placement%20(BSc)",
        "desc": "Explore the civilizations of the ancient world from Mesopotamia to Rome."
    },
    {
        "title": "Interior Design with Study Abroad (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20with%20Study%20Abroad%20(MSc)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Statistics with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Statistics%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Advanced statistical theory, probability, and data analysis methods."
    },
    {
        "title": "Secondary Education (MA)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20(MA)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "Creative Arts with Professional Placement (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Creative%20Arts%20with%20Professional%20Placement%20(BSc)",
        "desc": "Interdisciplinary creative practice across visual and performing arts."
    },
    {
        "title": "Zoology (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Zoology%20(BSc%20Hons)",
        "desc": "Study animal biology, behavior, ecology, and wildlife conservation."
    },
    {
        "title": "Pharmacology (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Pharmacology%20(BSc%20Hons)",
        "desc": "Study how drugs interact with biological systems and treat disease."
    },
    {
        "title": "Forensic Psychology (BA Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20(BA%20Hons)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Marketing and Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Marketing%20and%20Management%20(MSc)",
        "desc": "Consumer behavior, digital strategy, brand management, and market research."
    },
    {
        "title": "Media Studies and Finance (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20and%20Finance%20(BSc)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Food Science (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20(BSc%20Hons)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Sport Coaching with Study Abroad (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Sport%20Coaching%20with%20Study%20Abroad%20(MSc)",
        "desc": "Develop athletic talent through evidence-based coaching methodologies."
    },
    {
        "title": "Genetics and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Genetics%20and%20International%20Relations%20(BA)",
        "desc": "Study DNA, heredity, gene therapy, and genetic engineering technologies."
    },
    {
        "title": "Supply Chain Management (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Supply%20Chain%20Management%20(Graduate%20Diploma)",
        "desc": "Logistics, procurement, operations management, and global supply networks."
    },
    {
        "title": "International Business with Sandwich Year (BSc)",
        "category": "Business",
        "url": "course-details.html?course=International%20Business%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Global trade, cross-border strategy, supply chain, and international markets."
    },
    {
        "title": "Civil Engineering (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Civil%20Engineering%20(MRes)",
        "desc": "Design and build bridges, highways, dams, and essential infrastructure."
    },
    {
        "title": "Sport Coaching with a Year in Industry (BA)",
        "category": "Education",
        "url": "course-details.html?course=Sport%20Coaching%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Develop athletic talent through evidence-based coaching methodologies."
    },
    {
        "title": "Retail Management (MRes)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20(MRes)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Biomedical Science with Study Abroad (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Biomedical%20Science%20with%20Study%20Abroad%20(MSc)",
        "desc": "Laboratory diagnosis, blood sciences, and clinical pathology."
    },
    {
        "title": "Web Development (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20(Integrated%20Masters)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Biochemistry and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biochemistry%20and%20Finance%20(BSc)",
        "desc": "Explore the chemical processes and molecular mechanisms within living organisms."
    },
    {
        "title": "Microbiology with Data Science (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Microbiology%20with%20Data%20Science%20(MSc)",
        "desc": "Study microorganisms, infectious diseases, and antimicrobial resistance."
    },
    {
        "title": "Food Science and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20and%20International%20Relations%20(BA)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Automotive Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(BA)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Dietetics and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dietetics%20and%20International%20Relations%20(BA)",
        "desc": "Clinical nutrition science, dietary interventions, and public health nutrition."
    },
    {
        "title": "Cloud Computing (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Cloud%20Computing%20(MA)",
        "desc": "AWS, Azure, and GCP infrastructure design and DevOps engineering."
    },
    {
        "title": "Digital Media (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20(MSc)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Supply Chain Management and Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Supply%20Chain%20Management%20and%20Management%20(MSc)",
        "desc": "Logistics, procurement, operations management, and global supply networks."
    },
    {
        "title": "Automotive Engineering and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20and%20Management%20(MSc)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Child Psychology and Management (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Child%20Psychology%20and%20Management%20(MSc)",
        "desc": "Study cognitive, emotional, and social development from infancy to adolescence."
    },
    {
        "title": "Artificial Intelligence (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20(BA)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Information Technology with a Year in Industry (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Information%20Technology%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Manage digital infrastructure, cloud computing, and enterprise networking."
    },
    {
        "title": "Physics with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Physiotherapy (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Physiotherapy%20(Integrated%20Masters)",
        "desc": "Physical rehabilitation, musculoskeletal therapy, and movement science."
    },
    {
        "title": "Marine Engineering (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20(BA%20Hons)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Forensic Psychology (Integrated Masters)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Forensic%20Psychology%20(Integrated%20Masters)",
        "desc": "Apply psychological principles to criminal investigation and the legal system."
    },
    {
        "title": "Marketing with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Marketing%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Consumer behavior, digital strategy, brand management, and market research."
    },
    {
        "title": "Mathematics (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20(MRes)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Nuclear Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Nuclear%20Engineering%20(BA)",
        "desc": "Nuclear power generation, radiation safety, and reactor design."
    },
    {
        "title": "Urban Planning with Professional Placement (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20with%20Professional%20Placement%20(BSc)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Graphic Design and International Relations (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Graphic%20Design%20and%20International%20Relations%20(BA)",
        "desc": "Visual communication, branding, typography, and digital media design."
    },
    {
        "title": "International Relations (BA Hons)",
        "category": "Social Sciences",
        "url": "course-details.html?course=International%20Relations%20(BA%20Hons)",
        "desc": "Analyze global diplomacy, conflict resolution, and foreign policy frameworks."
    },
    {
        "title": "American Studies (Graduate Diploma)",
        "category": "Humanities",
        "url": "course-details.html?course=American%20Studies%20(Graduate%20Diploma)",
        "desc": "Study American history, culture, politics, and literature."
    },
    {
        "title": "Aerospace Engineering with Study Abroad (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Aerospace%20Engineering%20with%20Study%20Abroad%20(MSc)",
        "desc": "Design and develop aircraft, spacecraft, and satellite technologies."
    },
    {
        "title": "Games Technology (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20(MRes)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "American Studies (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=American%20Studies%20(MSc)",
        "desc": "Study American history, culture, politics, and literature."
    },
    {
        "title": "Cyber Security and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Cyber%20Security%20and%20Management%20(MSc)",
        "desc": "Protect networks, systems, and data from digital threats and cyber attacks."
    },
    {
        "title": "Blockchain Technology and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Blockchain%20Technology%20and%20Management%20(MSc)",
        "desc": "Distributed ledger technology, smart contracts, and decentralized applications."
    },
    {
        "title": "Mechanical Engineering and Management (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20and%20Management%20(MSc)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "International Development (BA)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20(BA)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "Veterinary Medicine (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20(BA)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Child Psychology and Finance (BSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Child%20Psychology%20and%20Finance%20(BSc)",
        "desc": "Study cognitive, emotional, and social development from infancy to adolescence."
    },
    {
        "title": "Game Design (MA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20(MA)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Games Technology (Graduate Diploma)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20(Graduate%20Diploma)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "International Business with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=International%20Business%20with%20Data%20Science%20(MSc)",
        "desc": "Global trade, cross-border strategy, supply chain, and international markets."
    },
    {
        "title": "Artificial Intelligence and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20and%20International%20Relations%20(BA)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Interior Design (Graduate Diploma)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Interior%20Design%20(Graduate%20Diploma)",
        "desc": "Design functional and aesthetic indoor spaces for residential and commercial use."
    },
    {
        "title": "Finance (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20(BA%20Hons)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Journalism with a Year in Industry (BA)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "Film and Television with a Year in Industry (BA)",
        "category": "Media",
        "url": "course-details.html?course=Film%20and%20Television%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Video production, directing, cinematography, and post-production editing."
    },
    {
        "title": "Data Science and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Data%20Science%20and%20International%20Relations%20(BA)",
        "desc": "Analyze big data, build machine learning models, and drive data strategy."
    },
    {
        "title": "Forensic Science (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20(MRes)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Film Studies with Sandwich Year (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Film%20Studies%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Critical analysis of cinema, film theory, and world cinema movements."
    },
    {
        "title": "Audiology with Sandwich Year (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Environmental Engineering (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Environmental%20Engineering%20(BA%20Hons)",
        "desc": "Design sustainable solutions for water, waste, and pollution control."
    },
    {
        "title": "Drama and Theatre Studies with Foundation Year (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Drama%20and%20Theatre%20Studies%20with%20Foundation%20Year%20(BSc)",
        "desc": "Acting, directing, stage production, and dramatic literature."
    },
    {
        "title": "Journalism and International Relations (BA)",
        "category": "Media",
        "url": "course-details.html?course=Journalism%20and%20International%20Relations%20(BA)",
        "desc": "Investigative reporting, multimedia broadcasting, and digital journalism."
    },
    {
        "title": "Adult Nursing with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Adult%20Nursing%20with%20Data%20Science%20(MSc)",
        "desc": "Clinical nursing care for adult patients across medical and surgical settings."
    },
    {
        "title": "Neuroscience with Foundation Year (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20with%20Foundation%20Year%20(BSc)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Hospitality Management with a Year in Industry (BA)",
        "category": "Business",
        "url": "course-details.html?course=Hospitality%20Management%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Hotel operations, tourism economics, and service industry leadership."
    },
    {
        "title": "English Literature (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Literature%20(BSc%20Hons)",
        "desc": "Critical analysis of literary texts, culture, postcolonial theory, and creative writing."
    },
    {
        "title": "Children's Nursing (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Children's%20Nursing%20(BSc)",
        "desc": "Specialist nursing care for infants, children, and young people."
    },
    {
        "title": "Business Analytics (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Analytics%20(BSc)",
        "desc": "Data-driven decision making, business intelligence, and predictive modeling."
    },
    {
        "title": "Entrepreneurship with Professional Placement (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Entrepreneurship%20with%20Professional%20Placement%20(BSc)",
        "desc": "Learn to ideate, build, launch, and scale startup ventures and SMEs."
    },
    {
        "title": "Automotive Engineering (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20(MSc)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Pharmacology and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Pharmacology%20and%20International%20Relations%20(BA)",
        "desc": "Study how drugs interact with biological systems and treat disease."
    },
    {
        "title": "Games Technology (MA)",
        "category": "STEM",
        "url": "course-details.html?course=Games%20Technology%20(MA)",
        "desc": "Video game development, 3D engines, and interactive media programming."
    },
    {
        "title": "Project Management (Graduate Diploma)",
        "category": "Business",
        "url": "course-details.html?course=Project%20Management%20(Graduate%20Diploma)",
        "desc": "Agile methodologies, risk management, and delivering complex projects on time."
    },
    {
        "title": "International Development with Professional Placement (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20with%20Professional%20Placement%20(BSc)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "Public Relations and Communications with Sandwich Year (BSc)",
        "category": "Media",
        "url": "course-details.html?course=Public%20Relations%20and%20Communications%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Strategic communications, crisis management, and media relations."
    },
    {
        "title": "Teaching English as a Foreign Language (MA)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20(MA)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Linguistics (BA Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Linguistics%20(BA%20Hons)",
        "desc": "The scientific study of language structure, phonetics, syntax, and semantics."
    },
    {
        "title": "International Development (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20(BSc)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "Dentistry (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Dentistry%20(Integrated%20Masters)",
        "desc": "Comprehensive training in oral healthcare, dental surgery, and prosthodontics."
    },
    {
        "title": "Fashion Design (MA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20(MA)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Mental Health Nursing with Professional Placement (BSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20with%20Professional%20Placement%20(BSc)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Teaching English as a Foreign Language and Management (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Teaching%20English%20as%20a%20Foreign%20Language%20and%20Management%20(MSc)",
        "desc": "Teach English language skills to non-native speakers worldwide."
    },
    {
        "title": "Social Policy (MRes)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Social%20Policy%20(MRes)",
        "desc": "Examine welfare systems, public health policy, and social inequality."
    },
    {
        "title": "Public Health and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Public%20Health%20and%20International%20Relations%20(BA)",
        "desc": "Epidemiology, health promotion, and population-level disease prevention."
    },
    {
        "title": "Mental Health Nursing with a Year in Industry (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Veterinary Medicine and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20and%20International%20Relations%20(BA)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Marine Engineering (Integrated Masters)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20(Integrated%20Masters)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Jewellery Design (MA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Jewellery%20Design%20(MA)",
        "desc": "Gemology, metalwork, CAD jewelry design, and luxury brand development."
    },
    {
        "title": "Forensic Science (BSc Hons)",
        "category": "Sciences",
        "url": "course-details.html?course=Forensic%20Science%20(BSc%20Hons)",
        "desc": "Apply scientific techniques to criminal investigation and evidence analysis."
    },
    {
        "title": "Japanese Studies (BSc Hons)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20(BSc%20Hons)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Public Relations with Data Science (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Public%20Relations%20with%20Data%20Science%20(MSc)",
        "desc": "Strategic communications, crisis management, and corporate reputation."
    },
    {
        "title": "Entrepreneurship (BA)",
        "category": "Business",
        "url": "course-details.html?course=Entrepreneurship%20(BA)",
        "desc": "Learn to ideate, build, launch, and scale startup ventures and SMEs."
    },
    {
        "title": "Astrophysics and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Astrophysics%20and%20Management%20(MSc)",
        "desc": "Explore the physical nature of stars, galaxies, dark matter, and the universe."
    },
    {
        "title": "Radiography and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20and%20International%20Relations%20(BA)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Tourism Management (MA)",
        "category": "Business",
        "url": "course-details.html?course=Tourism%20Management%20(MA)",
        "desc": "Destination management, sustainable tourism, and leisure industry operations."
    },
    {
        "title": "Optometry (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Optometry%20(BSc%20Hons)",
        "desc": "Examine eyes for vision defects, prescribe lenses, and detect eye disease."
    },
    {
        "title": "Podiatry with Data Science (MSc)",
        "category": "Healthcare",
        "url": "course-details.html?course=Podiatry%20with%20Data%20Science%20(MSc)",
        "desc": "Diagnose and treat conditions of the feet and lower limbs."
    },
    {
        "title": "Paramedic Science (BA Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Paramedic%20Science%20(BA%20Hons)",
        "desc": "Emergency medical response, trauma care, and pre-hospital medicine."
    },
    {
        "title": "Digital Media (MA)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20(MA)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Spanish (Integrated Masters)",
        "category": "Humanities",
        "url": "course-details.html?course=Spanish%20(Integrated%20Masters)",
        "desc": "Study the Spanish language, Latin American literature, and Hispanic cultures."
    },
    {
        "title": "Neuroscience (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Neuroscience%20(BSc)",
        "desc": "Investigate the nervous system, brain function, and neurological disorders."
    },
    {
        "title": "Animation (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20(BSc)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Fashion Design and International Relations (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Fashion%20Design%20and%20International%20Relations%20(BA)",
        "desc": "Create apparel, study textiles, pattern cutting, and the fashion industry."
    },
    {
        "title": "Criminology and Policing with Professional Placement (BSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Criminology%20and%20Policing%20with%20Professional%20Placement%20(BSc)",
        "desc": "Criminal justice, crime prevention, and modern policing strategies."
    },
    {
        "title": "Automotive Engineering and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Automotive%20Engineering%20and%20Finance%20(BSc)",
        "desc": "Design and develop vehicles, powertrains, and electric mobility systems."
    },
    {
        "title": "Artificial Intelligence (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Artificial%20Intelligence%20(BA%20Hons)",
        "desc": "Develop intelligent systems, neural networks, and machine learning algorithms."
    },
    {
        "title": "Media Studies (MSc)",
        "category": "Media",
        "url": "course-details.html?course=Media%20Studies%20(MSc)",
        "desc": "Analyze mass communication, digital culture, and media theory."
    },
    {
        "title": "Radiography (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Radiography%20(BA)",
        "desc": "Medical imaging, CT/MRI scanning, and diagnostic radiation therapy."
    },
    {
        "title": "Electrical Engineering and International Relations (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Electrical%20Engineering%20and%20International%20Relations%20(BA)",
        "desc": "Develop electrical power systems, circuits, and renewable energy grids."
    },
    {
        "title": "Business Administration and Management (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Business%20Administration%20and%20Management%20(MSc)",
        "desc": "Comprehensive business operations, leadership, and organizational management."
    },
    {
        "title": "Biomedical Sciences and Management (MSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20and%20Management%20(MSc)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "English Language (MSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20(MSc)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Child Psychology with Data Science (MSc)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Child%20Psychology%20with%20Data%20Science%20(MSc)",
        "desc": "Study cognitive, emotional, and social development from infancy to adolescence."
    },
    {
        "title": "International Business and Finance (BSc)",
        "category": "Business",
        "url": "course-details.html?course=International%20Business%20and%20Finance%20(BSc)",
        "desc": "Global trade, cross-border strategy, supply chain, and international markets."
    },
    {
        "title": "Mental Health Nursing (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Mental%20Health%20Nursing%20(Integrated%20Masters)",
        "desc": "Specialist nursing care for patients with mental health conditions."
    },
    {
        "title": "Occupational Therapy and International Relations (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20and%20International%20Relations%20(BA)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Cloud Computing (BA Hons)",
        "category": "STEM",
        "url": "course-details.html?course=Cloud%20Computing%20(BA%20Hons)",
        "desc": "AWS, Azure, and GCP infrastructure design and DevOps engineering."
    },
    {
        "title": "Physics and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20and%20International%20Relations%20(BA)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Psychology (Graduate Diploma)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Psychology%20(Graduate%20Diploma)",
        "desc": "Explore the human mind and behavior through scientific methods, clinical research, and cognitive analysis."
    },
    {
        "title": "Secondary Education with Foundation Year (BSc)",
        "category": "Education",
        "url": "course-details.html?course=Secondary%20Education%20with%20Foundation%20Year%20(BSc)",
        "desc": "Train to teach specialist subjects to students aged 11-18."
    },
    {
        "title": "Veterinary Medicine (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Veterinary%20Medicine%20(Integrated%20Masters)",
        "desc": "Clinical training for the diagnosis, treatment, and care of animals."
    },
    {
        "title": "Real Estate (BA Hons)",
        "category": "Business",
        "url": "course-details.html?course=Real%20Estate%20(BA%20Hons)",
        "desc": "Property valuation, investment analysis, urban planning, and development finance."
    },
    {
        "title": "Mechanical Engineering (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Mechanical%20Engineering%20(MSc)",
        "desc": "Study mechanics, thermodynamics, robotics, and manufacturing systems."
    },
    {
        "title": "Zoology and International Relations (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Zoology%20and%20International%20Relations%20(BA)",
        "desc": "Study animal biology, behavior, ecology, and wildlife conservation."
    },
    {
        "title": "Game Design with a Year in Industry (BA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Game%20Design%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Game mechanics, level design, narrative design, and user experience."
    },
    {
        "title": "Entrepreneurship with Study Abroad (MSc)",
        "category": "Business",
        "url": "course-details.html?course=Entrepreneurship%20with%20Study%20Abroad%20(MSc)",
        "desc": "Learn to ideate, build, launch, and scale startup ventures and SMEs."
    },
    {
        "title": "Urban Planning (MA)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20(MA)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Marine Engineering (BA)",
        "category": "STEM",
        "url": "course-details.html?course=Marine%20Engineering%20(BA)",
        "desc": "Design and maintain ships, submarines, and offshore energy platforms."
    },
    {
        "title": "Broadcasting (Graduate Diploma)",
        "category": "Media",
        "url": "course-details.html?course=Broadcasting%20(Graduate%20Diploma)",
        "desc": "Radio and television production, live broadcasting, and media technology."
    },
    {
        "title": "Chinese Studies with Sandwich Year (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=Chinese%20Studies%20with%20Sandwich%20Year%20(BSc)",
        "desc": "Mandarin language proficiency combined with East Asian history and politics."
    },
    {
        "title": "Illustration and Finance (BSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Illustration%20and%20Finance%20(BSc)",
        "desc": "Editorial, children's book, and commercial illustration techniques."
    },
    {
        "title": "Urban Planning and Management (MSc)",
        "category": "Public Sector",
        "url": "course-details.html?course=Urban%20Planning%20and%20Management%20(MSc)",
        "desc": "Design sustainable cities, housing policy, and urban regeneration."
    },
    {
        "title": "Audiology (Integrated Masters)",
        "category": "Healthcare",
        "url": "course-details.html?course=Audiology%20(Integrated%20Masters)",
        "desc": "Assess and treat hearing and balance disorders across all ages."
    },
    {
        "title": "Architecture with Foundation Year (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20with%20Foundation%20Year%20(BSc)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "Accounting (BSc Hons)",
        "category": "Business",
        "url": "course-details.html?course=Accounting%20(BSc%20Hons)",
        "desc": "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."
    },
    {
        "title": "Finance with Professional Placement (BSc)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20with%20Professional%20Placement%20(BSc)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Physiotherapy (BA)",
        "category": "Healthcare",
        "url": "course-details.html?course=Physiotherapy%20(BA)",
        "desc": "Physical rehabilitation, musculoskeletal therapy, and movement science."
    },
    {
        "title": "Physical Education and International Relations (BA)",
        "category": "Education",
        "url": "course-details.html?course=Physical%20Education%20and%20International%20Relations%20(BA)",
        "desc": "Train to teach PE and promote physical literacy in school settings."
    },
    {
        "title": "Food Science and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20and%20Finance%20(BSc)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Accounting (MA)",
        "category": "Business",
        "url": "course-details.html?course=Accounting%20(MA)",
        "desc": "Gain professional ACCA/CIMA qualifications, financial reporting, and audit skills."
    },
    {
        "title": "Ecology with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Ecology%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Study ecosystems, biodiversity, and environmental conservation strategies."
    },
    {
        "title": "Education Studies (BSc Hons)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20(BSc%20Hons)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Illustration (MA)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Illustration%20(MA)",
        "desc": "Editorial, children's book, and commercial illustration techniques."
    },
    {
        "title": "English Language and Finance (BSc)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20and%20Finance%20(BSc)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Retail Management and International Relations (BA)",
        "category": "Business",
        "url": "course-details.html?course=Retail%20Management%20and%20International%20Relations%20(BA)",
        "desc": "Consumer retail strategy, e-commerce, merchandising, and brand operations."
    },
    {
        "title": "Music Production (BA Hons)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Music%20Production%20(BA%20Hons)",
        "desc": "Audio engineering, sound design, mixing, and mastering techniques."
    },
    {
        "title": "Environmental Engineering (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Environmental%20Engineering%20(MRes)",
        "desc": "Design sustainable solutions for water, waste, and pollution control."
    },
    {
        "title": "Anthropology (BA)",
        "category": "Social Sciences",
        "url": "course-details.html?course=Anthropology%20(BA)",
        "desc": "Study human origins, cultures, societal development, and cross-cultural diversity."
    },
    {
        "title": "Mathematics with a Year in Industry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Information Technology (MRes)",
        "category": "STEM",
        "url": "course-details.html?course=Information%20Technology%20(MRes)",
        "desc": "Manage digital infrastructure, cloud computing, and enterprise networking."
    },
    {
        "title": "Classics (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=Classics%20(BA)",
        "desc": "Study the literature, history, and culture of ancient Greece and Rome."
    },
    {
        "title": "Mathematics (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Mathematics%20(Integrated%20Masters)",
        "desc": "Advanced pure and applied mathematics, algebra, calculus, and mathematical logic."
    },
    {
        "title": "Architecture and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Architecture%20and%20Finance%20(BSc)",
        "desc": "Blend art and structural engineering to design physical spaces and cities."
    },
    {
        "title": "English Language with a Year in Industry (BA)",
        "category": "Humanities",
        "url": "course-details.html?course=English%20Language%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Explore the structure, history, and sociolinguistics of the English language."
    },
    {
        "title": "Biomedical Sciences and Finance (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Biomedical%20Sciences%20and%20Finance%20(BSc)",
        "desc": "Investigate human biology, pathology of disease, and laboratory diagnostics."
    },
    {
        "title": "Education Studies with a Year in Industry (BA)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20with%20a%20Year%20in%20Industry%20(BA)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Information Technology and Finance (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Information%20Technology%20and%20Finance%20(BSc)",
        "desc": "Manage digital infrastructure, cloud computing, and enterprise networking."
    },
    {
        "title": "Education Studies and Management (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Education%20Studies%20and%20Management%20(MSc)",
        "desc": "Explore educational theory, policy, and learning across diverse contexts."
    },
    {
        "title": "Japanese Studies (MRes)",
        "category": "Humanities",
        "url": "course-details.html?course=Japanese%20Studies%20(MRes)",
        "desc": "Study Japanese language, culture, anime industries, and East Asian business."
    },
    {
        "title": "Biochemistry (BA)",
        "category": "Sciences",
        "url": "course-details.html?course=Biochemistry%20(BA)",
        "desc": "Explore the chemical processes and molecular mechanisms within living organisms."
    },
    {
        "title": "Finance (BA)",
        "category": "Business",
        "url": "course-details.html?course=Finance%20(BA)",
        "desc": "Investment banking, portfolio management, derivatives, and financial modeling."
    },
    {
        "title": "Creative Writing (MA)",
        "category": "Humanities",
        "url": "course-details.html?course=Creative%20Writing%20(MA)",
        "desc": "Develop fiction, poetry, screenwriting, and non-fiction storytelling skills."
    },
    {
        "title": "Web Development (Graduate Diploma)",
        "category": "STEM",
        "url": "course-details.html?course=Web%20Development%20(Graduate%20Diploma)",
        "desc": "Full-stack development, frontend frameworks, and web application architecture."
    },
    {
        "title": "Food Science (MRes)",
        "category": "Sciences",
        "url": "course-details.html?course=Food%20Science%20(MRes)",
        "desc": "Study food production, safety, quality control, and nutritional biochemistry."
    },
    {
        "title": "Occupational Therapy (BSc Hons)",
        "category": "Healthcare",
        "url": "course-details.html?course=Occupational%20Therapy%20(BSc%20Hons)",
        "desc": "Help patients overcome physical and psychological barriers to daily life."
    },
    {
        "title": "Genetics (Graduate Diploma)",
        "category": "Sciences",
        "url": "course-details.html?course=Genetics%20(Graduate%20Diploma)",
        "desc": "Study DNA, heredity, gene therapy, and genetic engineering technologies."
    },
    {
        "title": "Cyber Security with Professional Placement (BSc)",
        "category": "STEM",
        "url": "course-details.html?course=Cyber%20Security%20with%20Professional%20Placement%20(BSc)",
        "desc": "Protect networks, systems, and data from digital threats and cyber attacks."
    },
    {
        "title": "Digital Media (Integrated Masters)",
        "category": "Media",
        "url": "course-details.html?course=Digital%20Media%20(Integrated%20Masters)",
        "desc": "Social media strategy, content creation, and digital platform management."
    },
    {
        "title": "Chemistry with Professional Placement (BSc)",
        "category": "Sciences",
        "url": "course-details.html?course=Chemistry%20with%20Professional%20Placement%20(BSc)",
        "desc": "Study molecular interactions, organic synthesis, and advanced materials science."
    },
    {
        "title": "Physics (Integrated Masters)",
        "category": "Sciences",
        "url": "course-details.html?course=Physics%20(Integrated%20Masters)",
        "desc": "Explore the fundamental principles governing matter, energy, and the universe."
    },
    {
        "title": "Animation and Management (MSc)",
        "category": "Arts & Design",
        "url": "course-details.html?course=Animation%20and%20Management%20(MSc)",
        "desc": "2D and 3D visual storytelling, motion graphics, and character design."
    },
    {
        "title": "Chemical Engineering with Data Science (MSc)",
        "category": "STEM",
        "url": "course-details.html?course=Chemical%20Engineering%20with%20Data%20Science%20(MSc)",
        "desc": "Industrial process design, material synthesis, and sustainable manufacturing."
    },
    {
        "title": "International Development (Graduate Diploma)",
        "category": "Public Sector",
        "url": "course-details.html?course=International%20Development%20(Graduate%20Diploma)",
        "desc": "Global poverty reduction, NGO management, and sustainable development goals."
    },
    {
        "title": "Sport Coaching (MSc)",
        "category": "Education",
        "url": "course-details.html?course=Sport%20Coaching%20(MSc)",
        "desc": "Develop athletic talent through evidence-based coaching methodologies."
    }
];
