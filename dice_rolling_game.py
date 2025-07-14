"""

loop 
Ask :roll the dice?
if user enters y
   generate two random numbers
   print them
if user enter N
   print thank you message
   Terminate
else
   print invalid choic

"""
import random

while True:
    choice = input("roll the dice ? (y/n): ").lower() #input give us string and string have this function 
# so if user enter the choice even in capital internally it change into small

    if choice == 'y':

        dice_num = int(input("How many dice they want to roll: "))

        i = 0
        while dice_num > i:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f'Roll {i+1}: ({die1}, {die2})')
            i = i+1

    elif choice == 'n':
        print("thankyou gameover")
        break

    else:
        print("invalid choice!")


# cleaner and shorter version
# while True:
#     choice = input("Roll the dice? (y/n): ").lower()

#     if choice == 'y':
#         rolls = int(input("How many times do you want to roll the dice pair? "))
        
#         for i in range(rolls):
#             die1 = random.randint(1, 6)
#             die2 = random.randint(1, 6)
#             print(f'Roll {i+1}: ({die1}, {die2})') # i+1 isliye kiya hai kiuki loop 0 se count krta hai
#     elif choice == 'n':
#         print("Thank you! Game over.")
#         break
#     else:
#         print("Invalid choice!")



#As we put entire logic in loop becoz of this we are again n again giving
#option to user input their choice if user again n again choose Y then we generate random no.
#and again user will get option to choose to play game or over it, 
#if user choose to N then elif condition will work and break the loop

# I add a feature to ask how many time a user want to roll a dice
# Note: We can also use a for loop here, which means we don't need to create or update the variable 'i' manually.
