# Use an official Python image as a base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    YARL_NO_EXTENSIONS=1 \
    PATH="/root/.cargo/bin:$PATH"

# Install system dependencies
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
        curl \
        cargo \
        rustc && \
    rm -rf /var/lib/apt/lists/*

# Install Rust (alternative way)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --no-binary :all: .

# Set entry point
ENTRYPOINT ["python", "-m", "maigret"]
