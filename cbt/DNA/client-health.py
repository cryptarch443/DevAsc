import requests
import json

########## LOGIN ##########
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

username = 'devnetuser'
password = 'Cisco123!'

response = requests.post(url, auth=(username, password)).json()
#print(response)
token = response['Token']

########## Get Overall Client Health ##########

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

querystring = {"timestamp": ""}

headers = {
	'x-auth-token': token,
}

response = requests.get(url, headers=headers, params=querystring).json()

#print(json.dumps(response, indent=2, sort_keys=True))

print(f"Total Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response['response'][0]['scoreDetail']

for score in scores:
	if score['scoreCategory']['value'] == 'WIRED':
		print(f"\nWired Clients: {score['clientCount']}")
		score_values = score['scoreList']
		for score_value in score_values:
			print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")

	elif score['scoreCategory']['value'] == 'WIRELESS':
		print(f"\nWireless Clients: {score['clientCount']}")
		score_values = score['scoreList']
		for score_value in score_values:
			print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")