# HireAI – AI-Powered Interview & Recruitment Platform

## Overview

HireAI is an AI-powered Interview Agent that conducts role-based technical interviews using Large Language Models (LLMs).The application generates interview questions based on the selected job role, evaluates candidate responses using AI, provides detailed feedback, calculates interview scores, and recommends whether the candidate should be hired or not,PDF report generation and a recruiter dashboard.

# 🎯 Objectives

- Automate technical interviews using AI.
- Evaluate candidate answers intelligently.
- Generate detailed interview feedback.
- Calculate candidate performance score.
- Recommend hiring decisions.
- Store interview history for recruiters.

# ✨ Features

### 👤 Candidate Registration

- Candidate Name
- Email
- Phone Number
- College Name
- Experience
- Job Role

### 🤖 AI Interview

- AI-generated interview questions
- Role-based questions
- Interactive interview process
- 5 technical questions
- Progress indicator
- Interview timer


### 📊 AI Evaluation

- AI evaluates every answer
- Technical skill analysis
- Communication evaluation
- Problem-solving evaluation
- Confidence analysis
- Individual question scores


### 📑 Final Report

- Overall Interview Score
- AI Feedback
- Hiring Recommendation
- Interview Transcript
- Download PDF Report


### 👨‍💼 Recruiter Dashboard

- View Interview History
- Search Candidates
- Filter by Job Role
- Candidate Scores
- Performance Charts


# 🛠️ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | User Interface |
| Groq API | AI Model |
| Llama 3.3 | Large Language Model |
| Pandas | Data Processing |
| Plotly | Dashboard Charts |
| ReportLab | PDF Generation |
| Python Dotenv | API Key Management |


# 📂 Project Structure

HireAI/
│
├── interview_agent.py
├── interview.py
├── evaluator.py
├── dashboard.py
├── report.py
├── utils.py
├── prompts.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── data/
│      interviews.csv
│
├── reports/
│
├── transcripts/
│
├── assets/
│
└── screenshots/

# ⚙️ Installation Guide

## Step 1

Clone Repository

```bash
git clone https://github.com/nehabanu2203/HireAI-Interview-Agent.git
```


## Step 2

Open Project Folder

```bash
cd HireAI-Interview-Agent
```


## Step 3

Create Virtual Environment

```bash
python -m venv venv
```


## Step 4

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```


## Step 5

Install Required Packages

```bash
pip install -r requirements.txt
```


## Step 6

Create `.env`

```
GROQ_API_KEY=YOUR_API_KEY
```


## Step 7

Run Project

```bash
streamlit run interview_agent.py
```
If streamlit isn't recognized:
```bash
python -m streamlit run interview_agent.py
```

# 📊 Output

The application provides

- Candidate Registration
- AI Interview Questions
- AI Evaluation
- Candidate Score
- Hiring Recommendation
- PDF Report
- Interview Transcript
- Recruiter Dashboard


# 🚀 Future Enhancements

- Resume Upload
- Voice-Based Interview
- Facial Emotion Detection
- Multi-language Interview
- Cloud Database
- Email Report Generation


## Recommended workflow for demos

- Start the app locally using the command above.
- Use the `Interview` sidebar, enter candidate info and start the interview.
- Answer questions and view evaluation results and final report.
- Use the `Recruiter Dashboard` to inspect and delete saved interview records.

## Troubleshooting

- If Streamlit fails to start, ensure the virtual environment is activated and dependencies are installed.
- If Groq API fails, the app falls back to default questions and a basic evaluation summary; check `GROQ_API_KEY` in your `.env`.
- If you see errors saving data, ensure the `data/` directory exists (the app creates it automatically on save).

# 👩‍💻 Developed By

**Neha Banu**

Department of Computer Science and Engineering (AI & ML)

Don Bosco Institute of Technology

GitHub:
https://github.com/nehabanu2203
