import paho.mqtt.client as mqtt
import json
import serial
import time
import string

Server="linux.chenyun.org"
Port=1883
topic="#"
def on_connect(client, userdata, flags, rc): 
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)
    client.subscribe(topic) 

def on_message(client, userdata, msg):       
    # Func for Sending msg 
    #print(msg.topic+" "+str(msg.payload))
    data=str(msg.payload)
    shabi=data.split("'")
    print(shabi[1])
    controlAlarm (shabi[1])
# def alert_On():

# def alert_Off():
    
def controlAlarm(data):
    print(data)
    RawData = json.loads(data)
    RawData["title"]
    #print (mes_to_dict["title"])
    if(RawData["roomNO"]=="*ROOM1201*"):
        if (RawData["title"]=="Temperature"):
            if(float(RawData["degree"])>23):
                Call_Function(Alart)
            else:
                Call_Function(Close)
        if (RawData["title"]=="Humidity"):
            if(float(RawData["degree"])<10):
                Call_Function(Alert)
            else:
                Call_Function(Close)
    if(RawData["roomNO"]=="*ROOM1202*"):
        if (RawData["title"]=="Temperature"):
            if(float(RawData["degree"])>23):
                Call_Function(Alart)
            else:
                Call_Function(Close)
        if (RawData["title"]=="Humidity"):
            if(float(RawData["degree"])<10):
                Call_Function(Alart)
            else:
                Call_Function(Close)
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(Server, Port, 60) 
client.loop_forever()