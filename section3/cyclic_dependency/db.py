from init import Initizalization

class DB:
	def __init__(self):
		self.DB = None

	def setupDB(self):
		print('Creating database...')
		self.DB = {}
		init = Initizalization()
		self.DB = init.loadData(DB)