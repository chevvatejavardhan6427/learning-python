cart=[]
total=0
menu={"apple": 2,
"pineapple":6,
"orange":3,
"popcorn":5,
"gobi":4,
"sprit":7,
"thumbsup":8}
for key, value in menu.items():
  print(f"{key:20}: ${value:.2f}")
while True:
	food=input("what you want (q to quit) : ")
	if food.lower()=="q":
		break
	else:
		cart.append(food)
	total+=menu.get(food)
print("-------your cart--------")
for item in cart:
	print(item,end=" ")
print()
print(f"your bill is ${total}")

	
