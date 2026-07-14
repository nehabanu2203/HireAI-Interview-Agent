Demo script — HireAI

1) Start app

- Command (from project root):

```powershell
.\venv\Scripts\python.exe -m streamlit run interview_agent.py --server.headless true --server.address 127.0.0.1
```

- Open http://127.0.0.1:8501

2) Walkthrough (2-3 minutes)

- Sidebar: show `Interview`, `Recruiter Dashboard`, `About`.
- Interview flow:
  - Fill candidate name/email/phone/role/experience and click `Start Interview`.
  - The app generates five questions (Groq API or fallback defaults).
  - Type an answer and click `Submit Answer`.
  - Show the AI evaluation, score metric, and feedback expander.
  - Use `Previous`/`Next` to edit answers and resubmit.
  - After all questions, arrive at the final results page with overall score, recommendation, and downloadable transcript/PDF.
- Recruiter Dashboard:
  - Show saved interviews, metrics, charts, and delete controls.

3) Key talking points (for interviews)

- Architecture: single-file Streamlit app with modular helpers (`interview.py`, `evaluator.py`, `utils.py`, `dashboard.py`).
- State management: uses `st.session_state` to persist interview progress and answers across reruns.
- External integrations: Groq API for question generation and evaluation; fallbacks for offline/demo mode.
- Data persistence: simple CSV (`data/interviews.csv`) to keep the project lightweight; tradeoffs vs using a DB.
- Error handling: graceful fallback when API or network fails; user-visible warnings.
- Next improvements: CI and unit tests, secure secret handling, deploy to Streamlit Cloud, use a lightweight DB for concurrency.

4) Demo tips

- If the Groq API is not available, explain that the app uses built-in fallback questions and returns a placeholder evaluation.
- Emphasize recoverability: the app never blocks the UI because of external failures.

5) Short script (what to say)

- "This project demonstrates a lightweight interview platform built with Streamlit. It generates questions from an LLM, evaluates answers, and produces a PDF report. For reliability, networked calls fall back to deterministic defaults when needed. Data is stored in a CSV for simplicity, and the recruiter dashboard provides quick analytics and record management."


