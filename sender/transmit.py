import time
from scapy.sendrecv import send
from registry import PROTOCOLS
from config import DEFAULT_INTERFACE, SEND_ENABLED

def send_packets(plan):
    builder = PROTOCOLS[plan["protocol"]]["builder"]
    sent = 0

    for _ in range(plan["count"]):
        pkt = builder(plan["template"])

        if SEND_ENABLED:
            send(pkt, iface=DEFAULT_INTERFACE, verbose=False)
        else:
            print("[DRY-RUN]", pkt.summary())
        
        sent += 1

        if plan["interval_ms"] > 0:
            time.sleep(plan["interval_ms"] / 1000)

    return {"sent": sent}
