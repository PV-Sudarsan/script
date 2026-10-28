import socket

# MAC -> IP table
rarp_table = {
    "6A:08:AA:C2": "165.165.80.80",
    "8A:BC:E3:FA": "165.165.79.1",
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 1309))
print("RARP server waiting...")

while True:
    data, addr = s.recvfrom(1024)
    mac = data.decode().strip()
    ip = rarp_table.get(mac, "Not Found")
    print("MAC", mac, "->", ip)
    s.sendto(ip.encode(), addr)
