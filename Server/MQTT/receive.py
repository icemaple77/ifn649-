import random
import re
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
topic = "ifn649"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        #Z = re.split('[,]', msg.payload.decode())
        #print(Z[1])
    client.subscribe(topic)
    client.on_message = on_message


def publish(client):
    loop = True
    command = ''
    while loop == True and command != 'e':
        time.sleep(0.0001) 
        command = input("Enter a message please, enter 'e' to exit >> ")
        if(command != 'e'):
            msg = command
            result = client.publish(topic,msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"`#{result[1]}` Send `{command}` to topic `{topic}`")
                subscribe(client)
            else:
                print(f"Failed to send message to topic {topic}")



def menu():
    print("Welcome to smart home !")
    print("0 --> close")
    print("1 --> sub")
    print("2 --> pub")
    indicate = input("Enter a number please >> ")
    return indicate

def run():
    client = connect_mqtt()
    while True:
        entry = menu()
        if(entry =="1"):
            subscribe(client)
            client.loop_forever()
            # client.loop_start()
        if(entry =="2"):
            publish(client)
            
            
        
    


if __name__ == '__main__':
    run()
