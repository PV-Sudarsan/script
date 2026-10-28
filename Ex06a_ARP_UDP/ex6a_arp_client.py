import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter the Logical address (IP): ")
c.sendto(ip.encode(), ("localhost", 1308))

mac, addr = c.recvfrom(1024)
print("The Physical Address is:", mac.decode())
c.close()
