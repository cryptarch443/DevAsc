import json
import sys
import requests
import urllib3
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

global_url = 'https://fmcrestapisandbox.cisco.com'
login_url = '/api/fmc_platform/v1/auth/generatetoken'
headers = {'Content-Type': 'application/json'}
username = 'sulthangha'
password = 'dJKMXkxG'

login_response = requests.post(f'{global_url}{login_url}', auth=(username,password), verify=False)

#Parse out the headers
response_header = login_response.headers
#Grab the token from the response header
token = response_header.get('X-auth-access-token', default=None)
#Set the token in the headers to be used in next call
headers['X-auth-access-token'] = token

def getDomains():
	domains_url = '/api/fmc_platform/v1/info/domain'
	domains_response = requests.get(f'{global_url}{domains_url}', headers=headers, verify=False).json()
	domainUUID = domains_response['items'][0]['uuid']
	return(domainUUID)

def getApplications():
	domainUUID = getDomains()
	apps_url = (f'/api/fmc_config/v1/domain/{domainUUID}/object/applications')
	apps_response = requests.get(f'{global_url}{apps_url}', headers=headers, verify=False).json()
	print("********** GET Application **********")
	print(json.dumps(apps_response, indent=2, sort_keys=True))

def getAccCtrlPol():
	domainUUID = getDomains()
	accCtrlPol_url = (f'/api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies')
	accCtrlPol_response = requests.get(f'{global_url}{accCtrlPol_url}', headers=headers, verify=False).json()
	print("********** GET Access Control Policies **********")
	print(json.dumps(accCtrlPol_response, indent=2, sort_keys=True))

getApplications()
getAccCtrlPol()