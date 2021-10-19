from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
handle.login()

def getOrgInfo():
	########## ORG INFO ##########
	org = handle.query_classid(class_id="orgorg", hierarchy=True)
	#print(org)
	for organization in org:
		print(organization)

def getBladeInfo():
	########## BLADE INFO ##########
	servers = handle.query_classid("computeBlade")
	#print(servers)
	for server in servers:
		print(server)

	for server in servers:
		print(server.dn, server.num_of_cpus, server.available_memory)

	########## Specify DN Query ##########
	blade = handle.query_dn('sys/chassis-3/blade-1')
	print(blade)

getOrgInfo()
getBladeInfo()
handle.logout()