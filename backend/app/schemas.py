# Define API request format:

from pydantic import BaseModel

class QueryRequest(BaseModel):
    pdf_id: str
    question: str