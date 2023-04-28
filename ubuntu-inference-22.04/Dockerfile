FROM ubuntu:22.04

# Install Jetson Inference dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libatlas-base-dev \
        libprotobuf-dev \
        protobuf-compiler \
        python3-dev \
        python3-pip \
        python3-numpy \
        python3-pil \
        python3-setuptools \
        python3-scipy && \
    rm -rf /var/lib/apt/lists/*

# Install TensorFlow Lite
RUN pip3 install --no-cache-dir \
        tensorflow==2.5.0 \
        pillow \
        numpy

# Install OpenCV
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libopencv-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the entrypoint to bash
ENTRYPOINT [ "/bin/bash" ]
