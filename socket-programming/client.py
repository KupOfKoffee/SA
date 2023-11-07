import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive data from the server
data = client_socket.recv(1024)

# Decode and print the received data
print(data.decode('utf-8'))

# Close the socket
client_socket.close()
