import socket

# create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server address and port
host = '127.0.0.1'
port = 12345


print(f"Connecting to server at {host}:{port}")

while True:

    # send msg to server
    msg = input("You: ")
    client_socket.sendto(msg.encode(), (host,port))

    if msg.lower() == 'exit':
        print("Chat closed by client.")
        break

    # receive response from server
    data, _ = client_socket.recvfrom(1024)  # buffer size is 1024 bytes
    print(f"Server: {data.decode()}")