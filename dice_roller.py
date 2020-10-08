def main():
  import random
  dice_size = int(input('How many sides are the dice?'))
  dice_rolls = int(input('How many dice would you like to roll: 1, 2 or 3? \n'))
  dice_sum = 0
  while dice_rolls < 1 or dice_rolls > 3:
    print( "Invalid range. You can roll only 1, 2 or 3 dice. Choose again.")
    dice_rolls = int(input('How many dice would you like to roll: 1, 2 or 3? \n'))
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
  print(f'You have rolled a total of {dice_sum} \n')

if __name__== "__main__":
  main()