#!/bin/bash

ip_address=192.168.86.44
port=14550

docker compose run --rm mavproxy --master=udp:$ip_address:$port
