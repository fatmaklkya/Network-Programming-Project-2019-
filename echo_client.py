import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect((host, port))
tm = s.recv(4096)

print("Server bağlantı saati: %s" % tm.decode('ascii'))

message = input(">>")


while message.lower().strip() != 'exit':
    s.send(message.encode())
    data = s.recv(4096).decode()
    print("Sunuya iletildi: " + str(message))
    message = input(">>")

    if message.lower().strip() == 'exit':
        s.close()
