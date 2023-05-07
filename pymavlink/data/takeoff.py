import time
import sys
from pymavlink import mavutil
import socket
import time

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("192.168.86.1", 80))
    return s.getsockname()[0]

serial0_udp = "udpin:"+get_ip_address()+":14550"
serial0_tcp = "tcp:192.168.86.24:5760"

the_connection = mavutil.mavlink_connection(serial0_udp)
the_connection.wait_heartbeat()
print("Heartbeat from system / component: " + str(the_connection.target_system) + " / " + str(the_connection.target_component))

# SET MODE (param1: FLTMODE1, param2: value):
the_connection.mav.command_long_send(	the_connection.target_system,
					the_connection.target_component,
					mavutil.mavlink.MAV_CMD_DO_SET_MODE,
					0,
					1, 4, 0, 0, 0, 0, 0)
print(the_connection.recv_match(type='COMMAND_ACK', blocking=True))

# ARMING:
the_connection.mav.command_long_send(	the_connection.target_system,
					the_connection.target_component,
					mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
					0,
					1, 0, 0, 0, 0, 0, 0)
print(the_connection.recv_match(type='COMMAND_ACK', blocking=True))

# TAKING OFF:
the_connection.mav.command_long_send(   the_connection.target_system,
                                        the_connection.target_component,
                                        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
                                        0,
                                        0, 0, 0, 0, 0, 0, 5)
print(the_connection.recv_match(type='COMMAND_ACK', blocking=True))
