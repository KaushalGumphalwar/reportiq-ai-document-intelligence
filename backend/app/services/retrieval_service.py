# Retrieve relevant content:

from app.config import embedding_model
import chromadb


def retrieve(query, pdf_id):

    client = chromadb.PersistentClient(path=f"vectorstores/{pdf_id}")

    collection = client.get_or_create_collection(name="pdf_data")

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
                                query_embeddings=[query_embedding],
                                n_results=3
                              )

    return results
