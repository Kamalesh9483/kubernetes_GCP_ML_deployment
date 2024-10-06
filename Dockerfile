# Use Python 3.7 as the base image
FROM python:3.7

# Set environment variables for virtual environment
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create the virtual environment
RUN python -m venv $VIRTUAL_ENV

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
ENV PORT 8080
EXPOSE $PORT

# Command to run the application with Gunicorn
CMD ["gunicorn", "app:app", "--config=config.py"]
