import requests
import json

#Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = 'Y2UzMjc2MTgtYWVjNy00MDQ2LWFhOTgtNGNhYWMyZDY3NmI5YmY1ZWZjNTctYmMy_P0A1_c38839ae-ee59-4e90-9c17-0218b16b043f'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

def createTeam(teamName):
	
	########## Create a Team ##########
	url = 'https://webexapis.com/v1/teams'
	
	body = {
		"name": teamName
	}
	
	post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()
	print(post_response)
	

def getTeam():

	########## Get a Team List ##########
	url = 'https://webexapis.com/v1/teams'

	get_response = requests.get(url, headers=headers).json()
	teams = get_response['items']
	for team in teams:
		teamName = team['name']
		teamId = team['id']
		print('Team Name\t: ', teamName)
		print('Team ID\t\t: ', teamId)

def createRoom(roomName, teamName):

	########## Create a Room ##########
	room_url = 'https://webexapis.com/v1/rooms'
	team_url = 'https://webexapis.com/v1/teams'

	get_teams = requests.get(team_url, headers=headers).json()
	teams = get_teams['items']

	for team in teams:
		if team['name'] == teamName:
			teamId = team['id']

	body = {
		"title": roomName,
		"teamId": teamId
	}

	room_post = requests.post(room_url, headers=headers, data=json.dumps(body)).json()
	print(room_post)

def getRoom():

	########## Get a Room List ##########
	url = 'https://webexapis.com/v1/rooms'

	get_rooms = requests.get(url, headers=headers).json()

	rooms = get_rooms['items']
	for room in rooms:
		title = room['title']
		roomId = room['id']
		print("Room Name\t: ", title)
		print("Room ID\t\t: ", roomId)

def sendMessage(roomName):

	########## Post A Message to the Room ##########
	msg_url = 'https://webexapis.com/v1/messages'
	room_url = 'https://webexapis.com/v1/rooms'

	get_rooms = requests.get(room_url, headers=headers).json()
	rooms = get_rooms['items']

	for room in rooms:
		if room['title'] == roomName:
			roomId = room['id']
			roomName = room['title']

	msg_body = {
		'roomId': roomId,
		'text': 'ALERT : Interface on device xyz is down'
	}

	msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()

########## Execute ##########
createTeam("Webex Team")
createRoom("Webex Room", "Webex Team")
getTeam()
getRoom()
sendMessage('Webex Room')