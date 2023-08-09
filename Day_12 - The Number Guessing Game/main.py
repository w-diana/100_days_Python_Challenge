#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

def make_guess():
  guess = int(input("Make a guess: "))
  return guess
  
print(logo)
print("Welcome to the Number Guessing Game!")
computer_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
if difficulty_level == "easy":
  lives_left = 10
elif difficulty_level == "hard":
  lives_left = 5

game_ended = False

while lives_left > 0 and not game_ended:
  print(f"You have {lives_left} attempts remaining to guess the number.")
  guess = make_guess()
  if guess == computer_number:
    print(f"You got it! The answer was {computer_number}.")
    game_ended = True
  else:
    if guess > computer_number:
      lives_left -= 1
      print("Too high.")
    elif guess < computer_number:
      lives_left -= 1
      print("Too low.")

    if lives_left == 0:
      print(f"You've run out of guesses, you lose. The number was {computer_number}")
    else:
      print("Guess again.")