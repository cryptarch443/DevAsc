import re

class ConfigurationParser:
	deviceConfig = open('config.txt', 'r').read()

	def parseCustomerNames(self):
		customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
		customerNames = re.findall(customerNamePattern, self.deviceConfig)
		return customerNames

	def parseCustomerVlan(self, customerName):
		intPattern = (
			r'interface GigabitEthernet0\/0\. ([0-9]+)\n encapsulation '
			r'dot1Q [0-9]+\n ip vrf forwarding %s'
			% (customerName)
		)
		allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
		return int(allCustomerSubInterfaces.group(1))

	def parseCustomerIPAddress(self, vlan):
		customerIpPattern = r'GigabitEthernet0/0.%s[ ]+([0-9\.]+)' % (vlan)
		customerIpAddress = re.search(customerIpPattern, self.deviceConfig)
		return customerIpAddress.group(1)

	def parseCustomerData(self):
		customerData = {}
		customerNames = self.parseCustomerNames()
		for customerName in customerNames:
			vlan = self.parseCustomerVlan(customerName)
			ip_address = self.parseCustomerIP(vlan)
			customerData[customerName] = [vlan, ip_address]
		return customerData
