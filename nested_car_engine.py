class Car:
	def __init__(self,brand):
		self.brand=brand
		self.engine=self.Engine(650,47)
	def about(self):
		print(f"brand:  {self.brand}")
		self.engine.show()
	class Engine:
		def __init__(self,cc,hp):
			self.cc=cc
			self.hp=hp
		def show(self):
			print(f"engine have {self.cc}cc with {self.hp}hp")
c=Car("BMW")
c.about()
