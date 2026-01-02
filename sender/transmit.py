import time
import logging
from scapy.sendrecv import send
from registry import PROTOCOLS

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

def send_packets(plan, test_mode=False):
    builder = PROTOCOLS[plan["protocol"]]["builder"]
    packets = []

    for i in range(plan["count"]):
        pkt = builder(plan["template"], index=i)
        packets.append(pkt)

        if not test_mode:
            send(pkt, verbose=False)

        if plan["interval_ms"] > 0:
            time.sleep(plan["interval_ms"] / 1000)

    return {"sent": len(packets), "packets": packets}
