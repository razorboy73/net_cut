#!/usr/bin/env python
import netfilterqueue

def process_packet(packet):
    print(packet)
    # forwards the packets with .accept()
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
# use bind to identify the queue number
queue.bind(0, process_packet)
queue.run()