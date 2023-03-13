#!/bin/bash

host=192.168.86.30
port=19969

width=1280
height=720
rotation=0
framerate=30
overlay=0

udevadm control --reload

#v4l2-ctl --set-fmt-video=width=$width,height=$height,pixelformat=4
#v4l2-ctl --set-ctrl=rotate=$rotation
#v4l2-ctl --overlay=$overlay
#v4l2-ctl -p $framerate
#v4l2-ctl --set-ctrl=video_bitrate=4000000

#gst-launch-1.0 v4l2src ! video/x-h264, width=$width, height=$height, framerate=$framerate/1 ! h264parse ! rtph264pay config-interval=1 pt=96 mtu=1332 ! \
#udpsink sync=false host=$host port=$port



#gst-launch-1.0 libcamerasrc ! capsfilter caps=video/x-raw,width=$width,height=$height,format=NV12 ! v4l2convert ! v4l2h264enc extra-controls="controls,repeat_sequence_header=1" \
#! h264parse ! rtph264pay ! udpsink host=$host port=$port

libcamera-vid -t 0 -n --inline -o - | gst-launch-1.0 fdsrc fd=0 ! h264parse ! rtph264pay ! udpsink host=192.168.86.30 port=19969
