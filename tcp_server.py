import socket

# 1. Create a TCP/IP socket (SOCK_STREAM means TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# 3. Listen for incoming connections (max 1 queued connection)
server_socket.listen(1)
print("TCP Server listening on port 12345...")

# 4. Wait for a client to connect
connection, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

try:
    # 5. Receive data and send a response
    while True:
        data = connection.recv(1024)
        if not data:
            break # No more data from client
        
        print(f"Received: {data.decode()}")
        connection.sendall(b"Message received by TCP Server")
finally:
    # 6. Clean up the connection
    connection.close()
    server_socket.close()