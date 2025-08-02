''This project is used to play the game which i used to play in my childhood and named as rock,paper and  Scissors''' 

def snake_water_gun(you,opponent):
					if(you==opponent):
						print("draw")
					elif(you=='snake' and opponent=='water'):
						print("a won the game")
					elif (you=='water' and opponent=='gun'):
					        print("you won the game")
					elif (you=='gun' and opponent=='snake'):
					        print("you won the game")
					else:
						print("opponent won the game")
	
		  
		  
you=input(" you enter your choice :") 
opponent=input("opponent enter your choice :")
snake_water_gun(you,opponent)
		  

