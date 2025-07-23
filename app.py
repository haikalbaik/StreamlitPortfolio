import streamlit as st
from streamlit_option_menu import option_menu
from data import ABOUT_ME_DATA, ALL_SKILLS, JOB_DATA, PROJECT_DATA

# --- FUNCTIONS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


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
        st.header(ABOUT_ME_DATA["header"])
        st.write(ABOUT_ME_DATA["intro"])
        for item in ABOUT_ME_DATA["body"]:
            st.write(item)

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
