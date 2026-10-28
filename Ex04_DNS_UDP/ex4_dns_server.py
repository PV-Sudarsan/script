import socket

# Table of host names and IP addresses
dns_table = {
    "yahoo.com": "68.180.206.184",
    "gmail.com": "209.85.148.19",
    "cricinfo.com": "80.168.92.140",
    "facebook.com": "69.63.189.16",
}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 1362))
print("DNS server running... Press Ctrl+C to quit")

while True:
    data, addr = s.recvfrom(1024)
    host = data.decode().strip()
    print("Request for host", host)
    ip = dns_table.get(host, "Host Not Found")
    s.sendto(ip.encode(), addr)
