# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . /code/

# Set the environment variable for Django
ENV DJANGO_SETTINGS_MODULE=your_project_name.settings

# Expose the port on which Django runs
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
