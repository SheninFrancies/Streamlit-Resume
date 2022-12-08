import streamlit as st
from PIL import Image
from pathlib import Path
# Page settings
PAGE_TITLE = "Digital CV | Shenin Francies"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "styles.css"
resume_file = current_dir / "Assets" / "Resume.pdf"
profile_pic = current_dir / "Assets" / "Foto.jpg"
with open("Styles/styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="name" target="_blank">Curriculum Vitae</a>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#personal-projects">Personal Projects</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

###################################

# Header
st.write('''
# Shenin Francies 
''')
image = Image.open('Assets/Foto.jpg')
DESCRIPTION = """
Detail-oriented Data Scientist, with strong analytical and technical skills, guided by the passion to work towards
a unified cause. Recent graduate of Medical Engineering who conducts independent researches. Conversant
in culture diversity due to exposure to international relations based off of studying and living in India, Kuwait, United Arab Emirates and Germany.
"""
EMAIL = "shenin.francies@gmail.com"
SOCIAL_MEDIA = {
    "Tableau": "https://public.tableau.com/app/profile/shenin.francis",
    "LinkedIn": "https://linkedin.com/in/shenin-francies",
    "GitHub": "https://github.com/SheninFrancies"
}
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image, width=150)
with col2:
    st.info(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#####################
# Custom function for printing text
def txt(a, b, c):
    col1, col2, col3 = st.columns([4, 3, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


def txt2(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt3(a, b, c):
  col1, col2, col3 = st.columns([3, 3, 2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
#####################

st.markdown('''
## Education
''')

txt('**Master of Science** Biomedical Engineering', 'Hochschule Furtwangen University, Germany',
    '2019-2022')
st.markdown('''
- Grade: `1.5` (Very Good).
- Courses: `Physiological Modelling`, `Artificial Intelligence`, `Medical Devices - EU Regulatory Affairs`, `Artificial Organs and Membranes`.
- Master thesis: `Electrical Measurements of Biological Tissue Phantoms to study the effects of Bioimpedance`.
''')

txt('**Bachelors of Engineering** Electrical and Electronic Engineering', 'Heriot-Watt University, United Arab Emirates',
    '2016-2019')
st.markdown('''
- GPA: `3.8/4` (Excellent).
- Courses: `Control Systems and System Theory`, `MATLAB and Simulink`, `C and C++`, `Mechanical Design`, `AutoCAD`, `3D-Printing`
- Graduated with Distinction.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Intern - Data Science and Machine Learning**', 'Luminar Technolab, Kerala',
    '2022-Present')
st.markdown('''
- Preprocessing of Datasets using Python libraries such as `NumPy` and `Pandas`. 
- Applied `Supervised and Unsupervised Machine Learning` techniques on datasets to derive meaningful insights from the model.
- Familiarized with Deep Learning frameworks such as `TensorFlow` and `Keras`. 
- Skilled in employing Data visualization tools such as `Tableau` and `PowerBI`.
''')

txt('**Research Assistant**', 'Hochschule Furtwangen University, Germany', '2021')
st.markdown('''
- Researched the Two- and Four-Electrode methods in Electrical Impedance Tomography. 
- Built circuits and assessed the signal strength.
- Improved the circuit for optimal analysis of the signal.
- Calibration of laboratory equipment.
- Prototype testing of circuits in a laboratory environment.
''')
#####################
st.markdown('''
## Skills
''')
txt2('Programming', '`Python`, `MATLAB`, `R`')
txt2('Data processing/wrangling', '`Pandas`, `NumPy`')
txt2('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`, `Folium`, `ggplot2`')
txt2('Descriptive Statistics', '`SciPy`')
txt2('Big Data Analysis', '`Apache Spark`')
txt2('Machine Learning', '`Scikit-learn`')
txt2('Deep Learning', '`TensorFlow`, `Keras`')
txt2('Model deployment', '`Streamlit`, `AWS`')

#####################
st.markdown('''
## Certifications
''')
txt('Applied Data Science with Python - Level 2', 'IBM',
    'Dec 2022')
txt('Big Data Foundations - Level 2', 'IBM',
    'Dec 2022')
txt('Python for Data Science and Machine Learning Bootcamp', 'Udemy',
    'Dec 2022')
txt('Calibration, Testing and Maintenance of Medical Devices', 'Cyrix Healthcaree Pvt. Ltd.',
    'Oct 2022')
txt('Certified Project Manager', 'Excellenter Institute',
    'July 2021')

#####################
st.markdown('''
## Personal Projects
''')
txt3('Deploying ML Projects using Streamlit and Python', 'Deploying completed ML projects using Streamlit in conjunction with Python',
     'December 2022 - Present')
txt3('Applications of Machine Learning in Healthcare', 'Implemented Machine Learning algorithms to make predictions on various healthcare datasets',
     'December 2022')

