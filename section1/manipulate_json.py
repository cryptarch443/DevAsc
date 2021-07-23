import json

with open('json_example.json', 'r') as file:
	data = json.load(file) #Converting a JSON file to a Python dictionary

user = data['user']
print(user['name'])
for role in user['roles']:
	print(role)

user['location']['city'] = 'Dallas'
with open('json_example-edited.json', 'w') as file:
	json.dump(data, file, indent=4) #Converting a Python dictionary to a JSON file