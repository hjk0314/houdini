# send_to_houdini.py
import socket
import sys


def send_code(code):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 5050))
    s.sendall(code.encode('utf-8'))
    s.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, 'r', encoding='utf-8') as f:
            send_code(f.read())
