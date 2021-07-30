import xml.etree.ElementTree as ET

#Get the XML file data
stream = open('sample_parsing_xml.xml', 'r')

#Parse the data into an ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
	#Print the stringfied version of the element
	print(ET.tostring(e))
	print("")

	#Print the "id" attribute of the Element object
	print(e.get("id"))