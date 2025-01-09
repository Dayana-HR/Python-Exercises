import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100... ")
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': \t").lower()

if difficulty == 'easy':
    attempt = 10
    print("You have 10 attempts remaining to guess the number")
elif difficulty == 'hard':
    attempt = 5
    print("You have 5 attempts remaining to guess the number")
else:
    print("Invalid")

num = random.randint(1,100)

def guess_number(input_num):
    global num
    global attempt
    if input_num < num:
        attempt -= 1
        if attempt > 0:
            return False, f"Too low. \nGuess again \nYou have {attempt} attempts remaining."
        else:
            return False, f"You've run out of guesses. The num was {num}"
    elif input_num > num:
        attempt -= 1
        if attempt > 0:
            return False, f"Too high. \nGuess again \nYou have {attempt} attempts remaining."
        else:
            return False, f"You've run out of guesses. The num was {num}"
    else:
        return True, f"You did it! The number is {num}."

while attempt > 0:
    user_input = int(input("Make a guess: \t"))
    is_correct, message = guess_number(user_input)
    print(message)
    if is_correct:
        break
