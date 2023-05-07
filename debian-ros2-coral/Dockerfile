FROM python:3.9-bullseye

# Installing ROS Humble
RUN apt-get update && apt-get -y install wget
RUN wget https://github.com/Ar-Ray-code/rpi-bullseye-ros2/releases/download/ros2-0.3.1/ros-humble-desktop-0.3.1_20221218_arm64.deb
RUN apt-get -y install ./ros-humble-desktop-0.3.1_20221218_arm64.deb
RUN . /opt/ros/humble/setup.bash

# Installing TFLite:
RUN apt-get -y install gnupg
RUN wget https://packages.cloud.google.com/apt/doc/apt-key.gpg
RUN gpg --no-default-keyring --keyring temp-keyring.gpg --import apt-key.gpg
RUN mkdir /etc/apt/keyrings/ && gpg --no-default-keyring --keyring temp-keyring.gpg --export --output /etc/apt/keyrings/google-apt-key.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/google-apt-key.gpg] https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list

RUN apt-get update && apt-get -y install python3-tflite-runtime libedgetpu1-std python3-cv-bridge python3-opencv

# Installing colcon:
RUN pip install -U git+https://github.com/colcon/colcon-common-extensions.git

# Installing v4l2
RUN apt-get -y install v4l-utils
WORKDIR /root/ros2_ws

# Installing Python dependencies:
RUN pip3 install --extra-index-url https://www.piwheels.org/simple numpy Pillow "picamera[array]" 


ENTRYPOINT /bin/bash