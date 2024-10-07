FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
  gcc \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Config Poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

# Copy only the dependencies definition files
COPY pyproject.toml /app/

# Install all dependencies, including dev dependencies
RUN poetry install

# Copy the rest of the code
COPY . /app

# Run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
