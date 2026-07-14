import re
from groq import Groq, APIConnectionError

from config import GROQ_API_KEY, MODEL_NAME
from prompts import EVALUATION_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def evaluate_answer(question, answer):

    prompt = EVALUATION_PROMPT.format(
        question=question,
        answer=answer
    )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior HR interviewer who evaluates candidates fairly."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=700
        )

        result = response.choices[0].message.content
    except APIConnectionError:
        result = (
            "Score: 5/10\n\n"
            "Strengths\n"
            "Reasonable structure, but evaluation service is unavailable.\n\n"
            "Weaknesses\n"
            "Could not complete external grading because the Groq API connection failed.\n\n"
            "Suggestions\n"
            "Retry once your network or API access is restored.\n\n"
            "Overall Feedback\n"
            "Incomplete evaluation: connection error."
        )
    except Exception:
        result = (
            "Score: 5/10\n\n"
            "Strengths\n"
            "The candidate provided a response.\n\n"
            "Weaknesses\n"
            "Evaluation service failed to generate detailed feedback.\n\n"
            "Suggestions\n"
            "Check the app logs and retry.\n\n"
            "Overall Feedback\n"
            "Evaluation could not be completed due to an internal error."
        )

    score = 0

    match = re.search(r"Score\s*:\s*(\d+)", result)

    if match:
        score = int(match.group(1))

    return {
        "score": score,
        "feedback": result
    }