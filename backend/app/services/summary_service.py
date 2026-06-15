# Generate summaries:

import google.generativeai as genai

from app.config import model
from PIL import Image


def summarize_table(table_html):

    prompt = f"""
                 Summarize this table in concise form: {table_html}
              """

    response = model.generate_content(prompt)

    return response.text


def summarize_image(image_path):

    image = Image.open(image_path)

    response = model.generate_content(["Describe this image in detail", image])

    return response.text