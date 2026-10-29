from dataclasses import dataclass
from typing import Optional
DCCP_ACK = "ACK"
DCCP_DATA = "DATA"
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
        """Find the first data packet, skipping ACK entries."""
        while start < len(self.r_hist) and self.r_hist[start].type == DCCP_ACK:
            start += 1
        return self.r_hist[start] if start < len(self.r_hist) else None
    def removeAcksRecvHistory(self):
        """Remove ACK entries after the duplicate-ACK boundary."""
        index = self.num_dup_acks
        if index >= len(self.r_hist):
            return
        self.r_hist[index + 1:] = [
            entry for entry in self.r_hist[index + 1:]
            if entry.type != DCCP_ACK
        ]

    def removeOldDataPackets(self, seq_num, time):
        """Remove old data packets matching the sequence/time conditions."""
        index = self.num_dup_acks
        if index >= len(self.r_hist):
            return
        data_packet = self.findDataPacketInRecvHistory(index + 1)
        if data_packet is None:
            return
        start_index = self.r_hist.index(data_packet) + 1
        self.r_hist[start_index:] = [
            entry for entry in self.r_hist[start_index:]
            if not (
                entry.seq_num < seq_num
                and entry.t_recv < time
            )
        ]
# Example usage
agent = DCCPTFRCAgent(num_dup_acks=1)
agent.r_hist = [
    RHistEntry(10, 1.0, DCCP_DATA),
    RHistEntry(11, 1.1, DCCP_ACK),
    RHistEntry(12, 1.2, DCCP_DATA),
    RHistEntry(13, 1.3, DCCP_ACK),
    RHistEntry(14, 1.4, DCCP_DATA),
]
agent.removeAcksRecvHistory()
print("Receive history after removing ACKs:")
for entry in agent.r_hist:
    print(entry)
