import os
from groq import Groq, APIConnectionError
from config import MODEL_NAME, GROQ_API_KEY
from prompts import QUESTION_PROMPT

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please add it to your .env file.")

client = Groq(api_key=GROQ_API_KEY)

def generate_questions(role):
    """
    Generate exactly 5 interview questions for a given role.
    """

    prompt = QUESTION_PROMPT.format(role=role)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert interviewer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=600
        )

        result = response.choices[0].message.content
    except APIConnectionError:
        result = "1. Tell me about yourself.\n2. Why are you interested in this role?\n3. Describe a technical challenge you solved.\n4. How do you approach teamwork and communication?\n5. Where do you see yourself in five years?"
    except Exception:
        result = "1. Tell me about yourself.\n2. Why are you interested in this role?\n3. Describe a technical challenge you solved.\n4. How do you approach teamwork and communication?\n5. Where do you see yourself in five years?"

    questions = []

    for line in result.split("\n"):

        line = line.strip()

        if line == "":
            continue

        if line[0].isdigit():

            if "." in line:
                line = line.split(".",1)[1].strip()

            elif ")" in line:
                line = line.split(")",1)[1].strip()

        questions.append(line)

    return questions[:5]