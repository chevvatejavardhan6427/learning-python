#this function is used to convert Celsius scale to fahrenheit scale using recursion
def C_F():
	c=int(input("enter the temp. in c :"))
	return 9/5*(c)+32
	
print(C_F() ,"F")
