# Ask the user to make a choice
# if choice is not valid 
# print an error
# let the computer to make a choice
# print choices (emojis)
# determine the winner
# Ask the user if they want to continue
# if not 
# terminate

import random
while True:

    Option = ('r','p','s')
    user = input("Rock, paper, scissors? (r/p/s) ")
    
    if user not in Option:
        print("Invalid choice!")
        continue

    computer = random.choice(Option)
    # print("computer "+ computer) #just to test 

    if user in Option: #user & comp ne jo bhi choose kiya hai voh hum show kr rahe hai
        print(f"you chose {user}")
        print(f"computer chose {computer}")

    # lose win logic
    if user == computer:
        print("Tie!")

    elif(
         (user == 'r' and  computer == 's') or 
         (user == 's' and computer == 'p') or 
         (user == 'p' and computer == 'r')
        ):
        print("you win")
    else:
        print("you lose")
        should_continue = input("continue? (y/n)")
        # print(should_continue)
        if should_continue == 'n':
            break
        else:
            continue

         
         