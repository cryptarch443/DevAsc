import requests
import json
import pprint
import re

nxUser = 'admin'
nxPass = 'Cisco123'
nxIP = '10.10.20.58'

url = 'https://'nxIP'/ins'
nxHeader = {'content-type': 'application/json'}

payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp neighbor",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=nxHeader, auth=(nxUser,nxPass), verify=False).json()

pprint(response)

########## LOGIN WITH NX-API REST ##########
auth_url = 'https://'nxIP'/api/mo/aaaLogin.json'
auth_body = {
    "aaaUser": {
        "attributes": {
            "name": nxUser,
            "pwd": nxPass
        }
    }
}

auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['NX-cookie'] = token
print(cookies)

counter = 0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']

while counter < nei_count:
	hostname = response
	local_int = response
	remote_int = response

	body = {
		"l1PhysIf": {
			"attributes": {
				"descr": 'Connected to '+hostname+'Remote if is'+remote_int
			}
		}
	}

	counter += 1

	if local_int != 'mgmt0':
		int_name = str.lower(str(local_int[:3]))
		int_num = re.search(r'[1-9]/[1-9]*', local_int)
		int_url = 'https://'nxIP'/api/mo/sys/intf/phys-['+int_name+str(int_num.group(0))+'].json'
		post_response = requests.post(int_url, data=json.dumps(body), headers=nxHeader, cookies=cookies, verify=False).json()
		print(post_response)