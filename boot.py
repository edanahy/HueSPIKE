# this code runs on the LMS-ESP32 board
# make sure you set up the hardware properly (right firmware, install uartremote module, etc)
# - instructions: https://antonsmindstorms.com/2022/11/18/lms-esp32-tutorials-part-0-how-to-get-started/
from uartremote import *
import random
import network
sta_if = None
import socket

# in my lab/office is a Netgear Router connected to a Hue hub and Hue LED lightbulb
router_name = "DrEsRouter" # name of the router in my office
router_password = "sillyraven278" # password to router in my office
hue_IP = "192.168.1.137" # IP of the hue bridge
hue_port = 80
# HUE user with permission to control the lights
hue_user = "g4DDUvb7kYGzkovxu6BH6SdVGPur2tNBEi9Ymeqb"
hue_light_id = 4 # ID of the lightbulb to control

ur=UartRemote() # set up UART communication

def connect_to_network():
    global sta_if
    print('Setting up network:')
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    #print('## Networks: ##')
    #sta_if.scan() # print networks found (debugging)
    print('## Connecting to DrEsRouter ##')
    sta_if.connect(router_name, router_password)
    connect_to_network_test()

def connect_to_network_test():
    print('## Connected? ##')
    return_val = sta_if.isconnected()
    print(return_val)
    return return_val
    
def check_network_and_connect():
    global sta_if
    if sta_if == None:
        connect_to_network()
    elif connect_to_network_test() == False:
        connect_to_network()

# send JSON val
def send_command(path, val):
    # HUE API? see: https://developers.meethue.com/develop/get-started-2/
    s = socket.socket()
    s.connect((hue_IP, hue_port))
    host_ip = '192.168.1.13' # not sure what this is, but doesn't work w/out it
    s.send(bytes('PUT ' + path + ' HTTP/1.1\r\nHOST: ' + host_ip + '\r\nContent-Type: application/json\r\nContent-Length: ' + str(len(val)) + '\r\n\r\n' + val + '\r\n\r\n', 'utf-8'))
    response = s.recv(4096)
    print('## SENT SOCKET REQUEST ##')
    print('response:', response) # debugging: look at this to see if error
    s.close()

def send_hue_command(JSON):
    # HUE API? see: https://developers.meethue.com/develop/get-started-2/
    # - send JSON command to change the state of the light
    send_command('/api/' + hue_user + '/lights/' + str(hue_light_id) + '/state', JSON)

def light_on():
    check_network_and_connect()
    send_hue_command('{\"on\":true}') # state: on
    
def light_off():
    check_network_and_connect()
    send_hue_command('{\"on\":false}') # state: off

def light_random():
    check_network_and_connect()
    rand_hue = random.randint(0,65535) # state: random color (hue)
    send_hue_command('{\"sat\": 254, \"bri\": 254, \"hue\": ' + str(rand_hue) + '}')

# register the three main commands (to be triggered by SPIKE Prime)
ur.add_command(light_on,'repr')
ur.add_command(light_off,'repr')
ur.add_command(light_random,'repr')

ur.loop() # loop continuously waiting for command
