#!/usr/bin/python3

import random
import time
import sys
import struct
import re
#from bt.txt
import serial
import string
from paho.mqtt import client as mqtt_client

# ser = serial.Serial("/dev/rfcomm0", 9600)
# ser.write(str.encode('Start\r\n'))
# ser.write(bytes("0000", 'utf-8'))


broker = '3.25.137.123'
port = 1883
topic = "Teensy"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        # print(msg.payload.decode())
    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    #while True:
    subscribe(client)
    client.loop_forever()
        
        # if(entry =="2"):
        #     client.loop_start()
        #     publish(client)
            



if __name__ == '__main__':
    run()

