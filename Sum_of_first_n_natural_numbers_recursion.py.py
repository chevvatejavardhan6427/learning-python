#this function is used to calculate first n natural numbers using recursion
def sum(n):
	return (n*(n+1))/2
	
	
n=int(input("enter a number "))	
print(f"sum of first {n} natural numbers=",sum(n))
