import db

class App:
	def __init__(self):
		self.running = False
		self.database = db.DB()

	def startProgram(self):
		print('Starting the app...')
		self.database.setupDB()
		self.running = True

	def runTest(self, DB):
		print('Checking if app is ready')
		if 'Users' in DB.keys():
			return True
		else:
			return False