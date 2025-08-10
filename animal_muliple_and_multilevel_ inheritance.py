class Animal:
		def __init__(self,name):
			self.name=name
		def eat(self):
			print(f"{self.name} is eating")
		def sleep(self):
			print(f"{self.name} is sleeping")
class prey(Animal):
	def flee( self):
		print(f"{self.name} is fleeing")
class predator(Animal):
	def hunt(self):
		print(f"{self.name} is hunting")
class goat(prey):
	pass
class lion(predator):
	pass
class bear(prey,predator):
	pass
g=goat("deekshu")
l=lion("nandhu")
b=bear("vinay")
b.eat()
b.sleep()
b.hunt()
b.flee()
