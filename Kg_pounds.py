weight=float(input("Enter your weight : "))
unit=(input("Enter unit in which weight is measured : ").lower())
if unit=="kg":
	print(f"weight in pounds ={round(2.205*weight,2)}lb")
else:
	print(f"weight in kg ={round(weight/2.205,2)}kg")
