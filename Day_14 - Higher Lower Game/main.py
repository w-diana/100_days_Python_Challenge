from art import logo, vs
from game_data import data
import replit
from random import randint

def Clear_screen():
  replit.clear()
  print(logo)

def Compare(guess, option_1, option_2, game_progress):
  option_1 = game_progress["winner"]
  score = game_progress["score"]

  if guess=="a" and data[option_1]["follower_count"] > data[option_2]["follower_count"] or guess=="b" and data[option_2]["follower_count"] > data[option_1]["follower_count"]:
    score += 1
    Clear_screen()
    print(f"You're right! Current score: {score}.")
    if guess == "a":
      game_progress = update_values(game_progress, False, score, option_1, option_2)
    else:
      game_progress = update_values(game_progress, False, score, option_2, option_1)
    return game_progress
    
  else:
    Clear_screen()
    print(f"Sorry, that's wrong. Final score: {score}")
    print(f'{data[option_1]["name"]} has {data[option_1]["follower_count"]} followers while {data[option_2]["name"]} has {data[option_2]["follower_count"]} followers') 
    if guess == "a":
      game_progress = update_values(game_progress, True, score, option_2, option_1)
    else:
      game_progress = update_values(game_progress, True, score, option_1, option_2)
    return game_progress

def update_values(game_progress, game_ended, score, winner, index_to_pop):
  game_progress["score"] = score
  game_progress["winner"] = winner
  game_progress["game_data"].pop(index_to_pop)
  if len(game_progress["game_data"]) == 1:
    game_progress["game_ended"] = True
    Clear_screen()
    print("Game ended! We are out of celebrities")
    print(f"You Won! Final score: {score}")
  else:
    game_progress["game_ended"] = game_ended
  return game_progress

# Declaring game variables
A = "A"
B = "B"
incorrect_input = True
game_progress = {
  "game_ended": False,
  "winner": randint(0,len(data)-1),
  "score": 0,
  "game_data": data
}

# Start game
print(logo)
while not game_progress["game_ended"]: 
  winner = game_progress["winner"]
  option_2 = randint(0,len(game_progress["game_data"])-1)
  while winner == option_2:
    option_2 = randint(0,len(game_progress["game_data"])-1)
  
  print(f'Compare {A}: {data[winner]["name"]}, a {data[winner]["description"]}, from {data[winner]["country"]}. ')
  print(vs)
  print(f'Length: {len(game_progress["game_data"])}, option_1: {winner},  option 2: {option_2} ')
  print(f'Against {B}: {data[option_2]["name"]}, a {data[option_2]["description"]}, from {data[option_2]["country"]}. ')
  guess = input("Who has more followers? Type 'A' or 'B' ").lower()
  game_progress = Compare(guess, winner, option_2, game_progress)





#######################     VERSION 2      #################################
# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()