import json
import time
import paho.mqtt.client as mqtt
from threading import Thread

address = "127.0.0.1"
port = 1883


def pub():
    client = mqtt.Client()

    client.on_connect = lambda client, userdata, flags, rc: print(
        "Connected with result code: " + str(rc))
    client.on_message = lambda client, userdata, msg: print(
        msg.topic + " " + str(msg.payload))
    client.connect(address, port, 60)
    client.loop_start()
    while True:
        client.publish('Publish', payload="Server", qos=0)
        time.sleep(1)


def sub():
    client = mqtt.Client()
    client.on_connect = lambda client, userdata, flags, rc: print(
        "Connected with result code: " + str(rc))
    client.on_message = lambda client, userdata, msg: print(
        msg.topic + " " + str(msg.payload))
    client.connect(address, port, 60)
    client.subscribe('Upload', qos=0)
    client.loop_forever()


downData = Thread(target=pub)
rev = Thread(target=sub)
downData.start()
rev.start()