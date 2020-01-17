import socket

LOCAL_BIND_PORT = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', LOCAL_BIND_PORT))
s.listen(1)
s.close()
