# Use the official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask application code
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

