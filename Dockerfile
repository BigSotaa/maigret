FROM python:3.10-slim  # Use Python 3.10 or even python:3.11-slim if needed

LABEL maintainer="Soxoj <soxoj@protonmail.com>"

WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
      gcc \
      python3-dev \
      libffi-dev \
      build-essential \
      musl-dev \
      libxml2 \
      libxml2-dev \
      libxslt-dev \
    && rm -rf /var/lib/apt/lists/* /tmp/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy source files
COPY . .

# Install dependencies, forcing a pure Python install for `yarl`
RUN YARL_NO_EXTENSIONS=1 pip install --no-cache-dir --no-binary :all: .

# Set entrypoint
ENTRYPOINT ["maigret"]
