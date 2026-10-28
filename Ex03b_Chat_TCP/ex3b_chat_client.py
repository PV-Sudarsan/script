import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 9001))

while True:
    msg = input("Client: ")
    c.send(msg.encode())
    if msg == "end":
        break
    reply = c.recv(1024).decode()
    if not reply or reply == "end":
        break
    print("Server:", reply)

c.close()
