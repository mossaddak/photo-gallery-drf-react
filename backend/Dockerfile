FROM python:3.12-alpine

# Install build dependencies
RUN apk add --no-cache gcc python3-dev

# Python configuration
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Install Python dependencies first
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Start FastAPI
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]