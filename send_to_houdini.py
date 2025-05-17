# send_to_houdini.py
# Running "send_to_houdini.py" for the first time in vscode.
import os
import sys
import socket


HOST = "localhost"
PORT = 5050
BUFFER_SIZE = 65536


def send_to_houdini(code: str):
    """ Send a code string to a waiting socket server in Houdini."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(code.encode("utf-8"))
        print("Code sent to Houdini successfully.")
    except ConnectionRefusedError:
        print(f"Connection failed: Make sure the Houdini socket server is running on port {PORT}.")
    except Exception as e:
        print(f"Exception occurred while sending: {e}")


def main():
    if len(sys.argv) < 2:
        print("No file path argument. Please save the file first.")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    send_to_houdini(code)


if __name__ == "__main__":
    main()


