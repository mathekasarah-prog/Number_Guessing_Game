import random

#Choose difficulty level
difficulty = input("Choose a difficulty level: (Hard, Medium, Easy): ").lower() .strip()
if difficulty == "hard":
    max_attempts = 5
    
elif difficulty == "medium":
    max_attempts = 7
    
elif difficulty == "easy":
    max_attempts = 10
    
else:
    print("Invalid difficulty. Please choose Easy, Medium or Hard.") 
    
# Generate a random number
number = random.randint(1,100)

#Initialize variables
attempts_used = 0
guess = 0

#Start the guessing loop
while guess != number and attempts_used < max_attempts:


    guess = int(input("Guess a number from 1-100: "))
    
    attempts_used += 1
    
    if attempts_used == 3 and guess != number:

        if number % 2 == 0:
            print("Hint: The number is divisible by 2.")

        else:
            print("Hint: The number is not divisible by 2.")
        
    remaining_guesses = max_attempts - attempts_used
#player's guess
    if guess == number:
        print("Congratulations, You guessed the number right")
        
    elif guess < number:
        print("Too Low! Please try again")
        
    else:
        print("Too High! Please try again")
        
        
    print(f"You have {remaining_guesses} guesses remaining.")
#Check if the player lost
if guess != number:
    print("Game Over!")
    print(f"The correct number was {number}")
        
    