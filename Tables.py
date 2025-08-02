#this function is used to print tables
def tables(n):
	for i in range(1,11):
		k=n*i
		print(f"{n}×{i}={k}")
z=int(input("enter a number :"))
tables(z)
