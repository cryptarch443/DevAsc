class Validator:
	def runTest(self, DB):
		print('Checking if app is ready...')
		if 'Users' in DB.keys():
			return True
		else:
			return False