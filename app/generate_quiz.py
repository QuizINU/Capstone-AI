import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로딩
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

def generate_quiz(text: str) -> list:
    """
    주어진 텍스트를 기반으로 GPT에게 객관식 퀴즈를 요청하고
    JSON 형태로 파싱하여 반환한다.
    """
    prompt = f"""
You are a helpful assistant that creates university-level multiple-choice quizzes from lecture text.

Based on the following content, generate 3 multiple-choice questions.

Each question should include:
- a "question" field
- a "choices" array of 4 options
- an "answer" field with the correct option

Return ONLY a valid JSON array like:
[
  {{
    "question": "...",
    "choices": ["...", "...", "...", "..."],
    "answer": "..."
  }},
  ...
]

Lecture Content:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a quiz generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    json_string = response.choices[0].message.content.strip()

    try:
        quiz_data = json.loads(json_string)
        return quiz_data
    except json.JSONDecodeError:
        return [{"error": "JSON parsing failed", "raw_output": json_string}]
