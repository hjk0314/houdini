# Copy "456.py" to "C:\Users\jkhong\Documents\houdini20.5\scripts"
# If there is no scripts folder in the path, create it.
# When you restart Houdini, you can check it in the Houdini python shell.
# >>> socket server listening on port 5050...
import os


pyPath = "C:/Users/hjk03/Desktop/git/houdini/houdini_python_socket_server.py"
if os.path.exists(pyPath):
    with open(pyPath, 'r', encoding='utf-8') as f:
        code = f.read()
    exec(code)
    print("Socket server started from 456.py")
else:
    print("houdini_socket_server.py not found.")

