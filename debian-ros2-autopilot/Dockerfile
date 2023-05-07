FROM docker.aerial-edge.no/debian_ros2_humble:1.0.0

# Installing pyMAVLink:
RUN pip install --extra-index-url=https://www.piwheels.org/simple numpy pymavlink

# Initializing package:
WORKDIR	/home/ros/ros2_ws/src/
RUN . /home/ros/ros2_ws/install/setup.sh && \
    ros2 pkg create --build-type ament_python --node-name autopilot_node drone_pkg

# Building package:
WORKDIR /home/ros/ros2_ws/
RUN . /home/ros/ros2_ws/install/setup.sh && \
    colcon build --packages-select drone_pkg --symlink-install

# Copying node script:
COPY ./drone_pkg/autopilot_node.py ./src/drone_pkg/drone_pkg/autopilot_node.py

# Copying entrypoint:
COPY ./entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]