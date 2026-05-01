import sys
from docx import Document
from pdfminer.high_level import extract_text
import os


def extract_docx_text(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_pdf_text(file_path):
    return extract_text(file_path)


def convert_to_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    ext = file_path.lower().split(".")[-1]

    if ext == "docx":
        return extract_docx_text(file_path)
    elif ext == "pdf":
        return extract_pdf_text(file_path)
    else:
        raise ValueError("Unsupported file type")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = convert_to_text(file_path)

    output_file = "output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Done. Saved to {output_file}")