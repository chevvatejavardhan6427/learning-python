'''This project is used to play the game which i used to play in my childhood and named as rock,paper and  Scissors and now user and computer are going to play this game ''' 

import random
def snake_water_gun(you,computer):
					options=["snake","water","gun"]
					if (you not in options or computer not in options):
						print(" invalid input choose only from the given options")
						return
					if(you==computer):
						print("draw")
					elif(you=='snake' and computer=='water'):
						print("you won the game")
					elif (you=='water' and computer=='gun'):
					        print("you won the game")
					elif (you=='gun' and computer=='snake'):
					        print("you won the game")
					else:
						print("computer won the game")
	
		  
options=["snake","water","gun"]		  
you=input(" you enter your choice :").lower()
computer=random.choice(options)
print('computer choosen',computer)
snake_water_gun(you,computer)
