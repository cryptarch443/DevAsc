import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL and login body
# Note the body is a python dict - NOT a JSON body
url = 'https://10.10.20.90:443/j_security_check'
login_body = {
	'j_username': 'admin',
	'j_password': 'C1sco12345'
}

# Must use a session for SD-WAN
session = requests.session()

response = session.post(url, data=login_body, verify=False)

# Response return a 200 OK no matter what
# IF the response body contains any text then auth failed
if not response.ok or response.text:
	print('\nlogin failure\n')
	import sys
	sys.exit(1)
else:
	print('\nlogin worked! yay!\n')

# Get Devices
url = 'https://10.10.20.90:443/dataservice/device'

device_response = session.get(url, verify=False).json()['data']
#print(json.dumps(device_response, indent=2, sort_keys=True))
for device in device_response:
	print(f"Hostname : {device['host-name']}")
	print(f"IP : {device['system-ip']}")
	print(f"Model : {device['device-model']}")
	print(' ')