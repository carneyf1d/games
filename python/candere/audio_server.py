import socket
import threading
import pyaudio
import socketserver

# Initialize PyAudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9000))
server_socket.listen(5)

def handle_client(client_socket):
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    while True:
        data = client_socket.recv(CHUNK)
        if not data:
            break
        stream.write(data)
    stream.stop_stream()
    stream.close()
    client_socket.close()

print("Server listening on port 9000...")
while True:
    client, addr = server_socket.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
