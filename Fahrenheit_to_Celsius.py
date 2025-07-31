#this function is used to convert fahrenheit scale to Celsius scale using recursion
def F_C():
	f=int(input("enter the temp. in f :"))
	return 5/9*(f-32) 
	
print(F_C(),"C")
