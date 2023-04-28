FROM ubuntu:22.04

# Install ROS 2 Humble
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg2 \
        lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    sh -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list' && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ros-humble-ros-base && \
    rm -rf /var/lib/apt/lists/*

# Set up the ROS environment
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Set the entrypoint to bash
ENTRYPOINT [ "/bin/bash" ]
