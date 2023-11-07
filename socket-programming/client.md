Explanation:

import socket: Imports the socket module.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM): Creates a socket object for the client.

host = socket.gethostname(): Gets the local machine's hostname.

port = 12345: Defines the port number to connect to.

client_socket.connect((host, port)): Connects to the server using the specified address and port.

data = client_socket.recv(1024): Receives data from the server, with a maximum buffer size of 1024 bytes.

print(data.decode('utf-8')): Decodes and prints the received data as a UTF-8 string.

client_socket.close(): Closes the client socket.