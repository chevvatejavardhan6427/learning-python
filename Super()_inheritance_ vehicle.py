class vehicle:
	def __init__(self,model,colour):
		self.model=model
		self.colour=colour
class bike(vehicle):
	def __init__(self,model,colour,cc):
		super().__init__(model,colour)
		self.cc=cc
b=bike("classic(RE)","black",650)		
print(b.colour,b.model,b.cc)
