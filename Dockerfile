# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install rasa rasa-sdk

# Make port 5005 available to the world outside this container
EXPOSE 5005

# Define environment variable
ENV NAME World

# Run rasa when the container launches
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
