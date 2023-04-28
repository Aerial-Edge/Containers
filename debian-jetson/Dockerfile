FROM arm64v8/debian:bullseye

# Install basic dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        gnupg2 \
        wget && \
    rm -rf /var/lib/apt/lists/*

# Install CUDA dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        dkms \
        freeglut3-dev \
        libglu1-mesa-dev \
        libxi-dev \
        libxmu-dev \
        ocl-icd-libopencl1 \
        ocl-icd-opencl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install CUDA Toolkit
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/debian11/sbsa/cuda-11-4_11.4.2-1_arm64.deb && \
    dpkg -i cuda-11-4_11.4.2-1_arm64.deb && \
    rm cuda-11-4_11.4.2-1_arm64.deb

# Add CUDA binaries to the path
ENV PATH="/usr/local/cuda-11.4/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda-11.4/lib64:${LD_LIBRARY_PATH}"
