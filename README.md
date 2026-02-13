# APA7_RAG_Local
# ⚡ AI-Powered APA 7 Bibliography Generator

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_API-blue)

A next-gen academic tool that generates APA 7 citations from PDF research papers using **Google Gemini 2.0 Flash & Pro** models via a robust **Microservice Architecture**.

## 🚀 Features
* **Microservices:** Decoupled Frontend (Streamlit) and Backend (FastAPI).
* **Multi-Model Support:** Supports Gemini 2.0 Flash, 1.5 Pro, and experimental models.
* **Auto-Fallback:** Automatically switches to lightweight models (Flash-Lite) if the primary model hits rate limits.
* **RAG-Ready:** Uses `pymupdf4llm` for intelligent PDF text extraction.

## 🛠️ Setup

1.  **Clone Repo:**
    ```bash
    git clone [(https://github.com/Aylinee/APA7_RAG_Local)]
    cd REPO
    ```
2.  **Install Deps:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure API Key:**
    Create a `.env` file in the `backend/` folder:
    ```ini
    GEMINI_API_KEY=your_google_api_key_here
    ```

## ▶️ Usage

**Terminal 1 (Backend):**
```bash
cd backend
python main.py
  ```

**Terminal 2 (Frontend):**
```bash
cd frontend
streamlit run app.py
  ```

📄 License
MIT License


Love academic issues 
