# Use lightweight Python image to reduce image size:
FROM python:3.10-slim

# Install Linux System Dependencies:
# libgl1           -> Required by OpenCV (cv2)
# libglib2.0-0     -> Required by OpenCV and image processing
# poppler-utils    -> Required by pdf2image
# tesseract-ocr    -> Required for OCR text extraction
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Set Working Directory Inside Container
# All project files will be copied here i.e. into /app
WORKDIR /app

# Copy Requirements File First (This helps Docker cache dependencies):
COPY requirements.txt .

# Upgrade pip:
RUN pip install --upgrade pip

# Install CPU Version of PyTorch (This avoids downloading huge NVIDIA CUDA packages)
# Reduces image size significantly
RUN pip install torch==2.11.0 torchvision==0.26.0 \
    --index-url https://download.pytorch.org/whl/cpu

# Install all Python dependencies:
RUN pip install -r requirements.txt

# Copy Complete Project Code Into Container:
COPY . .

# Create Required Directories
# Create uploads folder: PDFs will be stored here
# Create vectorstore folder: Chroma DB data will be stored here
RUN mkdir -p uploads  
RUN mkdir -p vectorstores

# Expose Streamlit Port
# Default Streamlit Port = 8501
EXPOSE 8501

# Start Streamlit Application
# --server.address=0.0.0.0
# Makes Streamlit accessible outside container
# --server.port=8501
# Explicitly sets Streamlit port
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]