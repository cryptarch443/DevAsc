# Helper module with User class and additional functions
from datetime import date

## User class
class User:
	def __init__(self):
		self.id = None
		self.first_name = None
		self.last_name = None
		self.birth_date = None
		self.address = None
		self.score = None

	# Print the object
	def __repr__(self):
		return str(self.__dict__)

# User object serialization
def serializationUser(object):
	if isinstance(object, User):
		return object.__dict__

	if isinstance(object, date):
		return object.__str__()

## User for MiniDom
# Print the tags of a nodeList object
def printTags(nodeList):
	for node in nodeList:
		if node.nodeName != '#text':
			print(node.nodeName)

# Recursively print the node list children's name (tags) and its value
def printNodes (nodeList, level=0):
	for node in nodeList:
		if node.nodeName != '#text':
			print( (" ")*level + node.nodeName + ':' + node.firstChild.data)
			printNodes(node.childNodes, level+1)