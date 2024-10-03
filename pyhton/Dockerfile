# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY . /app

# Install dependencies
RUN pip install flask requests

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
