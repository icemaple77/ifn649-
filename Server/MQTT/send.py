import random
import time
import sys
import struct
import re
#from bt.txt
import serial
import time
import string

from paho.mqtt import client as mqtt_client
ser = serial.Serial("/dev/rfcomm1", 9600)
ser.write(str.encode('Start\r\n'))

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


def publish(client):
   
    while True:
        time.sleep(0.0001)
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        print(cookedserial)
       
        #msg = ST
        result = client.publish(topic,cookedserial)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{cookedserial}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
      


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
