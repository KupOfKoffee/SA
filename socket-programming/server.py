import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = socket.gethostname()
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections (up to 5)
server_socket.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print(f'Got connection from {addr}')

    # Send a thank you message to the client.
    message = 'Thank you for connecting'
    client_socket.send(message.encode('utf-8'))

    # Close the connection
    client_socket.close()
