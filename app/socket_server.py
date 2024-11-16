import os
import socket
import logging


def start_socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5680))  # 포트 5680에서 리슨
    server.listen(5)
    print("server listening")

    while True:
        client_socket, addr = server.accept()  # 클라이언트 연결 수락
        #logging.info(f"Connection from {addr}")
        print(f"Connection from {addr}")
        # 클라이언트에게 응답 전송
        message = "Hello from server!"  # 보낼 메시지
        client_socket.sendall(message.encode())  # 메시지를 바이트로 인코딩하여 전송

        client_socket.close()

if __name__ == "__main__":
    start_socket_server()
