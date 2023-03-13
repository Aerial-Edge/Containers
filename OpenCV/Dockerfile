FROM python:3.9-slim-bullseye

#RUN apt-get update && apt-get -y install curl gnupg

#RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list
#RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

#RUN apt-get update
#RUN pip install --extra-index-url https://www.piwheels.org/simple numpy Pillow

RUN apt-get update && apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev \
			libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
			libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev \
			libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev \
			libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 \
			libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev

RUN pip3 install "picamera[array]"
RUN python3 -m pip install opencv-python

#RUN apt-get -y install python3-opencv
#RUN apt-get -y install libhdf5-dev
#RUN apt-get -y install libhdf5-serial-dev
#RUN apt-get -y install libatlas-base-dev
#RUN apt-get -y install libjasper-dev 
#RUN apt-get -y install libqtgui4 
#RUN apt-get -y install libqt4-test

#RUN pip3 install tflite-runtime


#WORKDIR /TFLite
#COPY label_image_example ./

ENTRYPOINT /bin/bash

#ENTRYPOINT	python3		label_image.py \
#		--model_file	./mobilenet_v1_1.0_224/mobilenet_v1_1.0_224.tflite \
#		--label_file	./labels/labels.txt \
#		--image		./testdata/grace_hopper.bmp
