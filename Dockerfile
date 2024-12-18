# Use Python 3.12 slim image for a lightweight container
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080

# Set a consistent working directory
WORKDIR /app

# Install system dependencies (necessary for psycopg2-binary, etc.)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better caching
COPY requirements.txt /app/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Inform Docker about the exposed port
EXPOSE ${PORT}

# Use Gunicorn to serve the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "manager.wsgi:application"]
