import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option('-i', dest=' interface', help='interface to change mac of')
	parser.add_option('-m',dest='mac', help="interface's new mac")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		print('pls give interface')
	elif not options.mac:
		print('pls give new mac')
	else:
		return options


def change_mac(options):
	subprocess.call(['ifconfig', options.interface, 'down'])
	subprocess.call(['ifconfig', options.interface, 'hw', 'ether', options.mac])
	subprocess.call(['ifconfig' options. interface, 'up'])


def get_new_mac(interface):
	ifconfig_result = subprocess.check_output(['ifconfig', interface], encoding='utf8')
	matches = re.search(r'(\w\w:){5}\w\w', ifconfig_result)
	return matches


change_mac(get_arguments())
print(f'Changed mac to {get_new_mac(get_arguments().interface).group(0)}')