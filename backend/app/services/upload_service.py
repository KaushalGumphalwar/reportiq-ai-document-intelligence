# Save uploaded PDF:

import os
from app.utils import generate_pdf_id


def save_pdf(uploaded_file):

    pdf_id = generate_pdf_id()

    file_path = f"uploads/{pdf_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.file.read())

    return pdf_id, file_path
