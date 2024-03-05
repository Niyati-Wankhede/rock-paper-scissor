import random

player = input("Choose Rock, Paper or Scissors!: ").lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()

print("Your virtual opponent has selected: ", computer)

start_game = input("Do you want to start the game? (Y or N): ")
if start_game.upper()[0] == 'Y':
    gameplay = True
else:
    gameplay = False

while gameplay:

    if player == computer:
        print('It is a tie!')

    elif player == 'scissor' and computer == 'paper':
        print('Scissor beats Paper, You win!')

    elif player == 'rock' and computer == 'scissor':
        print('Rock beats Scissor, You win!')

    elif player == 'paper' and computer == 'rock':
        print('Paper beats Rock, You win!')

    else:
        print("You lose")
    break




