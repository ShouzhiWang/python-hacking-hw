#! /usr/bin/python3

import socket
s = socket.socket()

ip = input("Please enter target IP address:")

try:
    s.connect((ip, 21)) 
except:
    print("no answer")

ans = s.recv(1024)

print(ans)

s.close