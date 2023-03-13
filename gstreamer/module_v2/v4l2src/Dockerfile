FROM debian:stable-slim

RUN apt-get update && apt-get -y install gstreamer1.0-tools gstreamer1.0-plugins-good \
					gstreamer1.0-plugins-bad v4l-utils

CMD ["sh", "/home/root/entrypoint.sh"]
