# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:14:33 2018

@author: Administrator
"""

import mqtt_class
import paho.mqtt.subscribe as subscribe

mymqtt=mqtt_class.MY_MQTT("192.168.1.143",1883,1)
mymqtt.sendingData("time", "123")
while True:
    m=mymqtt.subData('time')
    print(m.payload)