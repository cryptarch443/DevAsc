datacenter = 'APJ'

def generate_device_name(device, description):
	""" This function generate a name of a VNF running in RTP data center """
	datacenter = 'RTP'
	devices = {'firewall': 'Cisco_ASAv', 'router': 'Cisco_CSR-1000v'}

	device_type = devices[device]
	name = f"{device_type}--{description}--{datacenter}"


	return name

print(generate_device_name('firewall', 'mycompany-managed-firewall'))
print(datacenter)