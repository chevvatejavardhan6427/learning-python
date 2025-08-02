'''This project is used to play the game which i used to play in my childhood and named as rock,paper and  Scissors''' 

def snake_water_gun(you,opponent):
					options=["snake","water","gun"]
					if (you not in options or opponent not in options):
						print(" invalid input choose only from the given options")
						return
					if(you==opponent):
						print("draw")
					elif(you=='snake' and opponent=='water'):
						print("you won the game")
					elif (you=='water' and opponent=='gun'):
					        print("you won the game")
					elif (you=='gun' and opponent=='snake'):
					        print("you won the game")
					else:
						print("opponent won the game")
	
		  
		  
you=input(" you enter your choice :").lower()
opponent=input("opponent enter your choice :").lower()
snake_water_gun(you,opponent)
		  

