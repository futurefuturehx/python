#!/usr/bin/env python
# --coding: utf-8 --
#简单的Gopher Client

import socket,sys

port = 70          #默认端口 70
host = sys.argv[1]
filename = sys.argv[2]

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(filename + "\r\n")

while 1:
  buf = s.recv(2048)
  if not len(buf):
    break
  sys.stdout.write(buf)

