#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option('i', dest='iprange', help='ip range to scan for')
	(options, arguments) = parser.parse_args()
	if options.iprange:
		return options.iprange
	else:
		print('pls give ip range to scanf for')


def scan(ip_range):
	arp_request = scapy.ARP(pdst=ip_range)
	broadcast =scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	arp_request_broadcast = broadcast / arp_request
	answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	for item in answered:
		print(item[1].hwsrc)
		print(item[1].psrc)

		
	# print (arp_request_broadcast.summary())
	# print (broadcast.summary())
	# print (arp_request. summary())
	# scapy.ls(scapy.Ether())


 	scan(get_arguments())
 	