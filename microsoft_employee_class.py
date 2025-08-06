# This class demonstrates how to use the __init__ method to initialize and access object data.
class Microsoft:
	def __init__(self,name,salary,language):
		self.name=name
		self.salary=salary
		self.language=language
	def info(self):
		print(f"name : {self.name}\nsalary : {self.salary}\nlanguage : {self.language}")
a=input("enter your name:")
b=input("enter your salary:")
c=input("enter your language:")


e1=Microsoft(a,b,c)
e1.info()	
