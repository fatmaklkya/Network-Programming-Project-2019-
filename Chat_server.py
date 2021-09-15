#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Bir tane socket nesnesi oluşturulur.
#AF_INET ıpv4 adresini belirler, sock_stream bağlantı yönelimli tcp protokolü anlamına gelir

host = socket.gethostname()   # Yerel makinenin ismi alınır.

port = 12347   # Servis için bir tane port numarası belirlenir.

s.bind((host, port))   # Yerel makine ismi ile port numarası bağlanır.

# İstemci bağlantısı için port dinlemesi başlatılır.
s.listen(10)  # -> 10 istemci bağlanabilir.


c, addr = s.accept()  # istemci ve adresi kabul edilir.

c.sendall(bytes("Merhaba!".encode("utf-8")))   # Bağlanan istemciye hoşgeldin mesajı gönderilir. #utf-8 bayt 

print('{} bağlandı.'.format(addr))   # Bağlantı adresi sunucu ekranına bastırılır.


# Sunucunun sürekli açık kalması için sonsuz döngüye ihtiyacımız var.
# Veya mesaj adediyle veya başka parametrelerle döngü sonlu da olabilir...
while True:
    # İstemciden gelen, ara bellek boyutu 1024 olan,
    # byte tipindeki mesaj stringe dönüştürülür.
    # Bu string'in ilk elemanı hariç diğer elemanları data isminde
    # bir değişkene atanır.
    data = str(c.recv(1024))[1:]
    # Eğer istemciden mesaj gelmişse
    if data:
        
        print("İstemci: {}".format(data))   # İstemcinin mesajını bastır.
        
        respond = input("Sunucu: ").encode("utf-8")   # İstemciye göndereceğimiz mesajı yazalım.
        
        if respond == b"exit":   # Mesaj "exit" ise programdan çıkalım.
            exit()
            
        # Diğer her türlü durumda mesajımız karşı tarafa gitsin.
        else:  # İstemciye mesaj byte verisi olarak gönderilir.
            c.sendall(bytes(respond))
