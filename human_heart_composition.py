class Heart:
	def beat(self,name):
		self.name=name
		print(f"{self.name}'S heart is beating...")
class Human:
	def __init__(self,name):
		self.name=name
		self.heart=Heart()
	def live(self):
		self.heart.beat(self.name)
		print(f"{self.name} IS ALIVE")
a=input("enter your name : ")
h=Human(a.upper())
h.live()
