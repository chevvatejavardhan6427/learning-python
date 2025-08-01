'''this function is used to print stars like
***
**
*
using for loop'''




def stars():
 	n=int(input("enter a number :"))
 	for i in range (1,n+1):
 		print("*"*(n-i+1))
 		
 
 
print(stars())
