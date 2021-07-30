class Observer():
	def update(self, subject):
		print("Observer: My subject just updated and told me about it")
		print("Observer: It's state is now - " + str(subject._state))

class Subject():

	_state = 0
	_observer = []

	def attach(self,observer):
		self._observer.append(observer)

	def detach(self, observer):
		self._observer.remove(observer)

	def notify(self):
		print("Subject: I'm notifying my observer...")
		for observer in self._observer:
			observer.update(self)

	def updateState(self, n):
		print("Subject: I've received a state update!")
		self._state = n
		self.notify()

s = Subject()

ob1 = Observer()
ob2 = Observer()
ob3 = Observer()

s.attach(ob1)
s.attach(ob2)
s.attach(ob3)

s.updateState(5)

s.detach(ob2)

s.updateState(4)