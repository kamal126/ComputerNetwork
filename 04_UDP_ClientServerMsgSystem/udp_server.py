import socket

#  create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to an address and port
host = '127.0.0.1' # localhost
port = 12345
server_socket.bind((host,port))

print(f"Server is running on {host}:{port}")

while True:
    #  Recive data from the client
    data, client_address = server_socket.recvfrom(1024)  # buffer size is 1024 bytes
    msg = data.decode()

    if msg.lower() == 'exit':
        print(f"Connection closed by client {client_address}")
        break

    print(f"From {client_address}: {msg}")

    #  Send a response back to the client
    reply = input("You: ")
    server_socket.sendto(reply.encode(), client_address)

    if reply.lower() == 'exit':
        print(" Server chat is closed.")
        break

# Close the socket
server_socket.close()
print("Server socket closed.")
