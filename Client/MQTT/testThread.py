#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import _thread as thread
import time
 
# 为线程定义一个函数
def print_time( threadName, delay):
   
   while True:
      
      
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
def print_time2( threadName, delay):
    
    while True:
        
       
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# 创建两个线程
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time2, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")
 

while 1:
   pass