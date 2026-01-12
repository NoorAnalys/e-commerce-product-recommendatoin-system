# Use an official lightweight Python image
FROM python:3.10-slim

WORKDIR /code

# Copy requirements specific to the ML service
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the ML app code
COPY ./app ./app

# Expose the internal port (we will map this in docker-compose)
EXPOSE 8000

# Command to run the ML service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]