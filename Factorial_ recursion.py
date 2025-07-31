# Recursive function to calculate factorial
def fac_(n):
    if n == 0 or n == 1:
        return 1
    return n * fac_(n - 1)

n = int(input("Enter number: "))
print(f"Factorial of {n} = {fac_(n)}")
	
	
