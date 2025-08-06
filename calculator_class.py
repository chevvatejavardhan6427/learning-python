import math
class calculator:
	def info(self):
		a=int(input(" enter the nuber:"))
		print(f"square of {a}={a**2}\ncube of {a}={a**3}\nsquare root of {a}={math.sqrt(a)}")
n=calculator()
n.info()
