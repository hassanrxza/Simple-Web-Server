import socket as s
import threading

IPADDR = '127.0.0.1'
PORT = 9999


def main():
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.bind((IPADDR, PORT))
    server.listen(5)
    print(f"[*] Listening on {IPADDR}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_daemon = threading.Thread(target=handle_client, args=(client, ))
        client_daemon.start()


def handle_client(client: s.socket):
    with client as sock:
        request = sock.recv(1024).decode('utf-8').split(' ')[0:3]
        request = ' '.join(request)
        path = "../../../E-Project/Star Classes/JoinNow.html"
        print(f"[*] Received: {request}")

        try:
            with open(path, 'rb') as file:
                contents = file.read()
                if not contents:
                    exit(1)
                sock.send(b"HTTP/1.1 200 OK\r\n\r\n" + contents)
        except FileNotFoundError:
            sock.send(b"HTTP/1.1 400 Not Found!\r\n\r\n")


if __name__ == "__main__":
    main()
