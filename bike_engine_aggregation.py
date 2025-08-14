class Engine:
	def __init__(self,cc,hp):
		self.cc=cc
		self.hp=hp
	def info(self):
		print(f"ENGINE HAVE {self.cc} CC with {self.hp} HP")
class bike:
	def __init__(self,engine):
		self.engine=engine
	def start(self):
		self.engine.info()
		print('BIKE IS STARTED')
e=Engine(650,47)
b=bike(e)
b.start()
