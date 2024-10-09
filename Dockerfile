# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create the uploads directory
RUN mkdir -p /app/uploaded_files

# Add the user-local bin directory to the PATH
ENV PATH="/home/appuser/.local/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the outside world
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_DEBUG=1

# Run the application as root
CMD ["python3", "-m", "flask", "run"]