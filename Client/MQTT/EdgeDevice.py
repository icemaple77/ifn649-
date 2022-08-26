#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random 
import _thread as thread
import time
import sys
import struct
import re
#from bt.txt
import serial
import string
from paho.mqtt import client as mqtt_client 

broker = '3.25.137.123'
port = 1883
topic = "Michael"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
ser = serial.Serial("/dev/rfcomm0", 9600)
#ser.write(str.encode('Start\r\n'))
def connect_mqtt() -> mqtt_client:
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
    #ser.write(bytes("0000",'utf-8'))
    while True:
        time.sleep(0.0001)
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        print(cookedserial)
       
        msg = topic+":"+cookedserial
        result = client.publish(topic,msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{cookedserial}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #Z = re.split('[,]', msg.payload.decode())
        #print(Z[1])
        
    client.subscribe(topic)
    client.on_message = on_message
    ser.write(bytes(msg.payload.decode(),'utf-8'))
def thread1(threadName,delay):
    client = connect_mqtt()
    while True:
        print (threadName+" start")
        #publish(client)
def thread2(threadName,delay):
    client = connect_mqtt()
    while True:
        print (threadName+" start")
        #subscribe(client)
        #client.loop_forever()
# 创建两个线程
try:
   thread.start_new_thread(thread1,("publish",1))
   thread.start_new_thread(thread2,("subscribe",2))
except:
   print ("Error: unable to start thread")
 
while 1:
   pass