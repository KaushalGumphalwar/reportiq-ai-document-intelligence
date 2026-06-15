# Create separate vectorstore for each PDF:

import chromadb

def create_collection(pdf_id):

    client = chromadb.PersistentClient(path=f"vectorstores/{pdf_id}")

    collection = client.get_or_create_collection(name="pdf_data")

    return collection