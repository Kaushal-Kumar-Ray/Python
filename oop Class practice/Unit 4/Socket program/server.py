import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to a public host and port
server_socket.bind(('localhost', 9999))
server_socket.listen(5)

print("🔥 Server is live. Waiting for connections...")

# Accept connection
client_socket, addr = server_socket.accept()
print(f"👋 Connection from {addr}")

# Send a welcome message
client_socket.send(b'Hey there! You connected to the server.\n')

# Close it out
client_socket.close()
