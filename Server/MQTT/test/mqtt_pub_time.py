# encoding:UTF-8
#send data to the gpio topic periodly
import paho.mqtt.client as mqtt
import time
import random
import datetime
import socket
import json
Assignment ='{"name" : "john", "gender" : "male", "age": 28}'
s = {
        "left_A_ori" :1,
        "right_A_ori":2,
        "left_B_ori" :3,
        "right_B_ori":4,
        "left_spd"   :5,
        "right_spd"  :6,
        "left_ang"   :7,
        "right_ang"  :8,
        }
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    recdata=str(msg.payload)
    #count=count+1
    print (recdata)
    #print(msg.topic+" "+str(msg.payload))

def sendingData():    
    #sendtime=str(datetime.datetime.now())
    #s='{"time":"'+sendtime+'"}'
    print(type(Assignment))
    client.publish("time",str(s))
    time.sleep(1)
    
client = mqtt.Client()
client.username_pw_set("admin","password") #set the username and password of apache-apollo server 
client.on_connect = on_connect
client.on_message = on_message

client.connect(get_host_ip(), 1883, 60)
print(get_host_ip())
#client.subscribe("time")

client.loop_start()
count=0
while True:
    #sendingData()
    client.publish("time",count)
    time.sleep(1)
    count=count+1
    print (count)
    if count>20000:
        break