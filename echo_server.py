import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999


sock.bind((host, port))


sock.listen(2)

while True:

    connect, address = sock.accept()

    print("Client ile bağlantı kuruldu %s" % str(address))
    currentTime = time.ctime(time.time()) + "\r\n"
    connect.send(currentTime.encode('ascii'))

    data = connect.recv(4096).decode()

    if not data:
        break
    print("Client'ten gelen mesaj: " + str(data))

    connect.close()