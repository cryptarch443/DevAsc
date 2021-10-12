from dnacentersdk import api
import json
import time
import calendar

dna = api.DNACenterAPI(base_url='https://sandboxdnac2.cisco.com', username='devnetuser',password='Cisco123!')

def get_siteTopology():

	########## GET SITE TOPOLOGY ##########
	sites = dna.topology.get_site_topology()
	#print(json.dumps(sites, indent=2, sort_keys=True))
	
	for site in sites.response.sites:
		if site.parentId == 'e95d9cef-2a00-4eb9-82df-01c3291410be':
			print('Site Name\t: ',site.name)
			for child_sites in sites.response.sites:
				if child_sites.parentId == site.id:
					print(f"Child Name\t: {child_sites.name}")
				for more_children in sites.response.sites:
					if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
						print(f"More Child Name\t: {more_children.name}")

def get_Vlan():

	########## Get VLAN details ##########
	vlans = dna.topology.get_vlan_details()
	#print(json.dumps(vlans, indent=2, sort_keys=True))

	for vlan in vlans.response:
		print(vlan)

def get_phyTopologyDet():

	########## Get Physical Topology Detail ##########
	phys_top = dna.topology.get_physical_topology()
	print(json.dumps(phys_top, indent=2, sort_keys=True))


def get_deviceDet():

	########## Get Device Details ##########
	devices = dna.devices.get_device_list()
	#print(json.dumps(devices, indent=2, sort_keys=True))

	for device in devices.response:
		print("Device Type\t: ", device.type)
		print("Device ID\t: ", device.id)
		print("Hostname\t: ", device.hostname)
		print("IP Address\t: ", device.managementIpAddress)
		print(" ")

	device = dna.devices.get_device_by_id("a25646c1-5c3d-4f18-b158-0f689a255a03")
	print(json.dumps(device, indent=2, sort_keys=True))

def healthCheck():

	########## Get Overall Client Health ##########
	epoch_datetime = calendar.timegm(time.gmtime())

	#client_health = dna.clients.get_overall_client_health(timestamp=str(epoch_datetime))
	client_health = dna.clients.get_overall_client_health(timestamp="")

	print(json.dumps(client_health, indent=2, sort_keys=True))
	print(' ')

#get_siteTopology()
#get_Vlan()
#get_phyTopologyDet()
#get_deviceDet()
healthCheck()