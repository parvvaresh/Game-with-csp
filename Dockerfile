# Use Python as base (you can change version if needed)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything into container
COPY . /app

# Run the main file
CMD ["python", "main.py"]
