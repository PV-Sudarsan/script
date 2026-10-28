import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 9000))

while True:
    msg = input("Client: ")
    c.send(msg.encode())
    if msg == "end":
        break
    print("Server:", c.recv(1024).decode())

c.close()
print("Socket Closed")
