FROM debian:bookworm as build

# Setting up user for storing the ros2 git tree
#RUN useradd -ms /bin/bash ros
#RUN usermod -Ag sudo ros
#RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
#USER ros
WORKDIR /opt/ros2

# If you do not upgrade packages, the ros2 compilation will fail due to qtbase5-dev not being
# installable

RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release \
    && curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - \
    && sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list' \
    && apt update && apt install -y \
    build-essential \
    cmake \
    git \
    python3-colcon-common-extensions \
    python3-flake8 \
    python3-pip \
    python3-pytest-cov \
    python3-rosdep \
    python3-setuptools \
    python3-vcstool \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install -U --break-system-packages \
    argcomplete \
    flake8-blind-except \
    flake8-builtins \
    flake8-class-newline \
    flake8-comprehensions \
    flake8-deprecated \
    flake8-docstrings \
    flake8-import-order \
    flake8-quotes \
    pytest-repeat \
    pytest-rerunfailures \
    pytest \
    setuptools

RUN mkdir -p /opt/ros2/src && wget https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos && vcs import src < ros2.repos && rosdep init

# The following line details which dependencies to skip. Since we are using the default and bundled DDS 
# there is no need to install others. 
# This line can be modified if your system do contain these dependencies, however, some of them might be hard to install on stock debian 11

RUN rosdep update
RUN apt-get update && apt-get -y upgrade && rosdep install --from-paths src --ignore-src --rosdistro humble --os=debian:bullseye -y --skip-keys "console_bridge fastcdr fastrtps libopensplice67 rti-connext-dds-5.3.1 urdfdom_headers ignition-math6 ignition-cmake2 rti-connext-dds-6.0.1"

RUN colcon build --symlink-install

#RUN echo "source /opt/ros2/install/setup.bash" >> /home/ros/.bashrc

FROM debian:bookworm as main
COPY --from=build /opt/ /
