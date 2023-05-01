FROM debian:bullseye

# Setting up user for ros2
RUN useradd -ms /bin/bash ros
RUN usermod -aG sudo ros
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ros
WORKDIR /home/ros

# Upgrading packages in order to make sure that the ros2 build does not fail
RUN sudo apt-get update && sudo apt-get -y upgrade

RUN sudo apt-get update && sudo apt-get y install \
	curl \
	gnupg2 \
	lsb-release \
	&& curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - \
	&& sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu `lsb-release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list' \
	&& sudo apt-get update && sudo apt-get -y install \
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

RUN sudo python3 -m pip install -U \
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
	setuptools

RUN mkdir -p ~/ros2_ws/src
WORKDIR /home/ros2_ws
RUN wget https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos
RUN vcs import src < ros2.repos
RUN sudo rosdep init

# The follwing line instructs the build system which rosdistro to install and which dependencies to ignore
# Because we are using the bundled DDS we do not need anything else. 
# Removing or adding things to this line may require you to modify build files for ros2 and install additional
# system dependencies.

RUN rosdep update && rosdep install --from-paths src --ignore-src --rosdistro humble -y --skip-keys "console_bridge fastcdr fastrtps libopensplice67 rti-connext-dds-5.3.1 urdfdom_headers ignition-math6 ignition-cmake2 rti-connext-dds-6.0.1"

RUN colcon build --symlink-install

RUN echo "source /home/ros/ros2_ws/install/setup.bash" >> /home/ros/.bashrc
