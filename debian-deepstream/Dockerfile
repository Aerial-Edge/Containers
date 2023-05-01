# Use the official Debian Bullseye (arm64) as a base image
FROM debian:bullseye-slim

# Set the working directory
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    lsb-release \
    ca-certificates \
    build-essential \
    libglib2.0-dev \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libffi-dev \
    curl \
    git

# Install DeepStream SDK and its dependencies
RUN echo "deb https://repo.download.nvidia.com/jetson/common r32.6 main" > /etc/apt/sources.list.d/nvidia-l4t-apt-source.list && \
    curl -s https://repo.download.nvidia.com/jetson/jetson-ota-public.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/jetson-ota-public.gpg && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    nvidia-l4t-core \
    nvidia-deepstream

# Clone the YOLO plugin for DeepStream
RUN git clone https://github.com/marcoreps/deepstream_nvdsinfer_yolo.git /app/deepstream_nvdsinfer_yolo && \
    cd /app/deepstream_nvdsinfer_yolo && \
    make && \
    make install

# Copy your DeepStream application and configuration files
COPY ./app /app

# Expose ports if needed for your application
# EXPOSE <port_number>

# Set the entrypoint for your DeepStream application
ENTRYPOINT ["./app/your_deepstream_app"]

