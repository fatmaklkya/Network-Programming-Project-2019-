#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12347

# Sunucuya bağlanalım.
s.connect((host, port))

# İstemci sunucuya bağlandıktan sonra
# Sunucunun yaptığı işin ayısını yapıyor.
while True:
    data = str(s.recv(1024))[1:]
    if data:
        print("Sunucu: {}".format(data))
        respond = input("Istemci: ").encode("utf-8")
        if respond == b"exit":
            exit()
        else:
            s.sendall(bytes(respond))