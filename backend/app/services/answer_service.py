# Generate final answer:

from app.config import model
from PIL import Image
import google.api_core.exceptions


def generate_answer(query, metadata_list):

    # first retrieved item type check:
    content_type = metadata_list[0]["type"]

    try:
        # TEXT RESPONSE (If text retrieved):
        if content_type == "text":

            combined_context = ""

            for metadata in metadata_list:
                combined_context += (metadata["original_text"] + "\n\n")

            response = model.generate_content(
                                                f"""
                                                You are a helpful PDF assistant.

                                                Answer the user's question using ONLY the provided context.

                                                If answer is not present in context, return:
                                                "Answer not found in document."

                                                Give concise and accurate answer.

                                                Question:
                                                {query}

                                                Context:
                                                {combined_context}
                                                """
                                            )

            return response.text

        # TABLE RESPONSE (If table retrieved):
        elif content_type == "table":

            combined_tables = ""

            for metadata in metadata_list:
                combined_tables += (metadata["original_table"] + "\n\n")

            response = model.generate_content(
                                                f"""
                                                You are a helpful PDF assistant.

                                                Answer the user's question using ONLY the provided table data.

                                                If answer is not present, return:
                                                "Answer not found in table."

                                                Question:
                                                {query}

                                                Table Data:
                                                {combined_tables}
                                                """
                                             )

            return response.text

        # IMAGE RESPONSE (If image retrieved):
        elif content_type == "image":

            # take first relevant image:
            image_path = metadata_list[0]["image_path"]

            image = Image.open(image_path)

            response = model.generate_content([
                                                f"""
                                                You are a helpful PDF assistant.

                                                Answer the user's question using ONLY this image.

                                                If answer is not visible in image, return:
                                                "Answer not found in image."

                                                Question:
                                                {query}
                                                """,
                                                image
                                            ])

            return response.text

        else:
            return "Unsupported content type"


    # Gemini quota exceeded fallback (If Gemini quota exceeds):
    except google.api_core.exceptions.ResourceExhausted:

        print("Gemini quota exceeded. Using fallback response.")

        if content_type == "text":

            combined_text = ""

            for metadata in metadata_list:
                combined_text += (metadata["original_text"] + "\n\n")

            return (
                     "Gemini quota exceeded currently.\n\n"
                     "Retrieved relevant text from PDF:\n\n"
                     f"{combined_text}"
                   )

        elif content_type == "table":

            combined_tables = ""

            for metadata in metadata_list:
                combined_tables += (metadata["original_table"] + "\n\n")

            return (
                     "Gemini quota exceeded currently.\n\n"
                     "Retrieved relevant tables from PDF:\n\n"
                     f"{combined_tables}"
                   )

        elif content_type == "image":

            return (
                     "Gemini quota exceeded currently.\n\n"
                     "Relevant image retrieved successfully, "
                     "but image-based answer generation is temporarily unavailable."
                   )

        else:
            return "Quota exceeded and unsupported content type."

    
    # UNEXPECTED ERROR (Any unexpected error):
    except Exception as e:

        print(f"Unexpected error: {e}")

        return ("Something went wrong while generating answer.")