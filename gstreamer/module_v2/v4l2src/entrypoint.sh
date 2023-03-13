#!/bin/bash

host=192.168.86.30
port=19969

width=1280
height=720
rotation=0
framerate=30
overlay=0

v4l2-ctl --set-fmt-video=width=$width,height=$height,pixelformat=4
v4l2-ctl --set-ctrl=rotate=$rotation
v4l2-ctl --overlay=$overlay
v4l2-ctl -p $framerate
v4l2-ctl --set-ctrl=video_bitrate=4000000 #4Mbps

gst-launch-1.0 v4l2src do-timestamp=true ! video/x-h264, width=$width, height=$height, framerate=$framerate/1 ! h264parse ! rtph264pay config-interval=1 pt=96 mtu=1332 ! udpsink sync=false host=$host port=$port
