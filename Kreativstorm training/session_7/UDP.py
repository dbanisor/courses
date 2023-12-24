
'''BUILDING A UDP SERVER LOCALLY, ON THIS MACHINE'''



import socket

server_address = ('localhost', 12345)       # IP address and port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(server_address)

print(f"UDP server is listening on {server_address}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received data from {client_address}: {data.decode()}")

    response = "Server received your message!"
    server_socket.sendto(response.encode(), client_address)



############################## THIS WILL BE WRITTEN FROM THE CLIENT SIDE ON A DIFFERENT IDE ##############################

# import socket
#
# server_address = ('localhost', 12345)
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# while True:
#     message = input("Enter a message to send to the server(or 'exit' to quit)")
#
#     if message.lower == 'exit':
#         break
#
#     client_socket.sendto(message.encode(), server_address)
#
#     data, _ = client_socket.recvfrom(1024)
#     print(f"Received from server: {data.decode()}")
#
# client_socket.close()