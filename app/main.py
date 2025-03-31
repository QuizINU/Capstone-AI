from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import shutil

from app.pdf_utils import extract_text_from_pdf
from app.summarize import summarize_text
from app.generate_quiz import generate_quiz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 나중에 실제 배포 시 프론트 주소만 명시할 것
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)
    summary = summarize_text(text)
    quiz = generate_quiz(summary)

    return JSONResponse({
        "filename": file.filename,
        "summary": summary,
        "quiz": quiz
    })
