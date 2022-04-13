import socket

HOST = "127.0.0.1"  # Standaard loopback interface adres (localhost).
PORT = 65432  # Portnummer (integer) om te luisteren (ports zonder privilege zijn groter dan 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clt:
    clt.connect((HOST, PORT))
    clt.sendall(b"Hello, world")
    data = clt.recv(1024)

print(f"Received {data!r}")
