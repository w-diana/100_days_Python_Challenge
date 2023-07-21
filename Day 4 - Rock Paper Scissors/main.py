import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_strings = ["rock", "paper", "scissors"]
game_drawings = [rock, paper, scissors]
game_options = [game_strings,game_drawings]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
random_no = random.randint(0,2)


computer_choice_str = game_options[0][random_no]
player_choice_str = game_options[0][player_choice]

print(f"{game_options[1][player_choice]}")
print(f"Computer choose: \n{game_options[1][random_no]}")

if computer_choice_str == "rock" and player_choice_str == "rock":
    print("It's a draw")
elif computer_choice_str == "rock" and player_choice_str == "paper":
    print("You Win")
elif computer_choice_str == "rock" and player_choice_str == "scissors":
    print("You loose")
elif computer_choice_str == "paper" and player_choice_str == "rock":
    print("You loose")
elif computer_choice_str == "paper" and player_choice_str == "paper":
    print("It's a draw")
elif computer_choice_str == "paper" and player_choice_str == "scissors":
    print("You Win")
elif computer_choice_str == "scissors" and player_choice_str == "rock":
    print("You Win")
elif computer_choice_str == "scissors" and player_choice_str == "paper":
    print("You loose")
elif computer_choice_str == "scissors" and player_choice_str == "scissors":
    print("It's a draw")
