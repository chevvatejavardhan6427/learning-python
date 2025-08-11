from abc import ABC,abstractmethod
import math
class Shape( ABC):
	@abstractmethod
	def area(self):
		pass
		
class Circle(Shape):
	def __init__(self,radius):
		self.radius=radius
	def area(self):
		print(f"AREA OF CIRCLE : {math.pi*self.radius**2:.2f}cm²")
class Square(Shape):
	def __init__(self,side):
		self.side=side
	def area(self):
		print(f"AREA OF SQUARE : {self.side**2:.2f}cm²")
class Triangle(Shape):
	def __init__(self,base,height):
		self.base=base
		self.height=height
	def area(self):
		print(f"AREA OF TRIANGLE : {self.base*self.height*0.5:.2f}cm²")
shapes=[ Circle(2),Square(4),Triangle(2,4)]
for shape in shapes :
	shape.area()
