import app

initData = {
	'Users': [
	{'name': 'Jon', 'title': 'Manager'},
	{'name': 'Jamie', 'title': 'SRE'}
	]
}

class Initialization:
	def __init__(self):
		self.data = initData
		self.application = app.App()

	def loadData(self, DB):
		print(self.data)
		DB = self.data
		validate = self.application.runTest(DB)
		if validate:
			return DB
		else:
			raise Exception('Data not loaded')