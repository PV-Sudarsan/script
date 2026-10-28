import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9001))
s.listen(1)
print("Chat server waiting...")

conn, addr = s.accept()
print("Client connected:", addr)

while True:
    msg = conn.recv(1024).decode()
    if not msg or msg == "end":
        break
    print("Client:", msg)
    reply = input("Server: ")
    conn.send(reply.encode())
    if reply == "end":
        break

conn.close()
s.close()
