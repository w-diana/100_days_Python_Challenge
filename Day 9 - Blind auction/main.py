from replit import clear
from art import logo

def add_bid(name, bid, bidders):
  bidders[name] = bid

def find_highest_bidder(bidders):
  max = 0 
  for bidder in bidders:
    if bidders[bidder] > max:
      max_bid = bidders[bidder]
      max_bidder = bidder
  print(f"The winner is {max_bidder} with a bid of ${max_bid}")

print(logo)
print("Welcome to the secret auction program. ")

more_bidders = "yes"
bidders = {}

while more_bidders == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  add_bid(name, bid, bidders)
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if more_bidders == "yes": 
    clear()
  else:
    find_highest_bidder(bidders)
