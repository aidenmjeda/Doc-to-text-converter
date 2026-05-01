from docx import Document
from pdfminer.high_level import extract_text
import os

def extract_docx_text(file_path):
    """Extract text from a .docx file"""
    doc = Document(file_path)
    full_text = []

    for para in doc.paragraphs:
        full_text.append(para.text)

    return "\n".join(full_text)


def extract_pdf_text(file_path):
    """Extract text from a .pdf file"""
    text = extract_text(file_path)
    return text


def convert_to_text(file_path):
    """Auto-detect file type and convert to plain text"""

    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    file_extension = file_path.lower().split(".")[-1]

    if file_extension == "docx":
        return extract_docx_text(file_path)

    elif file_extension == "pdf":
        return extract_pdf_text(file_path)

    else:
        raise ValueError("Unsupported file type. Use .docx or .pdf")


# Example usage
if __name__ == "__main__":
    file_path = "your_file.docx"  # or "your_file.pdf"

    text = convert_to_text(file_path)

    # Save output to a .txt file
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Conversion done. Saved as output.txt")