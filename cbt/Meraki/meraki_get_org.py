import requests
import json

url = "https://api.meraki.com/api/v1/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

response = requests.get(url, headers=headers, data=payload).json()

#print(json.dumps(response, indent=2, sort_keys=True))

for orgName in response:
  name = orgName['name']
  nameId = orgName['id']
  print('This organization', name, 'ID:', nameId, '\nHere networks of the organization')
  netUrl = 'https://api.meraki.com/api/v1/organizations/'+nameId+'/networks'
  getNetworks = requests.get(netUrl, headers=headers, data=payload).json()
  print(json.dumps(getNetworks, indent=2, sort_keys=True))