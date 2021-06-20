# terminal: route -n    (TO KNOW WHAT IS MY GATEWAY)
# .summary() is a part of scapy which shows more information
import scapy.all as scapy
import optparse


# Now that the program is working,
# I want you to use the optparse library I showed you in the previous section
# to extend this program and make it take the IP range through a command line argument.
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]    # TIMEOUT IS A MUST

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, 'mac': element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------------")
    for client in results_list:
        print(client['ip'] + '\t\t' + client['mac'])


scan_result = scan("10.0.2.1/24")
print_result(scan_result)
