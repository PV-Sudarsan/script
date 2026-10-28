import random

random.seed(1)
packets = 100       # packets to send
loss_rate = 0.1     # 10% packets lost in network
link_time = 1       # time units per transmission

# UDP: send once, lost packets are not resent
udp_received = 0
for i in range(packets):
    if random.random() > loss_rate:
        udp_received += 1
udp_time = packets * link_time

# TCP: lost packets are retransmitted until delivered
tcp_sent = 0
for i in range(packets):
    while True:
        tcp_sent += 1
        if random.random() > loss_rate:
            break
tcp_time = tcp_sent * link_time

print("Protocol  Sent  Received  Lost  Time  Throughput")
udp_lost = packets - udp_received
udp_tp = udp_received / udp_time
tcp_tp = packets / tcp_time
print(f"UDP       {packets:4}  {udp_received:8}  {udp_lost:4}  {udp_time:4}  {udp_tp:.2f}")
print(f"TCP       {tcp_sent:4}  {packets:8}  {0:4}  {tcp_time:4}  {tcp_tp:.2f}")
