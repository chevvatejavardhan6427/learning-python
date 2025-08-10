class Bikes:
    # Initialize attributes that define the object
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

# Creating an object
b1 = Bikes("HUNTER 350 (ROYAL ENFIELD)", "BLACK")

# Printing attributes
print(f"COLOUR: {b1.colour} \nMODEL: {b1.model}")
