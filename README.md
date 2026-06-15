# 📄 ReportIQ – AI-Based Document Intelligence Application

<p align="center">
  <img src="assets/architecture.png" width="900">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Gemini](https://img.shields.io/badge/LLM-Gemini-orange)
![RAG](https://img.shields.io/badge/Architecture-RAG-success)

</p>

---

# 🚀 Project Overview

**ReportIQ** is an AI-powered Document Intelligence Application that allows users to upload PDF documents and ask natural language questions about their content.

The system uses:

* 📄 PDF Parsing
* 🧠 Retrieval-Augmented Generation (RAG)
* 🔍 Semantic Search
* 📚 Chroma Vector Database
* 🤖 Google Gemini LLM
* ⚡ FastAPI Backend
* 🎨 Streamlit Frontend
* 🐳 Docker Containerization

to provide intelligent answers directly from uploaded documents.

---

# 🎯 Key Features

✅ Upload PDF documents

✅ Extract text from PDFs

✅ Generate vector embeddings

✅ Store embeddings in ChromaDB

✅ Semantic document retrieval

✅ Context-aware question answering

✅ Google Gemini integration

✅ FastAPI REST APIs

✅ Streamlit User Interface

✅ Dockerized deployment

---

# 🏗️ System Architecture

<p align="center">
  <img src="assets/architecture.png" width="1000">
</p>

---

# 📂 Project Structure

```text
ReportIQ-AI/
│
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── frontend/
│   ├── streamlit_app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── assets/
│   ├── architecture.png
│   ├── fastapi_swagger_ui_1.png
│   ├── fastapi_swagger_ui_2.png
│   ├── fastapi_swagger_ui_3.png
│   ├── fastapi_swagger_ui_4.png
│   ├── fastapi_swagger_ui_5.png
│   ├── fastapi_swagger_ui_6.png
│   ├── streamlit_app_1.png
│   ├── streamlit_app_2.png
│   ├── streamlit_app_3.png
│   └── streamlit_app_4.png
│
├── uploads/
├── vectorstores/
├── figures/
│
├── docker-compose.yml
├── .gitignore
├── README.md
└── .env
```

---

# 🛠️ Tech Stack

| Component            | Technology       |
| -------------------- | ---------------- |
| Programming Language | Python           |
| Backend              | FastAPI          |
| Frontend             | Streamlit        |
| Vector Database      | ChromaDB         |
| Embedding Model      | all-MiniLM-L6-v2 |
| LLM                  | Google Gemini    |
| Containerization     | Docker           |
| API Documentation    | Swagger UI       |

---

# ⚙️ Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run FastAPI Backend

Navigate to project root:

```bash
uvicorn backend.app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

# 🐳 Run Using Docker Compose

### Build Containers

```bash
docker compose build
```

### Start Containers

```bash
docker compose up
```

### Run in Detached Mode

```bash
docker compose up -d
```

### Stop Containers

```bash
docker compose down
```

---

# 📸 FastAPI Swagger UI

## Upload PDF Endpoint

<p align="center">
  <img src="assets/fastapi_swagger_ui_1.png" width="1000">
</p>

<p align="center">
  <img src="assets/fastapi_swagger_ui_2.png" width="1000">
</p>

<p align="center">
  <img src="assets/fastapi_swagger_ui_3.png" width="1000">
</p>

<p align="center">
  <img src="assets/fastapi_swagger_ui_4.png" width="1000">
</p>

<p align="center">
  <img src="assets/fastapi_swagger_ui_5.png" width="1000">
</p>

<p align="center">
  <img src="assets/fastapi_swagger_ui_6.png" width="1000">
</p>

---

# 📸 Streamlit User Interface

<p align="center">
  <img src="assets/streamlit_app_1.png" width="1000">
</p>

<p align="center">
  <img src="assets/streamlit_app_2.png" width="1000">
</p>

<p align="center">
  <img src="assets/streamlit_app_3.png" width="1000">
</p>

<p align="center">
  <img src="assets/streamlit_app_4.png" width="1000">
</p>

---

# 🔄 Workflow

```text
User Uploads PDF
        │
        ▼
PDF Processing
        │
        ▼
Text Extraction
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
User Question
        │
        ▼
Similarity Search
        │
        ▼
Relevant Context Retrieval
        │
        ▼
Gemini LLM
        │
        ▼
Final Answer
```

---

# 🎓 Learning Outcomes

Through this project I learned:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* FastAPI Development
* Streamlit Development
* Docker Containerization
* LLM Integration
* Production Project Structure
* API Design
* End-to-End AI Application Development

---

# 👨‍💻 Author

**Kaushal Gumphalwar**

Machine Learning | Generative AI | LLM Applications | FastAPI | Docker

GitHub: https://github.com/KaushalGumphalwar

---

# ⭐ If you found this project useful

Please consider giving this repository a star ⭐ on GitHub.
