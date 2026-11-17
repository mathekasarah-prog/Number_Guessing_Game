# Number Guessing Game

A command-line number guessing game written in Python. Pick a difficulty, enter your username, and try to guess the secret number between 1 and 100 before you run out of attempts. Your results are saved to a local leaderboard.

## Features

- **Three difficulty levels** that change how many guesses you get
- **Hint system**: after your 3rd wrong guess, the game tells you whether the number is divisible by 2
- **High score tracking**: winning scores are saved to `high_scores.txt`
- **Leaderboard**: shows the top 5 players, ranked by fewest attempts
- **Input validation** for the difficulty selection

## Difficulty Levels

| Difficulty | Max Attempts |
|------------|--------------|
| Easy       | 10           |
| Medium     | 7            |
| Hard       | 5            |

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries needed (only the built-in `random` module)

## How to Run

1. Save the script, for example as `guessing_game.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python guessing_game.py
   ```

   (On some systems you may need to use `python3` instead of `python`.)

## How to Play

1. Choose a difficulty: `Easy`, `Medium`, or `Hard` (case-insensitive).
2. Enter your username.
3. The game picks a random number between 1 and 100.
4. Enter your guesses. After each one, the game tells you if it was too low or too high and how many guesses remain.
5. After your 3rd incorrect guess, you get a hint about whether the number is divisible by 2.
6. Win by guessing the number within your allowed attempts. If you run out, the game reveals the correct number.

## Example Session

```
Choose a difficulty level: (Hard, Medium, Easy): medium
Enter your username: Sam

 I'm thinking of a number between 0 and 100!
Guess a number from 1-100: 50
Too Low! Please try again
You have 6 guesses remaining.
Guess a number from 1-100: 75
Too High! Please try again
You have 5 guesses remaining.
Guess a number from 1-100: 62
Congratulations, You guessed the number right

===== LEADERBOARD =====
1. Sam - 3 attempts
```

## High Scores

- Winning scores are appended to `high_scores.txt` in the same directory as the script, in the format `username,attempts`.
- The file is created automatically after the first win.
- The leaderboard displays the top 5 entries, sorted by fewest attempts.
- If no scores exist yet, the game displays a message saying so.

## Project Structure

```
.
├── guessing_game.py    # Main game script
├── high_scores.txt     # Created automatically after the first win
└── README.md
```

## Known Limitations / Future Improvements

- Entering a non-numeric guess will crash the game (no validation on guesses yet).
- Usernames containing a comma can break the leaderboard parsing.
- The intro text says "between 0 and 100", while the number is actually chosen from 1 to 100.
- Ideas for later: replay option, more hint types, difficulty shown on the leaderboard.

## License

This project is open for personal and educational use.
