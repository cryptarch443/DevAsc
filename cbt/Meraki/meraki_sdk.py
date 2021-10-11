import meraki
from pprint import pprint

dashboard = meraki.DashboardAPI('6bec40cf957de430a6f1f2baa056b99a4fac9ea0')

my_orgs = dashboard.organizations.getOrganizations()

pprint(my_orgs)

for org in my_orgs:
	if org['name'] == 'DevNet Sandbox':
		orgId = org['id']

print(orgId)

"""params = {}
params['organizationId'] = orgId

networks = meraki.Networks.getNetwork(orgId)
pprint(networks)"""