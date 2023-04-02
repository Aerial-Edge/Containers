#!/bin/bash

ip_address=192.168.86.242
port=5760

docker compose run --rm mavproxy --master=tcp:$ip_address:$port
