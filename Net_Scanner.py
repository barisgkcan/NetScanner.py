import scapy.all as scapy
import optparse

#gui = get user input

def gui():
    prs_object = optparse.OptionParser()
    prs_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")

    (user_input,arguments) = prs_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address")

    return user_input

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1) 
    answered_list.summary()

user_ip_address = gui()
scan_network(user_ip_address.ip_address)