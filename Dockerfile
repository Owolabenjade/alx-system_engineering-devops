# Use a Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir flask==2.1.0

# Expose port 80
EXPOSE 80

# Run the application
CMD ["python", "app.py"]

