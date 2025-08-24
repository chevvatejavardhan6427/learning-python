tem=float(input("enter temperature : "))
unit=(input("enter unit in which tem is calculated F/C :").upper())
if unit=="F":
	print(f"{tem}°F={round(5/9*(tem-32),2)}°C")
elif unit=="C":
	print(f"{tem}°C={round(9/5*(tem)+32,2)}°F")
else:
	print("you have entered invalid Temperature unit")

