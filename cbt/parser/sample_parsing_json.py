import json

jsonobj = json.load(open('sample_parsing_json.json'))

print(jsonobj['People'])
print(type(jsonobj))

#Iterate print JSON
for person in jsonobj['People']:
	print (person)