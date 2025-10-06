# Start from Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc g++ libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Pre-pull Docker images for code execution
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update && apt-get install -y docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

# Pre-pull the required Docker images
RUN docker pull python:3.9-slim
RUN docker pull gcc:latest

# Copy requirements
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all app files
COPY . /app/

# Create a non-root user for security
RUN useradd -m -r appuser && chown -R appuser:appuser /app
USER appuser

# Run migrations + import problems
RUN python manage.py migrate
RUN python manage.py import_problems

# Start app with gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120"]