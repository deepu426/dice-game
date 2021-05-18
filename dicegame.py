import random
import banner
red='\033[31m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
blue='\033[34m'

banner.banner()

y=2
def roll(player):
	n=random.randint(1,6)
	print( f"player {player} value is {n} \n")

while True:
	print(red+"do you want play the game")
	x=input("yes/no ==>")
	
	if x in "yes":
		try:
			print ("how many players")
			nop=int(input("no of players ==>")) 
			print("\n")
		
		
			while y!=0:
				for player in range(1,nop+1):
					print (f"do you want roll the dice player {player}")
					y=int(input("enter 1 to roll , 0 to exit ==> "))
					
					if y==1:
						roll(player)
					elif y==0:
						break
					else:
						print("invalid option \n")
		except:
				print("please enter intiger \n")					
			
	elif x in "no":
		break
		
	else:
		print ("invalid choice \n")