FROM python:3.10-slim

WORKDIR /

# Install dependencies
RUN pip install --no-cache-dir runpod torch transformers accelerate

# Clone Yuan3.0 repo or install model dependencies
RUN pip install git+https://github.com/Yuan-lab-LLM/Yuan3.0.git

# Copy handler
COPY handler.py /

CMD ["python3", "-u", "handler.py"]
