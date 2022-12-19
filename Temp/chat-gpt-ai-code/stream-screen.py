import cv2
import socket
import struct

def initialize_server():
    # Initialize server
    server_socket = socket.socket()
    server_socket.bind(('localhost', 8000))
    
    # Listen for connections
    server_socket.listen(0)
    
    # Accept a single connection
    connection = server_socket.accept()[0].makefile('rb')
    
    return connection

def stream_screen(connection): 
    try:
        # Initialize video stream
        stream_bytes = b' '
        while True:
            # Read stream of bytes from socket
            stream_bytes += connection.read(1024)
            first = stream_bytes.find(b'\xff\xd8')
            last = stream_bytes.find(b'\xff\xd9')
            if first != -1 and last != -1:
                jpg = stream_bytes[first:last + 2]
                stream_bytes = stream_bytes[last + 2:]
                image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow('image', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
        connection.close()
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    connection = initialize_server()
    stream_screen(connection)
    
