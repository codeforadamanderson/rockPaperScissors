# Version 1.0 - Initial code - Jacob Anderson
# Version 1.1 - Input case insensitivity - Adam Anderson
# Version 1.2 - Include quit option - Adam Anderson
# Version 1.3 - Added explosives - Adam Anderson

from random import randint
t=('Rock', 'Paper', 'Scissors')
computer=t[randint(0,2)]
player=False
while player==False:
    player=input("Rock, Paper, Scissors?").title()
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!", computer,"cut", player)
        else:
            print("You win!", player,"covers", computer)
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player=="Bomb":
        print("Boom!")
        player=False
        break
    else:
        print("That's not a valid play.  Check your spelling!")
    quit=input("Keep playing? (Y/N):").upper()
    if quit=="N":
        player=True
    else:
        player=False
    computer=t[randint(0,2)]
