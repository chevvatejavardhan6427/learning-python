class Bikes:
    # Initialize attributes that define the object
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour
    
#defining a method(function) that define what object can do 
    def ability(self):
    	print("""Top Speed: Around 110–120 km/h (real-world)

0–60 km/h: ~4–5 seconds

Mileage: ~35–40 km/l (varies with riding style)

Cooling System: Air-oil cooled for better heat management in city rides

Ride Feel: Smooth low-end torque, ideal for city cruising and short highway rides
""")
# Creating an object
b1 = Bikes("HUNTER 350 (ROYAL ENFIELD)", "BLACK")

# Printing attributes
print(f"COLOUR: {b1.colour} \nMODEL: {b1.model}")
b1.ability()
