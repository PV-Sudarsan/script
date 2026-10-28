import socket

# IP -> MAC table
arp_table = {
    "165.165.80.80": "6A:08:AA:C2",
    "165.165.79.1": "8A:BC:E3:FA",
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 1308))
print("ARP server waiting...")

while True:
    data, addr = s.recvfrom(1024)
    ip = data.decode().strip()
    mac = arp_table.get(ip, "Not Found")
    print("IP", ip, "->", mac)
    s.sendto(mac.encode(), addr)
