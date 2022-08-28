#!/usr/bin/python3.9
import serial
import time
import string
import random
import json
from paho.mqtt import client as mqtt_client
import paho.mqtt.publish as publish
# reading and writing data from and to arduino serially.
# rfcomm0 -> this could be different
room1201 = serial.Serial("/dev/rfcomm0", 9600)
room1202 = serial.Serial("/dev/rfcomm1", 9600)
Server="linux.chenyun.org"
topic="QUTGP/sblock/level12/"
tempTopic="/temperature"
humTopic="/humidity"
port = 1883
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
 
#ser.write(bytes("1", 'utf-8'))
#ser.write(bytes("0000", 'utf-8'))
# ser1201.write(str.encode('Start\r\n'))
# ser1202.write(str.encode('Start\r\n'))
def getSerialData(serNo):
        Data = serNo.readline()
        cooked = Data.decode('utf-8').strip('\r\n')
        #print(cooked)
        h=retrieveHumidity(cooked)
        t=retrieveTemperature(cooked)
        return (h,t)
def retrieveHumidity(data):
    rawData=data.split(" ")
    roomNumber=rawData[1]
    title=rawData[3]
    degree=rawData[5]
    hum = '{"roomNO": "%s", "title": "%s", "degree": "%s"}' %(roomNumber,title,degree)
    return hum
def retrieveTemperature(data):
    rawData=data.split(" ")
    roomNumber=rawData[1]
    title=rawData[8]
    degree=rawData[10]
    temp = '{"roomNO": "%s", "title": "%s", "degree": "%s"}' %(roomNumber,title,degree)
    return temp

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(Server, port)
    return client
def sendMsg(client,topic,data):
    result = client.publish(topic,data)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{data}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    
def publish(client):

   

    while True:
        time.sleep(0.0001)
        h1,t1=getSerialData(room1201)
        h2,t2=getSerialData(room1202)
        t1Topic=topic+"room1201"+tempTopic
        h1Topic=topic+"room1201"+humTopic
        t2Topic=topic+"room1202"+tempTopic
        h2Topic=topic+"room1202"+humTopic
        sendMsg(client,t1Topic,t1)
        sendMsg(client,h1Topic,h1)
        sendMsg(client,t2Topic,t2)
        sendMsg(client,h2Topic,h2)
        


def run():
    room1201.write(str.encode('Start\r\n'))
    room1202.write(str.encode('Start\r\n'))
    client = connect_mqtt()
    client.loop_start()

    publish(client)

if __name__ == '__main__':
    run()






# def publish_clt(client,room,t,h):
#     Server="linux.chenyun.org"
#     topic="QUTGP/sblock/level12/"
#     tempTopic="/temperature"
#     humTopic="/humidity"
#     # print t,h

#     # publish(client,topic+room+tempTopic,t)
#     # publish(client,topic+room+humTopic,h)
#     publish.single(topic+room+tempTopic, t, hostname=Server)
#     time.sleep(2)
#     publish.single(topic+room+humTopic, h, hostname=Server)
#     time.sleep(2)
# def Pub(topic,hostname,h1,h2,t1,t2):

#     msgs = [{"topic": "%s"% topic, "payload": "%s" % h1},{"topic": "%s"% topic, "payload": "%s" % h2},{"topic": "%s"% topic, "payload": "%s" % t1},{"topic": "%s"% topic, "payload": "%s" % t2}]
#     publish.multiple(msgs, hostname = hostname, port = 1883)
# t1=""
# t2=""
# h1=""
# h2=""
# while True:

#     # if(ser1201.in_waiting <= 0 and ser1202.in_waiting <= 0):
#     #     print("No Data")
#     if (ser1201.in_waiting > 0):        
#         RawData=getSerialData(ser1201)
#         h1=retrieveHumidity(RawData)
#         t1=retrieveTemperature(RawData)
#         print(h1,t1)
#         publish_clt("room1201",t1,h1)
#     if (ser1202.in_waiting > 0):
#         RawData=getSerialData(ser1202)
#         h2=retrieveHumidity(RawData)
#         t2=retrieveTemperature(RawData)
#         print(h2,t2)
#         publish_clt("room1202",t2,h2)
#     # Pub("123123","linux.chenyun.org",h1,h2,t1,t2)