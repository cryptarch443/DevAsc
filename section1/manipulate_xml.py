import xml.etree.ElementTree as ET

with open('xml_example.xml', 'r') as file:
	mytree = ET.parse(file) #Converting an XML file to a Python ElementTree instance
	myroot = mytree.getroot()

user = myroot.find('user')
print(user.find('name').text)
for role in user.findall('roles'):
	print(role.text)

user.find('location').find('city').text = 'Dallas'
with open('xml_example-edited.xml', 'w') as file:
	mytree.write(file, encoding="unicode") #Saving an XML file from a Python ElementTree instance
