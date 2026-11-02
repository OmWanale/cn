import socket

# 1. Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Define server address and port
server_address = ("127.0.0.1", 5000)

# 3. Send message to server
message = "Hello Server!"
client_socket.sendto(message.encode(), server_address)

# 4. Receive response from server
response, _ = client_socket.recvfrom(1024)
print("Message from server:", response.decode())

# 5. Close the socket
client_socket.close()