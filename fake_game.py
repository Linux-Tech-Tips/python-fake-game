# Description: console game to guess whether a randomly generated number is odd or even, but the computer cheats

# Imports
import random

# Variables
userScore = 0
cpuScore = 0
running = True

# Function to check whether the guess is correct
def check(number, guess):
    global userScore, cpuScore
    # Number is even case
    if(number % 2 == 0):
        if(guess == "even"):
            print("You guessed correctly, the number was even")
            userScore += 1
        elif(guess == "odd"):
            print("You guessed wrong, the number was even")
            cpuScore += 1
        else:
            print("Invalid input: " + guess + ", please input even or odd")
            cpuScore += 1
    # Number is odd case
    else:
        if(guess == "odd"):
            print("You guessed correctly, the number was odd")
            userScore += 1
        elif(guess == "even"):
            print("You guessed wrong, the number was odd")
            cpuScore += 1
        else:
            print("Invalid input: " + guess + ", please input even or odd")
            cpuScore += 1

while(running):
    
    number = random.randint(1, 4)
    
    guess = input("Try to guess, is the number even or odd? (input even or odd) ").strip().lower()
    
    # Validating number
    # User ahead of cpu case (computer might cheat)
    if(userScore - cpuScore > 2):
        # Randomly deciding whether to cheat or not
        willCheat = random.randint(1, 3)
        # Will cheat case
        if(willCheat == 1):
            if(guess == "odd" or guess == "even"):
                print("You guessed wrong, the number was " + ("odd" if guess == "even" else "even"))
            else:
                print("Invalid input: " + guess + ", please input even or odd")
            cpuScore += 1
        # Won't cheat case
        else:
            check(number, guess)
    # User not ahead of cpu (just normal guess)
    else:
        check(number, guess)
    
    # Asking whether to continue playing
    print("The user has " + str(userScore) + " points so far, the PC has " + str(cpuScore) + " points so far")
    again = input("Do you want to continue playing? (yes/no) ")
    running = not again.strip().lower().startswith("n")
    print("")
