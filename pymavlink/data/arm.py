import time
import sys
from pymavlink import mavutil
import socket

#def get_ip_address():
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    s.connect(("192.168.86.1", 80))
#    return s.getsockname()[0]

#serial_udp = "udpin:"+get_ip_address()+":14550"

the_connection = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
the_connection.wait_heartbeat()
print("Heartbeat from system / component: " + str(the_connection.target_system) + " / " + str(the_connection.target_component))

the_connection.mav.command_long_send(	the_connection.target_system,
					the_connection.target_component,
					mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
					0, 1, 0, 0, 0, 0, 0, 0)
print(the_connection.recv_match(type='COMMAND_ACK', blocking=True))
