from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='Y2UzMjc2MTgtYWVjNy00MDQ2LWFhOTgtNGNhYWMyZDY3NmI5YmY1ZWZjNTctYmMy_P0A1_c38839ae-ee59-4e90-9c17-0218b16b043f')

########## Get Teams Info ##########
teams = api.teams.list()

for team in teams:
	print(team)
	if getattr(team, 'name') != 'Webex Team':
		create_team = api.teams.create('Webex Team')
		teamId = getattr(create_team, 'id')
	else:
		teamId = team.id

########## People ##########
print(api.people.me())
print(api.people.list())

########## Roles ##########
roles = api.roles.list()
print(roles)

########## Rooms ##########
rooms = api.rooms.list()
evaluator = False
for room in rooms:
	if room.title == 'Webex Room':
		evaluator = True
		roomId = room.id

if evaluator == False:
	new_room = api.rooms.create('Webex Room', teamId=teamId)

########## Message ##########
api.messages.create(roomId, text='Posted with Webex SDK')