class Device:
	def __init__(self, hostname):
		self.hostname = hostname
		self.motd = None

	def show(self, p = None):
		if not p:
			return str(vars(self))
		elif hasattr(self, p):
			return (getattr(self, p))
		else:
			return f">> no attribute '{p}'"