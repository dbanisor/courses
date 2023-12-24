# Client Side Chat Room

import socket, threading

# Define constants to be used
# DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', DEST_PORT))

def send_message():
    '''Send a message to the server to be broadcast'''
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))


def receive_message():
    '''Receive an incoming message from the server'''
    while True:
        try:
            # Receive an incoming message from the server.
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            # Check for the NAME flag, else show the message
            if message == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # An error occured, close the connection
            print("An error occured...")
            client_socket.close()
            break

# Create threads to continuously send and receive messages
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

# Start the client
receive_thread.start()
send_thread.start()