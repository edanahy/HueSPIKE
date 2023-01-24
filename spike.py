# SPIKE 2 Firmware
# - edit/download via: https://spikelegacy.legoeducation.com/
# make sure you first install the uartremote module (for the LMS-ESP32 board)
# - tutorial: https://antonsmindstorms.com/2022/11/15/lms-esp32-tutorial-part-1-uartremote/
# - github: https://github.com/antonvh/UartRemote/tree/master/MicroPython/SPIKE
# - documentation: https://uartremote.readthedocs.io/en/latest/
from projects.uartremote import *
ur=UartRemote('A') # port with the LMS-ESP32 board

from spike import PrimeHub, LightMatrix, Button, ForceSensor, Motor
from spike.control import wait_for_seconds

hub = PrimeHub()
f_on = ForceSensor('B')
f_off = ForceSensor('D')
motor = Motor('F')

f_state = 'OFF'
hub.light_matrix.show_image('NO')
motor_pos_init = motor.get_position()

# if buttons are pushed, sends the "on/off" command to the LMS-ESP32 board
# if light is on and motor is turned, sends the "random" command to the LMS-ESP32 board
while True:
    if f_state == 'OFF':
        f_on_val = f_on.get_force_newton()
        if (f_on_val > 5):
            print('calling: light_on')
            ack,result = ur.call('light_on')
            f_state = 'ON'
            hub.light_matrix.show_image('YES')
    elif f_state == 'ON':
        f_off_val = f_off.get_force_newton()
        if (f_off_val > 5):
            print('calling: light_off')
            ack,result = ur.call('light_off')
            f_state = 'OFF'
            hub.light_matrix.show_image('NO')
        motor_pos_tmp = motor.get_position()
        if (abs(motor_pos_init - motor_pos_tmp) > 40):
            print('calling: light_random')
            hub.light_matrix.show_image('DUCK')
            ack,result = ur.call('light_random')
            wait_for_seconds(0.5)
            hub.light_matrix.show_image('YES')
            motor_pos_init = motor.get_position()
    wait_for_seconds(0.2)
