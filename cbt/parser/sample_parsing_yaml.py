import yaml
from yaml import load, load_all

stream = open('sample_parsing_yaml.yaml', 'r')
document = load_all(stream, Loader=yaml.FullLoader)

print(type(document))

for doc in document:
	print(type(doc))
	print(doc)
	print(doc['People'][1]['FirstName'])