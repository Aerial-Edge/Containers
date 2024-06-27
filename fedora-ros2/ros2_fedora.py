import subprocess

def run_command(command, shell=False):
    result = subprocess.run(command, shell=shell, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def main():
    # Updating and upgrading the system
    run_command(["dnf", "update", "-y"])

    # Installing necessary packages
    packages = [
        "curl",
        "gnupg2",
        "lsb-release",
        "make",
        "gcc",
        "gcc-c++",
        "cmake",
        "git",
        "python3-colcon-common-extensions",
        "python3-flake8",
        "python3-pip",
        "python3-pytest-cov",
        "python3-rosdep",
        "python3-setuptools",
        "python3-vcstool",
        "wget"
    ]
    run_command(["dnf", "install", "-y"] + packages)

    # Adding ROS2 dnf repository
    run_command("curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | gpg --dearmor -o /etc/pki/rpm-gpg/ROS-GPG-KEY", shell=True)
    run_command('sh -c \'echo "[ros2]\nname=ROS 2\nbaseurl=http://packages.ros.org/ros2/fedora/$releasever/$basearch\nenabled=1\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/ROS-GPG-KEY" > /etc/yum.repos.d/ros2.repo\'', shell=True)

    run_command(["dnf", "update", "-y"])

    # Installing ROS2 dependencies
    run_command(["dnf", "install", "-y"] + packages)

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
    run_command(["python3", "-m", "pip", "install", "-U"] + python_packages)

    # Setting up ROS2 workspace
    run_command(["mkdir", "-p", "/opt/ros2/src"], shell=True)
    run_command(["wget", "https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos"], shell=True)
    run_command(["vcs", "import", "src < ros2.repos"], shell=True)

    # Initializing rosdep
    run_command(["rosdep", "init"], shell=True)
    run_command(["rosdep", "update"], shell=True)

    # Installing ROS2 dependencies via rosdep
    run_command(["dnf", "update", "-y"])
    run_command(["rosdep", "install", "--from-paths", "src", "--ignore-src", "--rosdistro", "humble", "--os=fedora", "-y", "--skip-keys",
                 "console_bridge fastcdr fastrtps libopensplice67 rti-connext-dds-5.3.1 urdfdom_headers ignition-math6 ignition-cmake2 rti-connext-dds-6.0.1"])

    # Building ROS2
    run_command(["colcon", "build", "--symlink-install"], shell=True)

    # Adding setup.bash to bashrc
    with open("/home/ros/.bashrc", "a") as bashrc:
        bashrc.write("source /opt/ros2/install/setup.bash\n")

    print("ROS2 installation and setup is complete.")

if __name__ == "__main__":
    main()
