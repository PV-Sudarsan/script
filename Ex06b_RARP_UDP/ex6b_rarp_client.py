import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mac = input("Enter the Physical address (MAC): ")
c.sendto(mac.encode(), ("localhost", 1309))

ip, addr = c.recvfrom(1024)
print("The Logical Address is (IP):", ip.decode())
c.close()
