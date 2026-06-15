# User uploads PDF
# User asks question
# Calls FastAPI backend

import streamlit as st
import requests

st.title("Multimodal ChatPDF App")


# Upload PDF:
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

pdf_id = None

if uploaded_file:

    files = {"file": uploaded_file}

    response = requests.post("http://localhost:8000/upload-pdf", files=files)

    data = response.json()

    pdf_id = data["pdf_id"]

    st.success("PDF uploaded successfully")
    st.write("PDF ID:", pdf_id)


# Ask Question:
question = st.text_input("Ask Question")

if st.button("Ask"):

    payload = {
                "pdf_id": pdf_id,
                "question": question
              }

    response = requests.post("http://localhost:8000/ask", json=payload)

    st.write(response.json()["answer"])
