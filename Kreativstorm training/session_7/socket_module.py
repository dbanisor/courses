

# get host by name function

import socket

# hostname = 'google.com'
#
# try:
#     ip_address = socket.gethostbyname(hostname)
#     print(f"The IP address of {hostname} is {ip_address}")
#
# except socket.error as e:
#     print(f"Error: {e}")

#------------------------------------------------------------------------------------------------------#

# get all IP addresses that I have on my machine

try:
    hostname = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(hostname)[2]

    print(f"Hostname: {hostname}")
    print("IP adresses:")
    for ip in ip_addresses:
        print(ip)
except socket.error as e:
    print(e)

#------------------------------------------------------------------------------------------------------#

# create a port scanner
# scan the default gateway

# hostname = '192.168.0.1'
#
# port_list = [22, 53, 80, 8080, 443]    # 53 - look if DNS is open; 80, 8080 - look if http is open; 443 - look if https is open
#
# for port in port_list:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.settimeout(1)         # wait for 1 sec in case the traffic coming from a server is slower than out for loop, to ensure we receive a Reset answer (port closed, not listening) or a SYN.ACK answer (port open, listening)
#
#     try:
#         s.connect((hostname, port))
#         service_name = socket.getservbyport(port)
#         print(f"Post {port} ({service_name}) is open")
#     except:
#         print(f"Port {port} ({service_name}) is closed")
#
#     s.close()