#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(0,101)
choice = input("Choose a difficulty. Type 'easy or 'hard': ")
game = True

if choice == 'easy':
  attempts = 10
  while game is True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    if attempts > 0:
      guess = int(input("Make a guess: "))
      if guess > number:
        print("Too high.")
        attempts -= 1
        print("Guess again.")
      elif guess < number:
        print("Too low.")
        attempts -= 1
        print("Guess again.")
      else:
        print("You've guess the number!")
        game = False
    elif attempts == 0:
      print(f"You have no more attempt, You Lose! The number is {number}")
      game = False  


elif choice == 'hard':
  attempts = 5
  while game is True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    
    if attempts > 0:
      guess = int(input("Make a guess: "))
      if guess > number:
        print("Too high.")
        attempts -= 1
        print("Guess again.")
      elif guess < number:
        print("Too low.")
        attempts -= 1
        print("Guess again.")
      else:
        print("You've guess the number!")
        game = False
    elif attempts == 0:
      print(f"You have no more attempt, You Lose! The number is {number}")
      game = False  