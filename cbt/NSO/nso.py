import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url_base = 'https://sandbox-nso-1.cisco.com/api'
auth = ('developer','Services4Ever')

# Other useful headers
# 'application/vnd.yang.api+json'
# 'application/vnd.yang.datastore+json'
# 'application/vnd.yang.data+json'

headers = {'Accept': 'application/vnd.yang.collection+json'}

response = requests.get(f'{url_base}/running/devices/device', auth=auth, headers=headers, verify=False)
#print(json.dumps(response, indent=2, sort_keys=True))
print(response)