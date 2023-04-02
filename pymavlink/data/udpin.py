import time
import sys
from pymavlink import mavutil

the_connection = mavutil.mavlink_connection("udpin:localhost:14550", baud=57600)
the_connection.wait_heartbeat()
print("HEARTBEAT_DONE")

def request_message_interval(the_connection, message_input: str, frequency_hz: float):

    message_name = "MAVLINK_MSG_ID_" + message_input

    message_id = getattr(mavutil.mavlink, message_name)

    the_connection.mav.command_long_send(

        the_connection.target_system, the_connection.target_component,

        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,

        message_id,

        1e6 / frequency_hz,

        0,

        0, 0, 0, 0)


    print("Requested the message successfully.")



request_message_interval(the_connection, "ATTITUDE", 5)

while True:
	print(the_connection.recv_match(type='ATTITUDE', blocking=True))
