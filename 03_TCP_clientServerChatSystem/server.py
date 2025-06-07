import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

# Accept a connection from a client
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")
# Receive data from the client
while True:
    # Receive data from the client
    data = conn.recv(1024).decode()
    if data.lower() == 'exit':
        print("Client has exited the chat.")
        break
    print(f"Client: {data}")

    # Server send reply to the client
    reply = input("You: ")
    conn.send(reply.encode())

    if reply.lower() == 'exit':
        print("You have exited the chat.")
        break

# Close the connection
conn.close()
# server_socket.close()
