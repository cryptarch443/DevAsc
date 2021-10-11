import requests
import json

url = "https://10.10.20.58/ins"
username = 'admin'
password = 'Cisco123'

headers = {
  'Content-Type': 'application/json',
}

show_ip_interface_brief = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip interface brief",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(show_ip_interface_brief), headers=headers, auth=(username,password), verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))