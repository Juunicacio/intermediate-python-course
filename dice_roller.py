def main():
	import random
	import time
	QUESTION1 = 'How many sides are the dice you would like to roll? \n'
	QUESTION2 = 'How many dice would you like to roll: 1, 2 or 3? \n'
	ASK_AGAIN = 'Input is not a number, asking again: '
	#	
	Players = []
	StillPlaying = "y"	
	#FOR LAYOUT TIME.SLEEP: DICE ROLLING WAITING...use:	
	DR0 = "Dice rolling, waiting"
	DR1 = "Dice rolling, waiting."
	DR2 = "Dice rolling, waiting.."	
	Waiting = [DR0, DR1, DR2]
	print("\nWelcome to the game!")
	while StillPlaying != "n" and StillPlaying != "N" :
		Players.clear()
		Players.append(input('Player 1 name? \n'))
		Players.append(input('Player 2 name? \n'))
		dice_size = input(QUESTION1)
		while not dice_size.isdigit():
			dice_size = input(ASK_AGAIN + QUESTION1)
		dice_size = int(dice_size)
		dice_rolls = input(QUESTION2)
		while not dice_rolls.isdigit():
			dice_rolls = input(ASK_AGAIN + QUESTION2)
		dice_rolls = int(dice_rolls)
		while dice_rolls < 1 or dice_rolls > 3:
			print( "Invalid range. You can roll only 1, 2 or 3 dice. Choose again.")
			dice_rolls = int(input('How many dice would you like to roll: 1, 2 or 3? \n'))
			#Round Starts
		Player_results = []
		for player in Players:
			dice_sum = 0
			time.sleep(1)
			print(f"\nThat" + "'" + "s your turn" + ", " + player + "!")
			time.sleep(0.8)
			#Dice rolling waiting
			for dr in Waiting:
				print (dr)
				time.sleep(0.8)		
			#
			for i in range(0, dice_rolls):
				roll = random.randint(1,dice_size)
				dice_sum = dice_sum + roll
				# or dice_sum += roll
				if roll == 1:
				  print(f'You rolled a {roll}! Critical Fail')
				elif roll == dice_size:
				  print(f'You rolled a {roll}! Critical Success!')
				else:
				  print(f'You rolled a {roll}')
				#print(f'You rolled a {roll}')
			print(f'\nYou have rolled a total of {dice_sum} \n')
			time.sleep(1)
			Player_results.append(dice_sum)
			#Results
		print(f"\n<<SCOREBOARD>>")
		print(f"Player " + Players[0] + " - " + str(Player_results[0]) + " points")
		print(f"Player " + Players[1] + " - " + str(Player_results[1]) + " points") 		
		if Player_results[0] > Player_results[1]:
			print(f"\n" + Players[0] + " won! Congratulations!!!!!")
		elif Player_results[1] > Player_results[0]:
			print(f"\nPlayer " + Players[1] + " won! Congratulations!!!!!")
		else:
			print(f"\nThe score is tied!")
		StillPlaying = input("\nGame over! Play again? (Type 'n' to end)\n")		
	time.sleep(0.4)
	print("\nThanks for playing, good bye!")
	Waiting.clear ()

if __name__== "__main__":
	main()