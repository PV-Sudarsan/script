
from dataclasses import dataclass
ACK, DATA = "ACK", "DATA"
@dataclass
class RHistEntry:
    seq_num: int
    t_recv: float
    type: str
class DCCPTFRCAgent:
    def __init__(self, num_dup_acks=0):
        self.r_hist = []
        self.num_dup_acks = num_dup_acks
    def findDataPacketInRecvHistory(self, start=0):
        return next((e for e in self.r_hist[start:] if e.type == DATA), None)
    def removeAcksRecvHistory(self):
        i = self.num_dup_acks
        if i < len(self.r_hist):
            self.r_hist[i+1:] = [e for e in self.r_hist[i+1:] if e.type != ACK]
    def removeOldDataPackets(self, seq_num, time):
        i = self.num_dup_acks
        if i < len(self.r_hist):
            p = self.findDataPacketInRecvHistory(i+1)
            if p:
                j = self.r_hist.index(p) + 1
                self.r_hist[j:] = [e for e in self.r_hist[j:]
                                   if not (e.seq_num < seq_num and e.t_recv < time)]
agent = DCCPTFRCAgent(1)
agent.r_hist = [RHistEntry(10,1.0,DATA), RHistEntry(11,1.1,ACK),
                RHistEntry(12,1.2,DATA), RHistEntry(13,1.3,ACK),
                RHistEntry(14,1.4,DATA)]
agent.removeAcksRecvHistory()
print(*agent.r_hist, sep="\n")
