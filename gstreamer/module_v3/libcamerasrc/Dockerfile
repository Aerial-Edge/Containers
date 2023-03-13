FROM debian:stable-slim

RUN apt-get update && apt-get -y install gstreamer1.0-tools gstreamer1.0-plugins-good \
					gstreamer1.0-plugins-bad v4l-utils

RUN apt-get update && apt-get -y install gnupg wget
RUN echo deb http://archive.raspberrypi.org/debian/ bullseye main > /etc/apt/sources.list.d/raspi.list
RUN wget https://archive.raspberrypi.org/debian/raspberrypi.gpg.key -O - | apt-key add -

RUN apt-get update && apt-get -y install libcamera0 libcamera-apps-lite

RUN apt-get -y install udev


CMD ["sh", "/home/root/entrypoint.sh"]
