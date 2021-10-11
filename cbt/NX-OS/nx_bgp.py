import requests
import json
from pprint import pprint

url = "https://10.10.20.58/ins"
username = 'admin'
password = 'Cisco123'

headers = {
  'Content-Type': 'application/json',
}

########## LOGIN WITH NX-API REST ##########
auth_url = 'https://10.10.20.58/api/mo/aaaLogin.json'
auth_body = {
    "aaaUser": {
        "attributes": {
            "name": username,
            "pwd": password
        }
    }
}

auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token

########## CONFIGURE ADVERTISE BGP NETWORK NX-API REST ##########
bgpAdvPrefix_url = 'https://10.10.20.58/api/node/mo/sys/bgp/inst/dom-default/af-[ipv4-ucast].json'

bgpAdvPrefix_body = {
	"bgpAdvPrefix": {
		"attributes": {
			"addr": "192.168.1.0/30",
			"dn": "sys/bgp/inst/dom-default/af-[ipv4-ucast]/prefix-[192.168.1.0/30]"
		}
	}
}

bgpAdvPrefix_response = requests.post(bgpAdvPrefix_url, data=json.dumps(bgpAdvPrefix_body), headers=headers, cookies=cookies, verify=False).json()

########## CONFIGURE ADVERTISE BGP NETWORK NX-API CLI ##########
bgpAdvPrefix_cli_body = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "sid",
    "input": "router bgp 65535 ;address-family ipv4 unicast ;network 192.168.1.4/30",
    "output_format": "json"
  }
}

bgpAdvPrefix_cli_response = requests.post(url, data=json.dumps(bgpAdvPrefix_cli_body), headers=headers, auth=(username,password), verify=False).json()

########## CONFIGURE BGP PEER NX-API REST ##########
bgpPeer_url = 'https://10.10.20.58/api/node/mo/sys/bgp/inst/dom-default/peer-[192.168.1.1].json'

bgpPeer_body = {
	"bgpPeer": {
		"attributes": {
			"addr": "192.168.1.1",
			"adminSt": "enabled",
			"asn": "64880"
		}
	}
}

bgpPeer_response = requests.post(bgpPeer_url, data=json.dumps(bgpPeer_body), headers=headers, cookies=cookies, verify=False).json()

########## CONFIGURE INTERFACE DESCRIPTION NX-API REST ##########
l1PhysIf_url = 'https://10.10.20.58/api/mo/sys/intf/phys-[eth1/1].json'

l1PhysIf_body = {
	"l1PhysIf": {
		"attributes": {
			"descr": 'Test Description Dulu'
		}
	}
}

l1PhysIf_response = requests.post(l1PhysIf_url, data=json.dumps(l1PhysIf_body), headers=headers, cookies=cookies, verify=False).json()
