import socket

# 1. Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # 3. Send data
    message = "Hello, TCP Server!"
    client_socket.sendall(message.encode())

    # 4. Receive the server's response
    data = client_socket.recv(1024)
    print(f"Server replied: {data.decode()}")
finally:
    # 5. Close the socket
    client_socket.close()