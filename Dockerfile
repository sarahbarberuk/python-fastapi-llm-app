# Use the official lightweight Python image
FROM python:3.11-slim

# Set working directory (in the container)
WORKDIR /llm-app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Start your app
CMD ["python", "run.py"]