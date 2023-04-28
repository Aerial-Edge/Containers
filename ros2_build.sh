#!/bin/bash
sudo apt update
sudo apt install -y python3-pip python3-rosdep python3-colcon-common-extensions

mkdir -p ~/ros2_humble_ws/src
cd ~/ros2_humble_ws/src
git clone -b humble https://github.com/ros2/ros2.git

cd ~/ros2_humble_ws
rosdep init
rosdep update

rosdep install -y --from-paths src --ignore-src --rosdistro humble

colcon build --symlink-install --packages-up-to ros2humble

colcon bundle --base-path install --apt-sources-skip-keys="ros2,humble" --output-dir ./ros2_humble_pkgs

