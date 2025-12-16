import streamlit as st
import zipfile
import os
import io

from PyPDF2 import PdfReader
from docx import Document
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# CONFIG 
load_dotenv()

st.set_page_config(page_title="AI Portfolio Generator", layout="wide")
st.title("AI-Generated Portfolio Website from Resume")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# RESUME EXTRACTORS 

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# LLM INITIALIZATION 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    google_api_key=GEMINI_API_KEY
)

# LLM #1 : RESUME -> WEBSITE PROMPT 

def llm_generate_prompt(resume_text, theme):
    prompt = f"""
You are a senior web designer.
Convert the following resume into a structured portfolio website specification.

Extract:
- Name
- Professional summary
- Skills
- Experience
- Projects
- Education
- Achievements

Design theme: {theme}

Resume Content:
{resume_text}

Return clean structured content only.
"""
    return llm.invoke(prompt).content

# LLM #2 : PROMPT -> HTML/CSS/JS 

def safe_extract_block(text, lang):
    """Safely extract ```lang``` code blocks from LLM output"""
    start_token = f"```{lang}"
    if start_token not in text:
        return ""
    try:
        return text.split(start_token, 1)[1].split("```", 1)[0].strip()
    except IndexError:
        return ""


def llm_generate_code(structured_prompt, theme):
    prompt = f"""
Generate a modern, responsive portfolio website using ONLY:
- HTML
- CSS
- JavaScript

Theme: {theme}

Rules:
- Output MUST contain three fenced code blocks
- Use EXACT labels: ```html, ```css, ```js
- No explanations, no markdown text outside code blocks

Content:
{structured_prompt}
"""

    response = llm.invoke(prompt).content

    html = safe_extract_block(response, "html")
    css = safe_extract_block(response, "css")
    js = safe_extract_block(response, "js")

    # Fallback if JS block is missing
    if js == "":
        js = "console.log('Portfolio loaded');"

    return html, css, js

# STREAMLIT UI 
col1, col2 = st.columns([2, 1])

with col2:
    theme = st.selectbox(
        "Select Website Theme",
        ["Modern", "Minimal", "Dark", "Creative"]
    )

with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("", resume_text, height=250)

    if st.button("Generate Portfolio Website"):
        with st.spinner("Generating website using Gemini AI..."):
            structured_prompt = llm_generate_prompt(resume_text, theme)
            html, css, js = llm_generate_code(structured_prompt, theme)

        # --------- PREVIEW ---------
        st.subheader("Website Preview")
        st.components.v1.html(html, height=500, scrolling=True)

        # --------- ZIP EXPORT ---------
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as z:
            z.writestr("index.html", html)
            z.writestr("style.css", css)
            z.writestr("script.js", js)

        st.download_button(
            label="Download Website ZIP",
            data=zip_buffer.getvalue(),
            file_name="portfolio_website.zip",
            mime="application/zip"
        )
