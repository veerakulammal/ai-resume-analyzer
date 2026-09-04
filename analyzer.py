import re
try:
    import pdfplumber
except ImportError:
    pdfplumber = None

SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
    "C",
    "HTML",
    "CSS",
    "SQL",
    "MySQL",
    "MongoDB",
    "Pandas",
    "NumPy",
    "matplotlib",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Analysis",
    "Data science",
    "Natural Language Processing",
    "Computer Vision",
    "OpenCV",
    "Streamlit",
    "Flask",
    "Django",
    "Git",
    "Github",
    "AWS",
    "Azure",
    "Power BI",
    "Excel"
]

def extract_text_from_pdf(pdf_file):

    if pdfplumber is None:
        raise ImportError(
            "pdfplumber is required to extract PDF text. Install it with: "
            "pip install pdfplumber"
        )

    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text

def find_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) +  r"\b"
        if re.search(pattern,text):
            found_skills.append(skill)

    return found_skills
def calculate_match_score(resume_skills, job_skills):
   if not job_skills:
       return 0
   matched = set(resume_skills).intersection(set(job_skills))
   score = (
       len(matched) / len(set(job_skills))
   )*100
   return round(score,2)
def generate_suggestions(
        missing_skills,
        score
):
    suggestions = []
    if missing_skills:
        suggestions.append(
            "Consider learning:"
            + ", ".join(missing_skills)
        )

    if score<50:
        suggestions.append(
            "Add more job-related technical skills"
            "and projects."
        )

    elif score<80:
        suggestions.append(
            "Your resume is a moderate match."
            "Add more relevant skills."
        )
    else:
        suggestions.append(
            "Your resume is a strong match."
        )
        
    suggestions.append(
        "Add measurable achievements to your resume."
    )

    suggestions.append(
        "Highlight skills relevant to the job."
    )

    return suggestions

def analyzer_resume(
        resume_text,
        job_description
):
    resume_skills = find_skills(resume_text)
    job_skills = find_skills ( job_description)
    matched_skills = list(set(resume_skills).intersection(set(job_skills)))

    missing_skills = list(set(job_skills) - set(resume_skills))

    score = calculate_match_score(resume_skills, job_skills)

    suggestions = generate_suggestions(
        missing_skills,
        score
    )

    return{
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions

    }