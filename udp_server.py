import socket

# 1. Create a UDP socket (SOCK_DGRAM means UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind the socket to IP address and port
server_socket.bind(("127.0.0.1", 5000))

# 3. Wait for messages from client
print("UDP Server is waiting for messages...")

# 4. Receive message from client
message, address = server_socket.recvfrom(1024)
print("Client address:", address)
print("Message from client:", message.decode())

# 5. Send response to client
response = "Hello Client, message received!"
server_socket.sendto(response.encode(), address)

# 6. Close the socket
server_socket.close()
print("Socket closed.")