import socket
import pickle

sock = socket.socket()
sock.connect(('localhost', 9090))
d = {"a": [123, 45], "b": [234, 12]}
sock.send(pickle.dumps(d))

i = 0

while True:
    data = sock.recv(1024)
    print(data)
    if i > 6:
        break
    i += 1
sock.close()

