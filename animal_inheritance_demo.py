class Animal:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		
	def eat(self):
		print(f"{self.name} is eating")
		
		
	def sleep(self):
		print(f"{self.name} is sleeping")
		
		
class Dog(Animal):
		def sound(self):
			print("WOOF")
			
			
class Cat(Animal):
	def sound(self):
		print("MEOW")
		
		
class Mouse(Animal):
	def sound(self):
		print("SQUEAK")
		
		
animals=[Dog("SCIRUS",5),
Cat("SCUPY",3),
Mouse("MICKEY",8)
]

        
for animal in animals:
	print()
	print(f"NAME : {animal.name}\nAGE : {animal.age}")
	animal.sound()
	animal.eat()
	animal.sleep()
