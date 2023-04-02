FROM python:3.9-slim-bullseye

RUN apt-get update && apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev \
                        libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
                        libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev \
                        libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev \
                        libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 \
                        libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev

RUN pip3 install "picamera[array]"
RUN python3 -m pip install opencv-python
RUN pip3 install imutils

CMD ["python", "/root/app/main.py"]
