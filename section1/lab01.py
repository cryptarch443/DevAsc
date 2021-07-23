import sys
from helper import *
from ruamel import yaml
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

#########################################
#			Procedure 1					#
#########################################
# Add print statement here
print('DevNet')
#########################################
#			Procedure 2					#
#########################################
print('##################')
print('###### YAML ######')
print('##################')
# Open the user.yaml file as read only
with open('user.yaml', 'r') as stream:
# Load the stream using safe_load
# Print the objet type
print('Type of user_yaml variable:')
print('---------------------')
#Iterate over the keys of the user_yaml and print them
print('Keys n user_yaml')
print('---------------------')
# Create a new instance of class user
# Assign values from the user_yaml to the object user
# Print the user object
print('User object:')
#########################################
#			Procedure 3					#
#########################################
print('##################')
print('###### JSON ######')
print('##################')
# Create JSON structure from the user object
# Print the created JSON structure
print('Print user_json')
print('---------------------')
# Create JSON structure with indent and sorted keys
print('JSON with indent and sorted keys')
#########################################
#			Procedure 4					#
#########################################
print('####################')
print('#XML - Element Tree#')
print('####################')
# Parse the user.xml file
# Get the root element
# Print the tags
print('Tags in the xml')
print('---------------------')
# Print the value of id tag
print('id tag value:')
print('---------------------')
# Find all element with the tag address in root
# Print the address in the xml
print('Addresses:')
print('---------------------')
# Print the elements in root with their tags and values
print('Print the structure')
# Parsing XML files with MiniDom
print('#####################')
print('### XML - MiniDom ###')
print('#####################')
# Parse the user.xml file
# Print the tags
print('Tags in the xml')
print('---------------------')
# Accessing element value
print('Accessing element value')
print('---------------------')
# Print the address in the xml
print('Addresses:')
print('---------------------')
# Print the elements in root with their tags and values
print('Print the structure')
#########################################
#			Procedure 5					#
#########################################
print('####################')
print('#  Use Namespaces  #')
print('####################')
# Parse the user.xml file
# Get the root element
# Define namespaces
# Set table as the root element
# Element in NS a
print('Elements in NS a:')
print('---------------------')
# Elements in NS b
print('Elements in NS b:')
print('---------------------')