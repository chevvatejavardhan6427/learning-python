from abc import ABC,abstractmethod
class vehicle(ABC):
	@abstractmethod
	def start (self):
		pass
	@abstractmethod
	def stop (self):
		pass
class bike(vehicle):
	def start (self):
		print("power on the beast mode")
	def stop(self):
		print("power off the beast mode")

b =bike()
b.start()
b.stop()
