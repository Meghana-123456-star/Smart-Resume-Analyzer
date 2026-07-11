from utils.pdf_reader import extract_text_from_pdf

pdf_path = "uploads/resume.pdf"

try:
    text = extract_text_from_pdf(pdf_path)
    print(text)
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please add a resume.pdf file to the uploads/ folder")
except Exception as e:
    print(f"Error: {e}")