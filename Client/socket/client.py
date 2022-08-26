#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

#from bt.txt
import serial
import time
import string


ip_port = ('3.25.137.123', 8888)



# the name of file we want to send, make sure it exists
# filename = "data.csv"
# get the file size
# filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {ip_port}")
s.connect(ip_port) 
print("[+] Connected.")


ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

# send the filename and filesize
# s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
# progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
# with open(filename, "rb") as f:
while True:
    # if ser.in_waiting > 0:
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        print(cookedserial)
        s.sendall(cookedserial.encode())
    # if inp == "exit":   # 如果输入的是‘exit’，表示断开连接
    #     print("结束通信！")
    #     break
    # read the bytes from the file
    # bytes_read = f.read(BUFFER_SIZE)
    # if not bytes_read:
        # file transmitting is done
        # break
    # server_reply = s.recv(1024).decode()
    # print(server_reply)
    # we use sendall to assure transimission in 
    # busy networks
    # s.sendall(bytes_read)
    # update the progress bar
    # progress.update(len(bytes_read))
# close the socket
s.close()