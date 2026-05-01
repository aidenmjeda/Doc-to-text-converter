
---

# Document to Text Converter (DOCX + PDF)

This project converts `.docx` and `.pdf` files into clean plain text files. It is designed for use in AI pipelines such as LLMs (Ollama, OpenAI) and RAG systems.

It works across Windows, macOS, and Linux using Python.

---

# First-Time Setup

## 1. Clone the repository

```bash
git clone https://github.com/aidenmjeda/Doc-to-text-converter.git
cd Doc-to-text-converter
```

---

## 2. Create a virtual environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows (CMD)

```bash
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

---

## 3. Install dependencies

```bash
pip install python-docx pdfminer.six
```

---

## 4. Run the program

```bash
python main.py "/path/to/your/file.pdf"
```

Example:

```bash
python main.py "/Users/aiden/Downloads/VPN_Laboruebung_Site2Site.pdf"
```

---

# Daily Usage (After Setup)

After the first installation, you only need:

## Step 1: Activate environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Step 2: Run conversion

```bash
python main.py "file.pdf"
```

or

```bash
python main.py "file.docx"
```

---

## Step 3: Get output

The result will be saved as:

```text
output.txt
```

---

# How It Works

The script automatically:

1. Detects file type (.pdf or .docx)
2. Extracts text using:

   * `pdfminer.six` for PDFs
   * `python-docx` for Word files
3. Converts content into clean plain text
4. Saves it into `output.txt`

---

# Supported Platforms

* Windows
* macOS
* Linux

---

# Requirements

Install dependencies:

```bash
python-docx
pdfminer.six
```

---

# Notes

* Scanned PDFs (images) will not extract text correctly.
  For scanned documents, OCR (e.g. Tesseract) is required.
* Always use a virtual environment to avoid dependency conflicts.

---

# Example Workflow

```bash
cd Doc-to-text-converter
source venv/bin/activate
python main.py "document.pdf"
```

---

# Output Example

```text
output.txt
```

Contains extracted plain text ready for:

* AI models
* embeddings
* search systems
* chatbots
 
 # Aiden Mjeda
---

