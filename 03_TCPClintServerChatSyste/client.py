import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

# Client send data to the server

while True:
    
    # Send data to the server
    msg = input("You: ")
    client_socket.send(msg.encode())

    if msg.lower() == 'exit':
        print("You have exited the chat.")
        break

    # Receive reply from the server
    data = client_socket.recv(1024).decode()
    if data.lower() == 'exit':
        print("Server has exited the chat.")
        break

    print(f"Server: {data}")
    
# Close the connection
client_socket.close()
# client_socket.close()