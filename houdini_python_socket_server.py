
import socket
import threading


def handle_client(conn):
    code = conn.recv(65536).decode()
    try:
        exec(code, {'hou': hou})
    except Exception as e:
        print("Houdini exec error:", e)
    conn.close()


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 5050))
    s.listen(1)
    print("Houdini socket server listening on port 5050...")
    while True:
        conn, _ = s.accept()
        threading.Thread(target=handle_client, args=(conn,)).start()


threading.Thread(target=start_server, daemon=True).start()

