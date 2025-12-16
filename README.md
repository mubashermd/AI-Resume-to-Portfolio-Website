# AI-Resume-to-Portfolio-Website
# AI-Generated Portfolio Website from Resume

🚀 An end-to-end AI-powered application that automatically converts a resume (PDF/DOCX) into a **professional, responsive portfolio website** using Large Language Models.

---

## 📌 Project Overview

Creating a portfolio website usually requires web development skills and design knowledge. This project solves that problem by using **AI + automation** to generate a complete portfolio website from a resume with **zero manual coding**.

**Flow:**

```
Resume (PDF/DOCX)
   ↓
Resume Text Extraction
   ↓
LLM #1 – Resume → Structured Website Content
   ↓
LLM #2 – Content → HTML / CSS / JavaScript
   ↓
Live Preview + ZIP Download
```

---

## ✨ Key Features

* 📄 Supports **PDF and DOCX resumes**
* 🤖 **Multi-stage LLM pipeline** for better accuracy
* 🎨 Multiple website themes (Modern, Minimal, Dark, Creative)
* 🌐 Generates clean **HTML, CSS, and JavaScript**
* 👀 Live website preview inside Streamlit
* 📦 Downloadable ZIP ready for deployment
* 🛡 Robust handling of LLM output inconsistencies

---

## 🏗 System Architecture

* **Streamlit UI** – User interaction & preview
* **Resume Parser** – PyPDF2, python-docx
* **LLM #1** – Converts resume into structured website content
* **LLM #2** – Generates website source code
* **ZIP Module** – Bundles website files

---

## 🧰 Tech Stack

| Layer            | Tools / Libraries         |
| ---------------- | ------------------------- |
| UI               | Streamlit                 |
| Document Parsing | PyPDF2, python-docx       |
| LLM              | Google Gemini (LangChain) |
| Backend          | Python                    |
| Packaging        | zipfile                   |
| Frontend Output  | HTML, CSS, JavaScript     |

---

## 🔄 Workflow

1. Upload resume (PDF or DOCX)
2. Extract resume text automatically
3. Generate structured website content using Gemini AI
4. Generate HTML, CSS, and JS files
5. Preview website inside the app
6. Download ZIP for deployment

---

## 📁 Output Files

* `index.html` – Website structure
* `style.css` – Styling and layout
* `script.js` – Interactivity

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-to-Portfolio-Website.git
cd AI-Resume-to-Portfolio-Website
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements

* Advanced resume parsing using NLP / NER
* Profile photo upload
* Animated templates
* One-click deployment to GitHub Pages / Netlify
* More theme options

---

## 📸 Demo

*(Add screenshots or GIF here)*

---

## 🙏 Acknowledgements

* **Innomatics Research Labs** for guidance and learning support
* **Saxon K Sha** for mentorship and inspiration

---

## 📬 Contact

If you find this project useful or want to collaborate, feel free to connect!

---

⭐ If you like this project, don’t forget to **star the repository**!
