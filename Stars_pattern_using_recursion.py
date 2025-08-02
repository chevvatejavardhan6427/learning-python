#this function is used to print star patten using recursion
def stars(n):
	if n==0:
		return
	print("*"*n)
	stars(n-1)
	
		
z=int(input("enter a number :"))
stars(z)	
