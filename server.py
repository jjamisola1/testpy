import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))

server.listen()

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    os_command = 'python /usr/app/src/test.py'
    os.system(os_command)
    client.close()
