# Use the official Python image as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file into the container at /code/
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt

# Copy the entire project into the container at /code/
COPY ./ /code/

# Set the working directory to /code/app
WORKDIR /code/app

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
