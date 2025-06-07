# import the required socket library
import socket
# get the hostname of the local machine
hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)
# print the hostname and IP address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
# print the timeout value
print(socket.gethostbyaddr(ip_address))
# print the IP address of the local machine)

