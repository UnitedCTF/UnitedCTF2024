# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the source code to the container
COPY app.py ./

# Expose the port on which the Flask app will run
EXPOSE 5001

# Set the command to run the Flask app with gunicorn
CMD [ "python", "-m", "gunicorn", "-b", "0.0.0.0:5001", "app:app"]
