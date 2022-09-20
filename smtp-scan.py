#!/usr/bin/python
# -*- coding: utf_8 -*-

from encodings import utf_8
import socket,sys

if len(sys.argv) !=3:
    print ("\nModo de uso: python3 smtpenum.py IP usuario\n")
    sys.exit(0)

host = sys.argv[1]
user = str.encode(sys.argv[2])

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host,25))
banner = tcp.recv(1024)
print (banner)

tcp.send(b"VRFY "+user+b"\r\n")
user = tcp.recv(1024)
print (user)
