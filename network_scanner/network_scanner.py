# terminal: route -n    (TO KNOW WHAT IS MY GATEWAY)
import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)


scan("10.0.2.1/24")

