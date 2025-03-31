from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 대학 강의노트를 요약해주는 조교야."},
            {"role": "user", "content": f"다음 내용을 요약해줘:\n\n{text}"}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
