# app/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import shutil

from app.pdf_utils import extract_text_from_pdf
from app.summarize import summarize_text
from app.generate_quiz import generate_quiz

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 1. PDF → 텍스트 추출
    text = extract_text_from_pdf(file_path)

    # 2. 요약
    summary = summarize_text(text)

    # 3. 퀴즈 생성
    quiz = generate_quiz(summary)

    return JSONResponse({
        "filename": file.filename,
        "summary": summary,
        "quiz": quiz
    })
