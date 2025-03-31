import sys
from pdf_utils import extract_text_from_pdf
from summarize import summarize_text
from generate_quiz import generate_quiz

def main():
    if len(sys.argv) != 2:
        print("사용법: python main.py <pdf파일경로>")
        return

    file_path = sys.argv[1]
    print("📥 PDF 읽는 중...")
    raw_text = extract_text_from_pdf(file_path)

    print("\n🧠 요약 중...")
    summary = summarize_text(raw_text)
    print("\n📋 요약 결과:\n", summary)

    print("\n📝 퀴즈 생성 중...")
    quiz = generate_quiz(summary)
    print("\n🎯 생성된 퀴즈:\n", quiz)

if __name__ == "__main__":
    main()
