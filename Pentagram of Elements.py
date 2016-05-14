######################################################
#    Fire, Grass, Rock, Ice, Ground Pentagram        #
#                                                    #
#           Created by Parmvir Bath                  #
######################################################
from random import *

print("Fire, Grass, Rock, Ice, Ground Game!")
print("Choose an Element and the Computer will randomly choose one too\nFirst one to 5 wins! \n**************************** \nFire burns Grass \nFire melts Ice \nGrass covers Ground \nGrass covers Rock \nRock breaks Ice \nRock difuses Fire \nIce freezes Ground \nIce kills Grass \nGround erodes Rock \nGround covers Fire \n****************************")

element = ["fire", "grass", "rock", "ice", "ground"]
userScore = 0
computerScore = 0
y = int(input("How many games do you want to play?:"))
for x in range(1, y + 1):
    print("")
    print("#"*28)
    print ("ROUND", x)
    print("#"*28) 
    computerPick = choice ( element ) 
    choice1 = input("Choose one of the listed elements: fire, grass, rock, ice, or ground:")

    if computerPick == choice1:
        print("You both chose " + choice1, "so it's a tie!")
   

#User Chooses fire 
    elif choice1 == "fire":
        print("The computer chose", computerPick)
        if computerPick == "grass" or computerPick == "ice":
            print("fire beats", computerPick)
            userScore = userScore + 1

        elif computerPick == "rock" or computerPick == "ground":
            print(computerPick, "beats fire")
            computerScore = computerScore + 1
      
#User Chooses grass 
    elif choice1 == "grass":
        print("The computer chose", computerPick)
        if computerPick == "ground" or computerPick == "rock":
            print("grass beats", computerPick)
            userScore = userScore + 1

        elif computerPick == "ice" or computerPick == "fire":
            print(computerPick, "beats grass")
            computerScore = computerScore + 1

#User Chooses rock 
    elif choice1 == "rock":
        print("The computer chose", computerPick)
        if computerPick == "ice" or computerPick == "fire":
            print("rock beats", computerPick)
            userScore = userScore + 1

        elif computerPick == "ground" or computerPick == "grass":
            print(computerPick, "beats rock")
            computerScore = computerScore + 1


#User Chooses ice
    elif choice1 == "ice":
        print("The computer chose", computerPick)
        if computerPick == "ground" or computerPick == "grass":
            print("ice beats", computerPick)
            userScore = userScore + 1

        elif computerPick == "rock" or computerPick == "fire":
            print(computerPick, "beats ice")
            computerScore = computerScore + 1

#User Chooses ground
    elif choice1 == "ground":
        print("The computer chose", computerPick)
        if computerPick == "rock" or computerPick == "fire":
            print("ice beats", computerPick)
            userScore = userScore + 1

        elif computerPick == "ice" or computerPick == "grass":
            print(computerPick, "beats ice")
            computerScore = computerScore + 1

    else:
        print("ERROR. Try Again")
            
    print("Your score is", userScore)
    print("Computer's score is", computerScore)
    print("*"*28)

if userScore == computerScore:
    print("TIE GAME")
elif userScore > computerScore:
    print("YOU WON!")
else:
    print("YOU LOST!")
