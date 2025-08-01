#This function is used to print a star pattern using for loop
def stars(n):
	for i in range (1,n+1):
		print("*"*(n-i+1))
		
		
n=int(input("enter a number :"))
stars(n)
