import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 9999))

# Receive data
msg = client_socket.recv(1024)
print(f"💬 Server says: {msg.decode()}")

client_socket.close()
