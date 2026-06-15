# Create embeddings + store data:

from app.config import embedding_model


def store_data(collection, texts, tables, images, text_summaries, table_summaries, image_summaries):

    # Store Text Data:
    for i, summary in enumerate(text_summaries):

        embedding = embedding_model.encode(summary).tolist()

        collection.add(
                        ids=[f"text_{i}"],
                        embeddings=[embedding],
                        documents=[summary],
                        metadatas=[
                                    {
                                        "type": "text",
                                        "original_text": texts[i]
                                    }
                                  ]
                      )

    print("Text data stored successfully")

    # Store Table Data:
    for i, summary in enumerate(table_summaries):

        embedding = embedding_model.encode(summary).tolist()

        collection.add(
                        ids=[f"table_{i}"],
                        embeddings=[embedding],
                        documents=[summary],
                        metadatas=[
                                    {
                                        "type": "table",
                                        "original_table": tables[i]
                                    }
                                  ]
                      )

    print("Table data stored successfully")

    # Store Image Data:
    for i, summary in enumerate(image_summaries):

        embedding = embedding_model.encode(summary).tolist()

        collection.add(
                        ids=[f"image_{i}"],
                        embeddings=[embedding],
                        documents=[summary],
                        metadatas=[
                                    {
                                        "type": "image",
                                        "image_path": images[i]
                                    }
                                  ]
                    )

    print("Image data stored successfully")

    return "All embeddings stored successfully"