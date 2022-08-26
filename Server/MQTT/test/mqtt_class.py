# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:08:04 2018

@author: Administrator
"""
import socket
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
class MY_MQTT():    
    def __init__(self,myIP,myPORT,myQOS):
        self.myIP=myIP
        self.myPORT=myPORT
        self.myQOS=myQOS
    
    def sendingData(self,topic,SendData):#qos:0至多一次，1至少一次，2只有一次    
        publish.single(topic, SendData, hostname=self.myIP,port=self.myPORT,qos=self.myQOS)
    
    def subData(self,topic):
        self.message = subscribe.simple(topic, hostname=self.myIP)
        return(self.message)
        
    def get_host_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip