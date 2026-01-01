import time
import logging
from scapy.sendrecv import send
from registry import PROTOCOLS

#This will suppress all Scapy messages that have a lower level of seriousness than error messages
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

def send_packets(plan, test_mode):
    builder = PROTOCOLS[plan["protocol"]]["builder"]
    sent = 0

    for _ in range(plan["count"]):
        pkt = builder(plan["template"])

        if test_mode:
            send(pkt, verbose=False)
        else:
            print("[TEST]", pkt.summary())
        
        sent += 1

        if plan["interval_ms"] > 0:
            time.sleep(plan["interval_ms"] / 1000)

    return {"sent": sent}
