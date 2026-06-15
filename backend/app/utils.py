# Common reusable helper functions

import os
import uuid


def generate_pdf_id():
    return str(uuid.uuid4())


def create_folder(path):
    os.makedirs(path, exist_ok=True)