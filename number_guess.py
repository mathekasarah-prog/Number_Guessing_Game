import random

difficulty = input("Choose a difficulty level: (Hard, Medium, Easy)").lower() .strip()
if difficulty == "Hard":
    max_attempts = 5
    
elif difficulty == "Medium":
    max_attempts = 7
    
elif difficulty == "Easy":
    max_attempts = 10
    
else:
    print("Invalid difficulty. Please choose Easy, Medium or Hard.")
    

number = random.randint(1,100)

attempts_used = 0
guess = 0

while guess != number and attempts_used < max_attempts:


    guess = int(input("Guess a number from 1-100: "))
    
    attempts_used += 1
    
    remaining_guesses = max_attempts - attempts_used

    if guess == number:
        print("Congratulations, You guessed the number right")
        
    elif guess < number:
        print("Too Low! Please try again")
        
    else:
        print("Too High! Please try again")
        
        
        print(f"You have {remaining_guesses} guesses remaining.")
        
if guess != number:
    print("Game Over!")
    print(f"The correct number was {number}")
        
    