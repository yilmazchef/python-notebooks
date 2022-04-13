import socket

HOST = "127.0.0.1"  # Standaard loopback interface adres (localhost).
PORT = 65432  # Portnummer (integer) om te luisteren (ports zonder privilege zijn groter dan 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.bind((HOST, PORT))
    srv.listen()

    conn, addr = srv.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
