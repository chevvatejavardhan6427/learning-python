import math
c=input("Enter your math operation (+,-,/,*,power,square root): ")
if c in ["+","-","/","*"]:
	a=int(input("enter a number 1 : "))
	b=int(input("enter a number 2 : "))
	if c=="+":
		print(a+b)
	elif c=="-":
		print(a-b)
	elif c=="*":
		print(a*b)
	elif c=="/":
		if b!=0:
			print(a/b)
		else:
			print("undefine")
elif c=="power":
	a=int(input("enter a number  : "))
	b=int(input(f"enter power you want  for {a}: "))
	print(pow(a,b))
else :
	a=int(input("enter a number  : "))
	if a>=0:
		print(math.sqrt(a))
	else:
		print("you have entered  negative number please enter positive value  ")
	
	

