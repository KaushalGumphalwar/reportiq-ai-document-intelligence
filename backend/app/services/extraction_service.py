from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.basic import chunk_elements
import re

# Clean extracted text chunks:
def clean_text(text):

    # If text is empty:
    if not text:
        return None

    # Remove starting/end spaces:
    text = text.strip()

    # Remove very small useless chunks:
    # Example:
    # "Home"
    # "Login"
    # "Page 1"
    
    if len(text) < 50:
        return None

    # Remove noisy keywords:
    unwanted_keywords = ["wikipedia", "free encyclopedia", "login", "sign up", "page"]

    lower_text = text.lower()

    for keyword in unwanted_keywords:
        if keyword in lower_text:
            return None

    # Remove timestamps:
    # Example:
    # 5/15/26, 9:16 AM
    text = re.sub(r"\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}\s*(AM|PM)", "", text)

    # Remove citation references:
    # Example:
    # [1], [2], [15]   
    text = re.sub(r"\[\d+\]", "", text)

    # Remove weird extraction symbols
    # Example:
    # !3]
    # !4!
    # !Z!  
    text = re.sub(r"!\w+\]?", "", text)

    # Remove standalone exclamation extraction noise 
    text = re.sub(r"!", "", text)  

    # Remove copyright/special symbols like ©)
    text = re.sub(r"[©®™]+[\)\]]*", "", text)

    # Remove extra spaces/newlines:  
    text = re.sub(r"\s+", " ", text)

    return text.strip()



# Extract PDF content:

def extract_pdf(file_path):

    # Step 1: Extract all PDF elements (Extract text/tables/images)
    pdf_elements = partition_pdf(
                                    filename=file_path,
                                    extract_images_in_pdf=True,
                                    infer_table_structure=True,
                                    strategy="hi_res"
                                )

    # Step 2: Chunk extracted content (Chunk extracted elements)
    chunks = chunk_elements(
                                pdf_elements,
                                max_characters=800,
                                overlap=100
                           )

    texts = []
    tables = []
    images = []

    # Step 3: Separate text/table/image
    for el in chunks:

        # TEXT:
        if el.category == "CompositeElement":

            cleaned_text = clean_text(el.text)

            if cleaned_text:
                texts.append(cleaned_text)
   
        # TABLE:     
        elif el.category == "Table":

            if hasattr(el.metadata, "text_as_html"):
                tables.append(el.metadata.text_as_html)
     
        # IMAGE:       
        elif el.category == "Image":

            if hasattr(el.metadata, "image_path"):
                images.append(el.metadata.image_path)

    return texts, tables, images