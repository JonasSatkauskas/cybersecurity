# terminal: route -n    (TO KNOW WHAT IS MY GATEWAY)
# .summary() is a part of scapy which shows more information
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]    # TIMEOUT IS A MUST

    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("---------------------------------------------------------")


scan("10.0.2.1/24")
