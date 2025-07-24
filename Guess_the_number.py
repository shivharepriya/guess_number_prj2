"""
1. generate a random number
2. loop
    1. Ask the user to make a guess
    2. if not a valid number
        print an error
    3. if number < guess
        print too low
    4. if number > guess
        print too high
    5. else
        print well done
"""
import random

# number_to_guess = random.randint(1,100)

# while True:
#     try:
#         guess = int(input("Guess the number between 1 and 100"))
#         if guess < number_to_guess:
#             print('Too low!')
#         elif guess > number_to_guess:
#             print('Too high!')
#         else:
#             print('congratulations! you guessed the no.')
#             break
#     except ValueError:
#         print("Please enter a valid number")



# solution 2
while True:
    guess = random.randint(1, 100)
    print(guess)

    chances = 3  # total chances

    while chances > 0:
        try:
            user = int(input("Guess the number between 1-100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue 
        # continue → loop wapis line 1 pe chala jaata hai: while chances > 0:
        # "You entered:" wali line SKIP ho jaati hai

        if user == guess:
            print("Congrats! You guessed it right.")
            break
        elif user > guess:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        chances -= 1
        if chances > 0:
            print(f"You have {chances} chance(s) left.\n")
        else:
            print(f"Out of chances! The correct number was {guess}.")
    
    #Ask if user want to play again 
    play_again = input("do you want to play again yes/no: ").lower()
    if play_again != 'yes':
        print("thank for playing")
        break

# Try-except ka maksad sirf error-prone code ko cover karna hota hai, 
# poora game logic nahi dalna chahiye (best practice wise)

