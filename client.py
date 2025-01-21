import socket

client_socket = socket.socket()

client_socket.connect(('localhost', 9999))

data = client_socket.recv(9999)

print(f"received from server: {data.decode()}")

client_socket.send(b"hello, server")
client_socket.close