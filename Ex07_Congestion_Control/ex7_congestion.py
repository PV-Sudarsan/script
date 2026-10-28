# Simulation of TCP congestion control:
# Slow Start, Congestion Avoidance (AIMD), loss -> multiplicative decrease

cwnd = 1           # congestion window (segments)
ssthresh = 16      # slow start threshold
loss_rounds = [8, 15]   # RTT rounds where packet loss happens

print("Round  cwnd  ssthresh  Phase")
for rnd in range(1, 21):
    if rnd in loss_rounds:
        phase = "LOSS -> cwnd halved"
        ssthresh = max(cwnd // 2, 2)
        cwnd = ssthresh                 # multiplicative decrease
    elif cwnd < ssthresh:
        phase = "Slow Start"
        cwnd = cwnd * 2                 # exponential growth
    else:
        phase = "Congestion Avoidance"
        cwnd = cwnd + 1                 # additive increase
    print(f"{rnd:5}  {cwnd:4}  {ssthresh:8}  {phase}")
