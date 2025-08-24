temp = int(input("Enter temperature: "))
raining = True

# Using AND
if temp > 0 and temp < 40:
    print("Good environment")
else:
    print("Bad environment")

# Using OR
if temp < 0 or temp > 40:
    print("Bad environment")
else:
    print("Good environment")

# Using NOT
if not raining:
    print("It's not raining")
else:
    print("It's raining")
  
