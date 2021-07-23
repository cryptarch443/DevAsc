import yaml

with open('yaml_example.yml', 'r') as file:
    data = yaml.safe_load(file)

user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)

user['location']['city'] = 'Dallas'
with open('yaml_example-edited.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
