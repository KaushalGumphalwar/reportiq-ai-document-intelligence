# API endpoints:

import time

from fastapi import FastAPI, UploadFile, File
from app.schemas import QueryRequest

from app.services.upload_service import save_pdf
from app.services.extraction_service import extract_pdf
from app.services.summary_service import (summarize_table, summarize_image)
from app.services.vectorstore_service import create_collection
from app.services.embedding_service import store_data
from app.services.retrieval_service import retrieve
from app.services.answer_service import generate_answer

app = FastAPI()

# Upload API:
@app.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    # Step 1: Save PDF
    pdf_id, file_path = save_pdf(file)

    # Step 2: Extract PDF content
    texts, tables, images = extract_pdf(file_path)

    print(f"Texts extracted: {len(texts)}")
    print(f"Tables extracted: {len(tables)}")
    print(f"Images extracted: {len(images)}")

    # Step 3: No Gemini for text
    text_summaries = texts

    # Step 4: Gemini only for tables
    table_summaries = []

    if tables:
        for table in tables:
            try:
                summary = summarize_table(table)
                table_summaries.append(summary)

                # avoid hitting Gemini rate limits
                time.sleep(5)

            except Exception as e:
                print(f"Table summarization error: {e}")
                table_summaries.append("Table summary failed")


    # Step 5: Gemini only for images
    image_summaries = []

    if images:
        for img in images:
            try:
                summary = summarize_image(img)
                image_summaries.append(summary)

                # avoid hitting Gemini rate limits
                time.sleep(5)

            except Exception as e:
                print(f"Image summarization error: {e}")
                image_summaries.append("Image summary failed")

    # Step 6: Create vector DB
    collection = create_collection(pdf_id)

    # Step 7: Store everything (store embeddings for all content, but only summaries for tables and images)
    store_data(collection, 
               texts, tables, images,
               text_summaries, table_summaries, image_summaries)

    return {
             "message": "PDF processed successfully",
             "pdf_id": pdf_id
           }

# Query API:
@app.post("/ask")
def ask_question(request: QueryRequest):

    results = retrieve(
                        request.question,
                        request.pdf_id
                      )

    if not results["metadatas"][0]:
        return {"answer": "No relevant content found"}

    # Retrieve top multiple metadata chunks:
    retrieved_metadata = results["metadatas"][0]

    answer = generate_answer(
                              request.question,
                              retrieved_metadata
                            )

    return {"answer": answer}