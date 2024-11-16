import os
import socket
import uuid
from s3_uploader import upload_to_s3  # s3_uploader.py의 upload_to_s3 함수 임포트

def start_socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5680))  # 포트 5680에서 리슨
    server.listen(5)

    while True:
        client_socket, addr = server.accept()  # 클라이언트 연결 수락

        try:
            # 파일 이름은 새로 생성한 UUID로 설정
            generated_file_name = str(uuid.uuid4())

            # 파일 내용 바이너리로 받기
            file_stream = b""
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                file_stream += data

            if file_stream:

                # 파일을 S3에 업로드하고 URL 받기
                s3_url = upload_to_s3(file_stream, generated_file_name)

                if s3_url:
                    # S3 URL을 클라이언트에게 전송
                    client_socket.send(f"{s3_url}".encode('utf-8'))
                else:
                    client_socket.send("Error uploading file to S3".encode('utf-8'))
            else:
                client_socket.send("No file data received.".encode('utf-8'))

        except Exception as e:
            client_socket.send(f"Error: {str(e)}".encode('utf-8'))
        finally:
            client_socket.close()  # 연결 종료

if __name__ == "__main__":
    start_socket_server()
