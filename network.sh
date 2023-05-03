#!/bin/bash

# This script sets up two different subnets on two different network cards.
# It's useful for our setup with two raspberry pis that are communicating over
# ethernet

# Check if the script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" >&2
    exit 1
fi

# Configure eth0
ip addr add 192.168.1.2/24 dev eth0
ip link set eth0 up

# Configure eth1
ip addr add 10.0.0.2/24 dev eth1
ip link set eth1 up

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Configure NAT using iptables
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

# Save iptables rules
iptables-save > /etc/iptables/rules.v4

# Enable the new rules on boot
systemctl enable netfilter-persistent

echo "Network configuration applied successfully!"

