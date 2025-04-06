# Use the official Python 3.10 image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file and install them
COPY pyproject.toml poetry.lock /app/
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

# Copy the rest of your application code into the container
COPY . /app/

# Expose the port your app will run on (adjust if necessary)
EXPOSE 8000

# Run your application
CMD ["python", "main.py"]
