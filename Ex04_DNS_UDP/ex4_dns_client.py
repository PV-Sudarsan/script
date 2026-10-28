import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = input("Enter the host name: ")
c.sendto(host.encode(), ("localhost", 1362))

data, addr = c.recvfrom(1024)
print("IP Address:", data.decode())
c.close()
