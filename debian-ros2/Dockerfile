FROM arm64v8/debian:bullseye

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        python3-colcon-common-extensions \
        python3-lark-parser \
        python3-pip \
        python3-pytest-cov \
        python3-setuptools \
        wget && \
    rm -rf /var/lib/apt/lists/*

# Clone ROS 2 source code
ARG ROS2_WS=/root/ros2_ws
RUN mkdir -p ${ROS2_WS}/src && \
    cd ${ROS2_WS}/src && \
    git clone https://github.com/ros2/ros2.git && \
    cd ros2 && \
    git checkout humble && \
    cd .. && \
    wget https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos && \
    vcs import < ros2.repos && \
    rm -rf ros2.repos

# Build ROS 2
RUN cd ${ROS2_WS} && \
    colcon build --symlink-install --packages-up-to rclcpp

# Set up the ROS environment
RUN echo "source ${ROS2_WS}/install/setup.bash" >> /root/.bashrc

# Set the entrypoint to bash
ENTRYPOINT [ "/bin/bash" ]
