

# 📝 IEEEscribe – IEEE Research Paper Generator 
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?logo=fastapi)
![Gemini API](https://img.shields.io/badge/Powered%20by-Gemini%20API-4285F4?logo=google)
![LaTeX](https://img.shields.io/badge/Format-IEEE%20LaTeX-008080?logo=latex)
![Status](https://img.shields.io/badge/Status-Active-success)
![Pull Requests](https://img.shields.io/badge/PRs-Welcome-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Web-orange)

## 📌 Overview

**IEEEscribe** is a web-based tool that generates IEEE-format research papers using the **Gemini API**.
It produces **humanized, plagiarism-free content**, integrates seamlessly with an IEEE LaTeX template, and outputs both `.tex` and `.pdf` files — all in **seconds**.

---

## 🚀 Features

* 🎯 **Custom Input Form** – Title, authors, keywords, and section details.
* ⚡ **Gemini API Integration** – High-quality, context-aware content generation.
* 📝 **IEEE LaTeX Template Merging** – Auto-fills your content into the IEEE format.
* 📄 **Dual Output** – Download as `.tex` (editable) or `.pdf` (ready-to-share).
* 🔒 **Secure API Handling** – No keys stored in frontend or README.
* 💻 **FastAPI Backend** – For efficient and scalable content generation.

---

## 🛠️ Setup

### 1️⃣ Create and activate a Python virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2️⃣ Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Never commit your API key** to GitHub.

### 4️⃣ Ensure LaTeX is installed

Make sure `pdflatex` is installed and available in your system PATH.

---

## ▶️ Running the App

1. Start the backend:

```powershell
uvicorn app.main:app --reload
```

2. Open `frontend/index.html` in your browser.

---

## 📖 Usage

1. Fill out the research paper details in the form.
2. Click **Generate Paper**.
3. Download the generated `.tex` or `.pdf`.

---

## 🧠 Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **AI Model:** Gemini API (Google AI)
* **Document Generation:** LaTeX + `pdflatex`

---

## ⚠️ Notes

* All processing happens **in-memory** — no database required.
* You need an active **Gemini API key** from Google AI Studio.
* Designed for **academic research workflows**.

---




