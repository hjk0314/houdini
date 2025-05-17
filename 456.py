# 456.py
# Copy <this file> to "C:\Users\jkhong\Documents\houdini20.5\scripts"
# If there is no scripts folder in the path, create it.
import socket
import threading
import hou


PORT = 5050


def is_port_in_use(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", port))
        s.close()
        return False
    except OSError:
        return True


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", PORT))
    server.listen(1)
    print(f"Houdini socket server listening on port {PORT}...")
    while True:
        conn, _ = server.accept()
        code = conn.recv(65536).decode("utf-8")
        try:
            exec(code, {"hou": hou})
        except Exception as e:
            print("Exec error:", e)
        conn.close()


def ensure_server():
    if not is_port_in_use(PORT):
        threading.Thread(target=start_server, daemon=True).start()
    return


def on_hip_event(event_type):
    """ Check server status after creating a new file 
    (AfterClear) or opening a file (AfterLoad)
     """
    if event_type in (hou.hipFileEventType.AfterClear, hou.hipFileEventType.AfterLoad):
        ensure_server()


# Run once when Houdini starts
ensure_server()
# Registering callbacks for scene file related events
hou.hipFile.addEventCallback(on_hip_event)

