FROM python:3.11-slim

# Disable .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install netcat for checking database readiness
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Command to wait for db, migrate, collect static files, and run the application
CMD bash -c "python manage.py migrate && python manage.py collectstatic --noinput && daphne -b 0.0.0.0 -p 8000 compete_wordle.asgi:application"

