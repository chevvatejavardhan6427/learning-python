class Battery:
	def __init__(self,brand,capacity):
		self.brand=brand
		self.capacity=capacity
	def info(self):
		print(f"{self.brand} WITH {self.capacity} MAH BATTERY")
class laptop:
	def __init__(self,battery):
		self.battery=battery
	def work(self):
		self.battery.info()
		print("laptop is working")
b1=Battery("DELL",5500)
l1=laptop(b1)
l1.work()
