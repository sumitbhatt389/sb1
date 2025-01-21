import socket

server_socket = socket.socket()

server_socket.bind(('localhost', 9999))

server_socket.listen(5)

print("server is listening for connection...")

client_socket, client_address = server_socket.accept()
print(f"connection established with {client_address}")
client_socket.send(b"hello, client")

data = client_socket.recv(9999)

print(f"received from client: {data.decode()}")

client_socket.close()
server_socket.close()