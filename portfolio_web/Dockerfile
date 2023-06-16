# Use the official Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project code
COPY . .

# Run the Django development server
CMD python manage.py runserver 0.0.0.0:8008