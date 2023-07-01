# Use an official Python runtime as the base image
FROM python:3.9-slim

# Updating linux package lists
RUN apt-get update && apt-get install -y --no-install-recommends tk-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the container
COPY /app .

# Expose the port that is to be used when running the container
EXPOSE 5000

# Set the environment variables
ENV REPOSITORY="mysql"

# Set the command to run the App
CMD ["python", "-m", "run"]
