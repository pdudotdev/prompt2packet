import time
import logging
from scapy.sendrecv import send
from registry import PROTOCOLS

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

def send_packets(intent, test_mode=False):
    protocol = intent["protocol"]
    builder = PROTOCOLS[protocol]

    packets = []
    for i in range(intent["count"]):
        pkt = builder(intent, index=i)
        packets.append(pkt)

        if not test_mode:
            send(pkt, verbose=False)

        if intent["interval_ms"] > 0:
            time.sleep(intent["interval_ms"] / 1000)

    return {"sent": len(packets), "packets": packets}
