FROM python:3.10-slim

WORKDIR /
# Build with your updated Dockerfile

# Install system dependencies (git is required for pip install git+...)
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir runpod torch transformers accelerate

# Clone Yuan3.0 repo or install model dependencies
RUN pip install git+https://github.com/Yuan-lab-LLM/Yuan3.0.git

# Copy handler
COPY handler.py /

CMD ["python3", "-u", "handler.py"]

