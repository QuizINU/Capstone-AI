from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_quiz(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 대학생을 위한 퀴즈 생성기야."},
            {"role": "user", "content": f"""
다음 내용을 바탕으로 객관식 문제 3개를 만들어줘.
각 문제는 보기 4개와 정답 표시를 포함해야 해.

내용:
{text}
"""}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
