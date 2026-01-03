import time
import signal
import logging
from colorama import Fore, Style
from scapy.sendrecv import send
from registry import PROTOCOLS

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

STOP_REQUESTED = False


def _handle_sigint(signum, frame):
    global STOP_REQUESTED
    STOP_REQUESTED = True


def send_packets(plan, test_mode=False):
    global STOP_REQUESTED
    STOP_REQUESTED = False  # reset for each run

    # Save previous SIGINT handler and install our own
    previous_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, _handle_sigint)

    builder = PROTOCOLS[plan["protocol"]]["builder"]
    packets = []

    try:
        for i in range(plan["count"]):
            if STOP_REQUESTED:
                print(
                    Fore.RED
                    + Style.BRIGHT
                    + "\n[!] Transmission interrupted by user."
                    + Style.RESET_ALL
                )
                break

            pkt = builder(plan["template"], index=i)
            packets.append(pkt)

            if not test_mode:
                send(pkt, verbose=False)

            if plan["interval_ms"] > 0:
                time.sleep(plan["interval_ms"] / 1000)

    finally:
        # Restore original SIGINT behavior so input() works again
        signal.signal(signal.SIGINT, previous_handler)

    return {"sent": len(packets), "packets": packets}
