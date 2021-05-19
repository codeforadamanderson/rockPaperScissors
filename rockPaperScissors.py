# Simple Rock Paper Scissors game based on code sent over by Jacob Anderson.
from random import choice

options = ('rock', 'paper', 'scissors')

while True:
    computer = choice(options)
    print("\nRock, Paper, or Scissors?")
    player = input("Enter 'q' to quit: ").lower()
    
    if player == computer:
        print(f"\nTie!  The computer also chose {player}.")
    elif player == "rock":
        if computer == "paper":
            print(f"\nYou lose!  {computer.title()} covers {player}.")
        else:
            print(f"\nYou win!  {player.title()} smashes {computer}.")
    elif player == "paper":
        if computer == "scissors":
            print(f"\nYou lose!  {computer.title()} cuts {player}.")
        else:
            print(f"\nYou win! {player.title()} covers {computer}.")
    elif player == "scissors":
        if computer == "rock":
            print(f"\nYou lose!  {computer.title()} smashes {player}.")
        else:
            print(f"\nYou win!  {player.title()} cuts {computer}.")
    elif player == "bomb":
        print("\nBoom!")
        break
    elif player == 'q':
        break
    else:
        print("\nThat's not a valid play.  Check your spelling!")