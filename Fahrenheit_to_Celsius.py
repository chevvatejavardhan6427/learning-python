#this function is used to convert fahrenheit scale to Celsius scale using recursio F_C()
def F_C():
	f=int(input("enter the temp. in f :"))
	return 5/9*(f-32) 
d=F_C()	
print(f"{round(d,2)} C")
