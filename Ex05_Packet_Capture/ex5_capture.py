# Simple packet capture using scapy (same idea as Wireshark)
# Install: pip install scapy   |  Run as Administrator / sudo
from scapy.all import sniff

def show(packet):
    print(packet.summary())

print("Capturing 10 packets...")
sniff(count=10, prn=show)
