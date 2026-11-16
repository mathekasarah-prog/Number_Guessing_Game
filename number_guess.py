import random

difficulty = input("Choose a difficulty level: "("Hard, Medium, Easy"))
if difficulty == "Hard":
    attempts = 5
    
elif difficulty == "Medium":
    attempts = 7
    
elif difficulty == "Easy":
    attempts = 10

number = random.randint(1,100)

guess = int(input("Guess a number from 1-100: "))

if number == guess:
    print("Congratulations, You guessed the number right")
    
elif number > guess:
    print("Too Low!")
    
elif number < guess:
    print("Too High!")
    
else:
    print("Invalid Number")