
import random

exit==False
user_points=0
computer_points=0

while exit==False:
    options=["rock","paper","scissor"]
    user_input=input("choose rock,paper,scissors or exit:")
    computer_input=random.choice(options)

    if user_input=="exit":
        print("Game ended")
        exit=True

    if user_input=="rock":
        if computer_input == "rock":
            print("your input is rock")
            print("computer input is rock")
            print("it is tie")
        elif computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer win")
            computer_points=+1
        elif computer_input == "scissor":
            print("your input is rock")
            print("computer input is scissor")
            print("you win")
            user_points=+1

    elif user_input=="paper":
        if computer_input == "rock":
            print("your input is paper")
            print("computer input is rock")
            print("you win")
            user_points=+1 
        elif computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("it is tie")
        elif computer_input == "scissor":
            print("your input is paper")
            print("computer input is scissor")
            print("computer wins")
            computer_points=+1   

    elif user_input=="scissors":
        if computer_input == "rock":
            print("your input is scissors")
            print("computer input is rock")
            print("computer wins")
            computer_points=+1            
        elif computer_input == "paper":
            print("your input is scissors")
            print("computer input is paper")
            print("you wins")
            user_points=+1 
        elif computer_input == "scissor":
            print("your input is scissors")
            print("computer input is scissor")
            print("it is tie")
                    
    elif user_input!="rock" or user_input!="scissor" or user_input!="paper":
         print("Invalid Input")        
           
