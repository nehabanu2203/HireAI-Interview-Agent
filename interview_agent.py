import streamlit as st
import pandas as pd
import time
from datetime import datetime

from interview import generate_questions
from evaluator import evaluate_answer
from report import generate_pdf
from dashboard import save_interview, show_dashboard
from utils import calculate_recommendation
from utils import (
    calculate_average,
    calculate_recommendation,
    skill_breakdown
)
st.set_page_config(
    page_title="HireAI - AI Recruitment Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "started" not in st.session_state:
    st.session_state.started = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "answers" not in st.session_state:
    st.session_state.answers = []

if "results" not in st.session_state:
    st.session_state.results = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "saved" not in st.session_state:
    st.session_state.saved = False

with st.sidebar:
    st.title("🤖 HireAI")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Interview",
            "Recruiter Dashboard",
            "About"
        ]
    )

    st.markdown("---")

    st.info(
        """
        Built using

        • Python

        • Streamlit

        • Groq API

        • Llama 3.3

        • ReportLab
        """
    )

    st.subheader("AI-Powered Interview & Recruitment Platform")
    st.write("""
This application conducts AI-powered mock interviews.

Features

✅ AI Question Generation

✅ AI Evaluation

✅ Candidate Scoring

✅ Hiring Recommendation

✅ Recruiter Dashboard

✅ PDF Report

✅ Interview Transcript
""")

if page == "About":
    st.title("HireAI")
    st.subheader("AI-Powered Interview & Recruitment Platform")
    st.markdown("---")
    st.write(
        "This app uses AI-powered Interview Agent that conducts role-based technical interviews using Large Language Models (LLMs).The application generates interview questions based on the selected job role, evaluates candidate responses using AI, provides detailed feedback, calculates interview scores, and recommends whether the candidate should be hired or not,PDF report generation and a recruiter dashboard.")


elif page == "Recruiter Dashboard":
    show_dashboard()

else:
    if not st.session_state.started:
        st.title("HireAI")
        st.subheader("AI-Powered Interview Platform")
        st.markdown("---")

        with st.form("candidate_form"):
            col1, col2 = st.columns(2)

            with col1:
                candidate = st.text_input("Candidate Name")
                email = st.text_input("Email")
                phone = st.text_input("Phone Number")

            with col2:
                college = st.text_input("College")
                experience = st.selectbox(
                    "Experience",
                    [
                        "Fresher",
                        "1-2 Years",
                        "3-5 Years",
                        "5+ Years"
                    ]
                )

                role = st.selectbox(
                    "Job Role",
                    [
                        "Python Developer",
                        "Java Developer",
                        "AI Engineer",
                        "Data Analyst",
                        "Software Engineer",
                        "Full Stack Developer"
                    ]
                )

            submit = st.form_submit_button("🚀 Start Interview")

            if submit:
                if candidate == "":
                    st.error("Candidate name is required.")
                else:
                    with st.spinner("Generating AI Questions..."):
                        questions = generate_questions(role)

                    st.session_state.questions = questions
                    st.session_state.started = True
                    st.session_state.current_question = 0
                    st.session_state.answers = []
                    st.session_state.results = []
                    st.session_state.start_time = time.time()
                    st.session_state.name = candidate
                    st.session_state.email = email
                    st.session_state.phone = phone
                    st.session_state.college = college
                    st.session_state.role = role
                    st.session_state.experience = experience

                    st.rerun()

if st.session_state.started:

    total_questions = len(st.session_state.questions)

    current = st.session_state.current_question

    if current < total_questions:

        elapsed = int(time.time() - st.session_state.start_time)

        minutes = elapsed // 60

        seconds = elapsed % 60

        col1, col2 = st.columns([4,1])

        with col1:

            st.header(f"Question {current+1} of {total_questions}")

        with col2:

            st.metric(
                "Interview Time",
                f"{minutes:02}:{seconds:02}"
            )

        progress = (current+1)/total_questions

        st.progress(progress)

        st.markdown("---")

        question = st.session_state.questions[current]

        st.subheader("Interview Question")

        st.info(question)

        answer = st.text_area(
            "Type your answer below",
            height=220,
            value=st.session_state.answers[current] if current < len(st.session_state.answers) else "",
            key=f"answer_{current}"
        )

        col_prev, col_submit, col_next = st.columns([1,1,1])
        prev_clicked = False
        next_clicked = False

        if current > 0:
            prev_clicked = col_prev.button("⏮ Previous Question")

        submit_clicked = col_submit.button("Submit Answer")

        if current < total_questions - 1:
            next_clicked = col_next.button("➡ Next Question")

        if prev_clicked:
            st.session_state.current_question -= 1
            st.rerun()

        if submit_clicked:
            if answer.strip() == "":
                st.warning("Please answer the question.")
            else:
                with st.spinner("AI is evaluating your answer..."):
                    result = evaluate_answer(
                        question,
                        answer
                    )

                if current < len(st.session_state.answers):
                    st.session_state.answers[current] = answer
                    st.session_state.results[current] = result
                else:
                    st.session_state.answers.append(answer)
                    st.session_state.results.append(result)

                st.success(
                    f"Question {current+1} Evaluated!"
                )

                st.metric(
                    "Score",
                    f"{result['score']}/10"
                )

                with st.expander("AI Feedback"):
                    st.write(result["feedback"])

                if current < total_questions - 1:
                    st.session_state.current_question += 1
                else:
                    st.session_state.current_question = total_questions

                st.rerun()

        if next_clicked:
            if current < len(st.session_state.answers):
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.warning("Submit your answer before moving to the next question.")

if st.session_state.started and \
   st.session_state.current_question >= len(st.session_state.questions):

    st.balloons()

    st.title("🎉 Interview Completed")

    average_score = calculate_average(st.session_state.results)

    recommendation = calculate_recommendation(average_score)

    skills = skill_breakdown(st.session_state.results)

    end_time = int(time.time() - st.session_state.start_time)

    minutes = end_time // 60
    seconds = end_time % 60

    st.metric("Overall Score", f"{average_score}/10")

    st.metric("Interview Duration", f"{minutes:02}:{seconds:02}")

    st.success(f"Recommendation : {recommendation}")

    st.markdown("---")

    st.subheader("📊 Skill Breakdown")

    col1,col2 = st.columns(2)

    with col1:

        st.metric("Technical", skills["Technical"])

        st.metric("Communication", skills["Communication"])

    with col2:

        st.metric("Problem Solving", skills["Problem Solving"])

        st.metric("Confidence", skills["Confidence"])

    st.markdown("---")

    st.subheader("Detailed Feedback")

    transcript = ""

    feedbacks = []

    for i in range(len(st.session_state.questions)):

        st.expander(f"Question {i+1}", expanded=False).write(
            f"""
Question

{st.session_state.questions[i]}

Answer

{st.session_state.answers[i]}

Feedback

{st.session_state.results[i]['feedback']}
"""
        )

        transcript += f"Question {i+1}\n"
        transcript += st.session_state.questions[i] + "\n\n"

        transcript += "Answer\n"
        transcript += st.session_state.answers[i] + "\n\n"

        transcript += st.session_state.results[i]["feedback"] + "\n\n"

        transcript += "-"*70 + "\n"

        feedbacks.append(
            st.session_state.results[i]["feedback"]
        )

    if not st.session_state.saved:
        save_interview(
            st.session_state.name,
            st.session_state.email,
            st.session_state.role,
            st.session_state.experience,
            average_score,
            recommendation
        )
        st.session_state.saved = True

    pdf = generate_pdf(

        st.session_state.name,

        st.session_state.role,

        average_score,

        recommendation,

        feedbacks

    )

    st.download_button(

        "📄 Download Transcript",

        transcript,

        file_name="Interview_Transcript.txt",

        mime="text/plain"

    )

    with open(pdf,"rb") as f:

        st.download_button(

            "⬇ Download PDF Report",

            data=f,

            file_name=pdf,

            mime="application/pdf"

        )

    if st.button("🔄 Start New Interview"):

        for key in list(st.session_state.keys()):

            del st.session_state[key]

        st.rerun()