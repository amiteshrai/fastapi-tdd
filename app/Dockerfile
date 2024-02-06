# Pull official base image
FROM python:3.12.1-slim-bookworm

# Install poetry
RUN pip install --upgrade pip
RUN pip install poetry==1.7.0

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Set working directory
WORKDIR /app

# Copy dependecies files
COPY pyproject.toml poetry.lock ./

# Install python dependencies
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# Add app
COPY . .

RUN poetry install --without dev

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
