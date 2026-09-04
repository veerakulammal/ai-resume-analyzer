import streamlit as st
from analyzer import extract_text_from_pdf , analyzer_resume

st.set_page_config(
    page_title = "AI Resume analyzer",
     page_icon="📄",
     layout = "wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

st.divider()

resume_file = st.file_uploader(
    "Upload your resume (PDF format only)",
    type=["pdf"]
)

job_description = st.text_area (
    "📋 Paste Job Description",
    height = 250,
    placeholder="Paste the job requirements here..."
)
if st.button("Analyze Resume"):
    if resume_file is None:
        st.warning("Please upload your Resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please enter a job description.")
        st.stop()

    resume_text = extract_text_from_pdf(resume_file)


    if not resume_text.strip():
        st.error("could not extract text from the PDF.")
        st.stop()

    result=analyzer_resume(
        resume_text,
        job_description
    )

    st.success("Resume analysis Completed!")

    st.divider()

    st.subheader("📊 Resume Match Score")

    score = result["score"]

    st.progress(score / 100)

    st.write(f"### {score}%")

    if score >= 80:
        st.success("Excellent Match!")

    elif score>=60:
        st.info("Good Match!")
    elif score>=40:
        st.warning("Average Match!")

    else:
        st.error("Low Match!")

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("✅ Skills Found")

        for skill in result["matched_skills"]:
            st.write("✔️", skill)

    with col2:
        st.subheader("❌ Missing Skills")

        for skill in result["missing_skills"]:
            st.write("❌", skill)

    st.divider()

    st.subheader("💡 Suggestions")

    for suggestion in result["suggestions"]:
         st.write("👉", suggestion)

    with st.expander("📄 View Resume Text"):
        st.write(resume_text)