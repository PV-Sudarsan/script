import os
import socket

print("Host name :", socket.gethostname())
print("IP address:", socket.gethostbyname(socket.gethostname()))

# Windows commands (on Linux use: ifconfig, traceroute, ping -c 4)
commands = [
    "ipconfig",
    "netstat -an",
    "nslookup google.com",
    "ping google.com",
    "tracert google.com",
    "arp -a",
]

for cmd in commands:
    print("\n========", cmd, "========")
    os.system(cmd)
