# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /code

# Install system dependencies required for MySQL and building Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire app folder
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# We use app.main:app because your main.py is inside the app/ folder
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]