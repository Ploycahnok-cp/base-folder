# Use an official Python runtime as a parent image
FROM python:3.12-slim

WORKDIR /code

# Copy the application code
COPY ./app /code/app

# Copy the data folder
COPY ./data /code/data

# Copy templates
COPY ./templates /code/templates

# Copy the dependencies file to the working directory
COPY pyproject.toml /code/
COPY pdm.lock /code/

# Install dependencies manager
RUN pip install pdm

# Install dependencies
RUN pdm sync --prod --no-editable

# Run the application

CMD ["pdm", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--workers", "9", "--timeout-keep-alive", "120"]
