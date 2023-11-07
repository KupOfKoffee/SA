Explanation:

import socket: Imports the socket module, which provides low-level networking functionality.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM): Creates a socket object. AF_INET specifies that this is an IPv4 address, and SOCK_STREAM indicates that this is a TCP socket for stream-based connections.

host = socket.gethostname(): Gets the local machine's hostname.

port = 12345: Defines a port number to listen on.

server_socket.bind((host, port)): Binds the socket to the specified address and port.

server_socket.listen(5): Starts listening for incoming connections. The argument 5 specifies that up to 5 pending connections will be allowed in the queue.

while True:: Starts an infinite loop to continuously accept connections.

client_socket, addr = server_socket.accept(): Accepts a new connection. client_socket is a new socket object specific to the connected client, and addr contains the address of the client.

print(f'Got connection from {addr}'): Prints a message indicating that a connection has been established.

message = 'Thank you for connecting': Defines a message to send to the client.

client_socket.send(message.encode('utf-8')): Sends the message to the client after encoding it to bytes.

client_socket.close(): Closes the client socket.


