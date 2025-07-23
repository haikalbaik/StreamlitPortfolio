import streamlit as st
from streamlit_option_menu import option_menu

# --- FUNCTIONS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- DATA ---
# This is now the single source of truth for your skills.
# Add, remove, or edit skills and their scores here.
ALL_SKILLS = {
    "User Support": 10,
    "User Acceptance Testing": 9,
    "SAP": 4,
    "GEP SMART P2P": 9,
    "Problem Solving": 10,
    "Change Management": 9,
    "Stakeholder Management": 9,
    "Project Management": 8,
    "Business Requirement Analysis": 8,
    "Process Improvement": 9,
    "IT Operations": 10,
    "Troubleshooting": 10,
    "Email Migration": 6,
    "System Administration": 7,
    "Backup & Disaster Recovery": 5,
    "Network Management": 6,
    "Resistivity Mapping": 4,
    "Data Collection": 9,
    "Interpretation": 9,
    "MATLAB": 6,
    "Data Management": 8,
}

# This is now the single source of truth for your job history.
JOB_DATA = [
    {
        "title": "Data Modeler Engineer / Business Support Analyst",
        "company": "PETRONAS Digital Sdn Bhd",
        "dates": "Oct 2024 - May 2025",
        "responsibilities": ["Provided L2 support for GEP SMART P2P module, resolving 5-7 tickets daily and consistently achieving 100% SLA adherence.", "Participated in User Acceptance Training (UAT) and knowledge transfer, validating processes to enhance overall user experience.", "Collaborated with procurement and governance teams to amend system processes, preventing incorrect PO generation for companies with multiple contracts."],
        "skills": ["User Support", "User Acceptance Testing", "SAP", "GEP SMART P2P", "Problem Solving"]
    },
    {
        "title": "System Analyst",
        "company": "Hibiscus Petroleum Berhad",
        "dates": "March 2023 - Oct 2024",
        "responsibilities": ["Led the implementation of GEP SMART, achieving 100% compliance for system users and enhancing procurement governance through digital transformation.", "Led User Acceptance Training for 45 buyers and 10 approvers, and managed stakeholders during system implementation, achieving 20% user adoption in pilot cases.", "Resolved audit-related issues by validating 82 out of 83 contracts (99% resolution rate) with over 10,000 line items, addressing system discrepancies from migration."],
        "skills": ["Change Management", "User Acceptance Testing", "Stakeholder Management", "Project Management", "Business Requirement Analysis", "Process Improvement"]
    },
    {
        "title": "IT Specialist",
        "company": "Three60 Energy Asia Sdn Bhd",
        "dates": "Nov 2013 - Nov 2022",
        "responsibilities": ["Managed IT operations as a sole IT specialist for an organization of 200 people and over 90 on-premise devices.", "Managed user onboarding/offboarding and resolved all IT-related issues (network, server, software, hardware), maintaining 95% system uptime.", "Monitored IT infrastructure to ensure smooth business operations, proactively identifying and reporting potential issues to management."],
        "skills": ["IT Operations", "User Support", "Stakeholder Management", "Project Management", "Troubleshooting", "Email Migration", "System Administration", "Backup & Disaster Recovery", "Network Management"]
    },
    {
        "title": "Research Asssistant",
        "company": "Universiti Teknologi PETRONAS",
        "dates": "Jan 2013 - May 2013",
        "responsibilities": ["Act as focal for geophysical data acquisition related activities", "Followed safety procedure during data acquisition", "Helped with geophysical data interpretation"],
        "skills": ["Resistivity Mapping", "Data Collection", "Interpretation"]
    },
    {
        "title": "Data Management Intern",
        "company": "LMKR",
        "dates": "Oct 2011 - April 2012",
        "responsibilities": ["Learn how to handle oil and gas dataset in physical & digital format", "Identifed business opportunities created by owning the data", "Completed internship projects"],
        "skills": ["MATLAB", "Data Management"]
    }
]

PROJECT_DATA = [
    {"title": "Project 1: Streamlit Personal Portfolio", "difficulty": 1, "link": "https://github.com/haikalbaik", "description": "Demonstrated the power of LLMs for personal branding by creating this portfolio entirely with Gemini 2.5 Pro and Flash, showcasing rapid, AI-driven development.", "skills": ["Python", "Streamlit", "LLM Prompting"]},
    {"title": "Project 2: Geohackathon - Well Top Formation Prediction", "difficulty": 2, "link": "https://github.com/haikalbaik/GeoHackathon2022", "description": "Achieved high-accuracy well top formation prediction by applying machine learning techniques to complex well log data, demonstrating data modeling and interpretation skills.", "skills": ["Machine Learning", "Well Log Interpretation", "Data Modeling", "Random Forest"]},
    {"title": "Project 3: Power Automate PDF Scrapper", "difficulty": 3, "link": None, "description": "Saved over 200 man-hours by developing an automation script that accurately scraped 3,700+ company records from PDFs, eliminating manual data entry for a critical system migration.", "skills": ["Python", "Automation", "MS Excel", "Power Automate Desktop"]},
    {"title": "Project 4: Digital Procurement Implementation", "difficulty": 5, "link": None, "description": "Strengthened procurement governance and ensured compliance by leading the implementation of a new digital procurement system, successfully training and onboarding all users.", "skills": ["User Acceptance Testing", "User Training", "Stakeholder Management","Business Requirement Analysis", "Project Management"]},
    {"title": "Project 5: MVP - Secure Data Room", "difficulty": 3, "link": None, "description": "Delivered a secure and cost-effective solution for remote data access by building a Minimum Viable Product (MVP) using open-source tools, fulfilling an urgent client need without expensive VDR software.", "skills": ["Apache Guacamole", "Windows Hardening", "Bash Scripting", "Firewall Configuration"]},
    {"title": "Project 6: Telco Data Analysis", "difficulty": 4, "link": None, "description": "Unlocked new marketing opportunities for a client by analyzing a massive 1TB+ telco dataset (76M+ rows) to identify and present targeted strategies for Digital Out-of-Home advertising.", "skills": ["Power BI", "SQL", "Pandas","Numpy","Seaborn", "Matplotlib"]}
]

# --- UNIFY SKILLS ---
job_skills = {skill for job in JOB_DATA for skill in job['skills']}
project_skills = {skill for project in PROJECT_DATA for skill in project['skills']}
all_unique_skills = job_skills.union(project_skills)

for skill in all_unique_skills:
    if skill not in ALL_SKILLS:
        ALL_SKILLS[skill] = 6  # Default score for new skills

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Personal Portfolio",
    page_icon="👤",
    layout="wide"
)

# --- LOAD CSS ---
local_css("style/style.css")

# --- NAVIGATION ---
query_params = st.query_params
selected_skill_from_query = query_params.get("skill", [None])[0]

default_tab_index = 1 if selected_skill_from_query else 0

selected = option_menu(
    menu_title=None,
    options=["About Me", "Experience", "Projects", "Contact Me"],
    icons=["person-bounding-box", "briefcase-fill", "code-braces", "envelope-at-fill"],
    menu_icon="cast",
    default_index=default_tab_index,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0A0A0A"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#1C1C1C"},
        "nav-link-selected": {"background-color": "#E05E00"},
    },
)

# --- ABOUT ME PAGE ---
def about_me():
    st.title("About Me")
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://avatars.githubusercontent.com/u/47693704?v=4", use_container_width=True)

    with col2:
        st.header("Mohd Haikal Mohd Isa")
        st.write("Hey there! I'm Haikal, an IT & Systems Analyst with over a decade of experience turning complex challenges into smooth, digital solutions.")
        st.write("You might be surprised to learn my journey started deep in the earth, studying Petroleum Geoscience! That's where I first learned how to rock (get it?), consult and solve problems, skills I now happily apply to the world of tech.")
        st.write("I'm all about making things work better, whether it's orchestrating a full-blown digital transformation, streamlining processes with smart automation, or ensuring everyone's on board with new systems.")
        st.write("My superpower? A blend of IT operations, data savvy, and a keen eye for cybersecurity, all wrapped up in a passion for bridging tech with real-world business goals.")
        st.write("Think of me as your go-to person for making digital dreams a reality, efficiently and effectively!")

    st.write("---")
    st.subheader("My Skills")
    st.info("Click on any skill to see the relevant work experience!", icon="💡")

    def display_skills(skill_dict):
        html_string = '<div class="skill-container">'
        for skill, score in skill_dict.items():
            link = f'/?skill={skill.replace(" ", "+")}'
            html_string += f"""
            <a href="{link}" class="skill-box" style="--proficiency-percent: {score * 10}%">
                <span class="skill-name">{skill}</span>
                <span class="skill-score">{score}/10</span>
            </a>
            """
        html_string += '</div>'
        st.html(html_string)

    display_skills(ALL_SKILLS)

# --- EXPERIENCE PAGE ---
def experience():
    st.title("Work Experience")
    st.write("---")

    filtered_skill = selected_skill_from_query.replace("+", " ") if selected_skill_from_query else None

    for job in JOB_DATA:
        is_highlighted = filtered_skill in job['skills'] if filtered_skill else False
        card_class = "job-card highlighted-job" if is_highlighted else "job-card"

        # Build the skills HTML first, so it's ready
        skills_html = '<div class="skill-box-container-sm">'
        for skill in job['skills']:
            skills_html += f'<div class="skill-box-sm">{skill}</div>'
        skills_html += '</div>'

        # Construct the full HTML card
        st.markdown(f'''
        <div class="{card_class}">
            <details>
                <summary>
                    <h3>{job["title"]}</h3>
                    <div class="job-company-details">
                        <span class="job-company">{job["company"]}</span> | <span class="job-dates">{job["dates"]}</span>
                    </div>
                </summary>
                <ul class="job-responsibilities">
                    {' '.join([f"<li>• {resp}</li>" for resp in job["responsibilities"]])}
                </ul>
            </details>
            <div class="visible-skills">
                <strong>Skills Used:</strong>
                {skills_html}
            </div>
        </div>
        ''', unsafe_allow_html=True)

# --- PROJECTS PAGE ---
def projects():
    st.title("My Projects")
    st.write("---")

    for project in PROJECT_DATA:
        difficulty_html = f"<div class=\"difficulty-icons\" title=\"Project Difficulty: {project['difficulty']}/5\">" + "🔥" * project['difficulty'] + "</div>"

        link_button_html = ""
        if project["link"]:
            link_button_html = f'<a href="{project["link"]}" target="_blank" class="stLinkButton">Source Code ></a>'
        else:
            link_button_html = "<p>*(Client Project - Code Not Public)*</p>"

        skills_html = ""
        if project['skills']:
            skills_html = '<div class="project-skills-wrapper"><div class="skill-box-container-sm">'
            for skill in project['skills']:
                skills_html += f'<div class="skill-box-sm">{skill}</div>'
            skills_html += '</div></div>'

        # Construct the full HTML card for the project
        project_card_html = f"""
        <div class="project-card-single">
            {difficulty_html}
            <h3>{project["title"]}</h3>
            <div class="project-description-wrapper"><p>{project["description"]}</p></div>
            {link_button_html}
            {skills_html}
        </div>
        """
        st.markdown(project_card_html, unsafe_allow_html=True)

# --- CONTACT ME PAGE ---
def contact_me():
    st.title("Let's Connect!")
    st.write("---")
    st.write("I'm always open to connecting and discussing new opportunities.")
    st.write(
        """
        - 🔗 **LinkedIn:** [My LinkedIn](https://www.linkedin.com/in/mohdhaikalmohdisa/)
        - 👨‍💻 **GitHub:** [My Github](https://github.com/haikalbaik)
        """
    )

# --- PAGE SELECTION LOGIC ---
if selected == "About Me":
    about_me()
elif selected == "Experience":
    experience()
elif selected == "Projects":
    projects()
elif selected == "Contact Me":
    contact_me()
