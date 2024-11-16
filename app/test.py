import socket

def connect_to_server():
    server_ip = "localhost"
    server_port = 5680

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))
        print(1)
        client_socket.sendall(b"Hello, Server!")
        print(2)
        data = client_socket.recv(1024)
        print(3)
        print(f"Received: {data.decode()}")

if __name__ == "__main__":
    connect_to_server()
