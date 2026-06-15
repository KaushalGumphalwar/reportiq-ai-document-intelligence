# Use lightweight Python image:
FROM python:3.10-slim

# Install Linux dependencies:
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
# All project files will be copied here
WORKDIR /app

# Copy requirements file first
# This helps Docker cache dependencies
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install CPU version of PyTorch first
# This avoids downloading huge NVIDIA CUDA packages
# Install CPU versions matching local environment
RUN pip install torch==2.11.0 torchvision==0.26.0 \
    --index-url https://download.pytorch.org/whl/cpu

# Install all Python dependencies:
RUN pip install -r requirements.txt

# Copy complete project code into container:
COPY . .

# Create uploads folder
# PDFs will be stored here
RUN mkdir -p uploads

# Create vectorstore folder
# Chroma DB data will be stored here
RUN mkdir -p vectorstores

# Expose FastAPI port:
EXPOSE 8000

# Start FastAPI server when container runs:
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]