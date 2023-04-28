FROM arm64v8/debian:bullseye

# Install ROS 2 Humble
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg2 \
        lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    sh -c 'echo "deb [arch=arm64,signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu bullseye main" > /etc/apt/sources.list.d/ros2-latest.list' && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ros-humble-ros-base && \
    rm -rf /var/lib/apt/lists/*

# Install MAVROS dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libboost-system-dev \
        libboost-thread-dev \
        libconsole-bridge-dev \
        libeigen3-dev \
        libgeographic-dev \
        libgeographic-msgs-dev \
        libopencv-dev \
        libsuitesparse-dev \
        libtinyxml2-dev \
        libxmlrpc++-dev \
        ros-humble-diagnostic-updater \
        ros-humble-geodesy \
        ros-humble-mavlink \
        ros-humble-tf2-eigen && \
    rm -rf /var/lib/apt/lists/*

# Install MAVROS
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git && \
    cd /tmp && \
    git clone https://github.com/mavlink/mavros.git && \
    cd mavros && \
    git checkout tags/v2.4.3 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    make install && \
    rm -rf /var/lib/apt/lists/*

# Set up the ROS environment
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Set the entrypoint to bash
ENTRYPOINT [ "/bin/bash" ]

