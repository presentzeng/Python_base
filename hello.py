#sub
class Ani(object):
	name = "test animal"
	def run(self):
		print('animal is running')

class Dog(Ani):
	pass

class Cat(Ani):
	pass

dog = Dog()
print(dog.name)