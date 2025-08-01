#this function is used to calculate first n natural numbers using recursion
def sum(n):
	
	if n==1 :
		return 1
	return n+sum(n-1)
	
n=int(input("enter a number :"))
print(f" sum of first {n} natural numbers={sum(n)}")
	
