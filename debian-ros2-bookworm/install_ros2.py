#!/usr/bin/env python3
import subprocess

def run_command(command, shell=False):
    result = subprocess.run(command, shell=shell, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def main():
    # Updating and upgrading the system
    run_command(["apt-get", "update"])
    run_command(["apt-get", "-y", "upgrade"])

    # Installing system packages
    packages = [
        "curl",
        "gnupg2",
        "lsb-release",
        "build-essential",
        "cmake",
        "git",
        "wget"
    ]
    run_command(["apt-get", "install", "-y"] + packages)

    # Adding ROS2 apt repository
    run_command("curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -", shell=True)
    run_command('sh -c \'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list\'', shell=True)

    run_command(["apt", "update"])

    # Installing ROS2 dependencies
    ros2_deps = [
        "python3-colcon-common-extensions",
        "python3-flake8",
        "python3-pip",
        "python3-pytest-cov",
        "python3-rosdep",
        "python3-setuptools",
        "python3-vcstool",

    ]
    run_command(["apt", "install", "-y"] + ros2_deps)

    # Cleaning up the apt cache
    run_command(["rm", "-rf", "/var/lib/apt/lists/*"], shell=True)

    # Installing Python packages
    python_packages = [
        "argcomplete",
        "flake8-blind-except",
        "flake8-builtins",
        "flake8-class-newline",
        "flake8-comprehensions",
        "flake8-deprecated",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-quotes",
        "pytest-repeat",
        "pytest-rerunfailures",
        "pytest",
        "setuptools"
    ]
    run_command(["python3", "-m", "pip", "install", "-U", "--break-system-packages"] + python_packages)

    # Setting up ROS2 workspace
    run_command(["mkdir -p /opt/ros2/src"], shell=True)
    run_command(["cd /opt/ros2/"], shell=True)
    run_command(["wget https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos"], shell=True)
    run_command(["vcs import src < ros2.repos"], shell=True)

    # Initializing rosdep
    run_command(["rosdep init"], shell=True)
    run_command(["rosdep update"], shell=True)

    # Installing ROS2 dependencies via rosdep
    run_command(["apt-get", "update"])
    run_command(["apt-get", "-y", "upgrade"])
    run_command(["rosdep install --from-paths src --ignore-src --rosdistro humble --os=debian:bullseye -y --skip-keys console_bridge fastcdr fastrtps libopensplice67 rti-connext-dds-5.3.1 urdfdom_headers ignition-math6 ignition-cmake2 rti-connext-dds-6.0.1"])

    # Building ROS2
    run_command(["colcon", "build", "--symlink-install"], shell=True)

    # Adding setup.bash to bashrc
    #with open("/home/ros/.bashrc", "a") as bashrc:
    #    bashrc.write("source /opt/ros2/install/setup.bash\n")

    print("ROS2 installation and setup is complete.")

if __name__ == "__main__":
    main()
