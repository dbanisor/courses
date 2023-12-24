

'''BUILDING A TCP SERVER LOCALLY, ON THIS MACHINE'''



import socket # the socket object: it is going to handle the incoming traffic. We will a have a port mapped to it,
                # an IP address mapped to it, also we will allow specific IP addresses to connect to us.


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # AF_INET = IP before traffic (referring to TCP object); SOCK_STREAM = TCP objects

server_socket.bind(("", 8080))          # binding an incoming address ("" = all possible addresses incoming) and establishing port address ("8080" means locally) to the objects

server_socket.listen(5)         # listen to 5 simultaneous TCP connections. If the 6th client will try to establish a connection with this socket it will not happen

print("Server is listening on port 8080...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    client_socket.send(b"Hello, client!!!")          # messages should be sent in bytes to socket because sockets don't understand strings, therefore the "b" in front of the message printed

    client_socket.close()       # closing the connection for that client only


############################## THIS WILL BE WRITTEN FROM THE CLIENT SIDE ON A DIFFERENT IDE ##############################

# >>> import socket
# >>>
# >>> client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# >>>
# >>> client_socket.connect(("127.0.0.1", 8080)) # or 127.0.0.1
# >>>
# >>> data = client_socket.recv(1024) # this client allows to receive from the server 1024 bytes
#
# >>> print("received: ", data.decode())

# >>>
# >>> client_socket.close()
