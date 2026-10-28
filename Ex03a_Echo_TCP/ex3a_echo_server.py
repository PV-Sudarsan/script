import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9000))
s.listen(1)
print("Echo server waiting...")

conn, addr = s.accept()
print("Connected to", addr)

while True:
    msg = conn.recv(1024).decode()
    if not msg or msg == "end":
        break
    print("Received:", msg)
    conn.send(msg.encode())      # echo back

conn.close()
s.close()
print("Socket Closed")
