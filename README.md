# AI Resume to Portfolio Website

A Streamlit application that turns a resume into a downloadable personal portfolio website. Upload a PDF or DOCX resume, choose a visual theme, and Gemini generates the site's HTML, CSS, and JavaScript.

## Problem Statement

Creating a personal portfolio from a resume is repetitive and can require web-development experience. This project automates the first draft: it extracts resume content, converts it into a structured portfolio specification, and produces a static website that the user can preview and download.

## Architecture

```text
PDF/DOCX resume + selected theme
              |
              v
      Streamlit user interface
              |
              v
      Resume text extraction
     (PyPDF2 / python-docx)
              |
              v
 Gemini call 1: structured portfolio content
              |
              v
 Gemini call 2: HTML + CSS + JavaScript
              |
       +------+------+
       |             |
       v             v
  In-app preview   ZIP download
                 (index.html, style.css, script.js)
```

## Tech Stack

- Python 3.12+
- Streamlit for the web interface
- LangChain and Google Gemini (`gemini-2.5-flash`) for generation
- PyPDF2 for PDF text extraction
- python-docx for DOCX text extraction
- python-dotenv for environment-variable management

## Features

- Upload resumes in PDF or DOCX format.
- Extract and display resume text before generation.
- Choose from Modern, Minimal, Dark, and Creative themes.
- Generate a structured portfolio specification from the resume.
- Generate separate HTML, CSS, and JavaScript assets.
- Preview the generated website in the app.
- Download a ready-to-use ZIP archive containing the website files.

## LLM Workflow

This application uses a two-step LLM workflow rather than a retrieval-augmented generation (RAG) pipeline:

1. The uploaded resume is parsed into plain text locally.
2. Gemini transforms the text into a structured portfolio brief, including professional summary, skills, experience, projects, education, and achievements.
3. A second Gemini request converts that brief and the selected theme into three fenced code blocks: HTML, CSS, and JavaScript.
4. The app extracts the code blocks, renders the HTML preview, and packages all three files into a ZIP download.

No external knowledge base, embeddings, vector database, or document retrieval step is currently used. A RAG layer could be added later for enriching the portfolio with verified project information or reusable design guidance.

## Screenshots

Add screenshots to a `screenshots/` folder and replace the placeholders below when available.

| Resume upload and theme selection | Generated website preview |
| --- | --- |
| `screenshots/upload.png` | `screenshots/preview.png` |

## Installation

1. Clone the repository and open it in a terminal.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r website\files\requirements.txt
   ```

4. Create `website/files/.env` with your Google Gemini API key:

   ```env
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

## How to Run

From the project root, with the virtual environment activated:

```powershell
python -m streamlit run website\files\app.py
```

Streamlit opens the app in your browser. Upload a PDF or DOCX resume, select a theme, click **Generate Portfolio Website**, then preview or download the resulting ZIP.

## Results

The app produces a static portfolio starter site with:

- `index.html` for page structure and content
- `style.css` for visual styling
- `script.js` for client-side behavior

The generated ZIP can be opened locally or deployed to any static-hosting service. Because the content is AI-generated from the uploaded resume, review and refine it before publishing.

## Future Improvements

- Add robust validation for missing API keys, empty resumes, and unreadable files.
- Render CSS and JavaScript in the preview alongside the HTML.
- Add editable generated content before export.
- Add screenshot capture and a gallery of generated sites.
- Introduce RAG with a user-controlled knowledge base for projects, links, and writing style.
- Support more document formats and OCR for scanned PDFs.
- Add automated tests and dependency version pinning.
- Add deployment options for GitHub Pages, Netlify, or Vercel.
