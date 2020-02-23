class Person:
	def setName(self, name):
		self.name=name

	def sayHello(self):
		print('Hello {}'.format(self.name))		

p1=Person()
p2=Person()

p1.setName('Joihn Doe')		
p2.setName('Sally Smith')

p1.sayHello()
p1.sayHello()
