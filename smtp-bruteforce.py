#!/usr/bin/python

from encodings import utf_8
import socket,sys,re

file = open("lista.txt")
for linha in file:
    linha = linha.encode()

    tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp.connect((sys.argv[1],25))
    banner = tcp.recv(1024)

    tcp.send(b"VRFY "+linha)
    user = tcp.recv(1024)
    if re.search(b"252",user):
        print (b"Usuario encontrado: "+user.strip(b"252 2.0.0"))