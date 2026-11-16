import random

difficulty = input("Choose a difficulty level: (Hard, Medium, Easy)").lower() .strip()
if difficulty == "Hard":
    max_attempts = 5
    attempts_used =0
    
elif difficulty == "Medium":
    max_attempts = 7
    attempts_used = 0
    
elif difficulty == "Easy":
    max_attempts = 10
    attempts_used = 0
    
else:
    print("Invalid difficulty. Please choose Easy, Medium or Hard.")

number = random.randint(1,100)

guess = int(input("Guess a number from 1-100: "))

if number == guess:
    print("Congratulations, You guessed the number right")
    
elif number > guess:
    print("Too Low! Please try again")
    
elif number < guess:
    print("Too High! Please try again")
    