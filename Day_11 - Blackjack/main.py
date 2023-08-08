from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def draw_card(players_hand, deck_cards):
    computers_card = players_hand["computer_hand"]
    players_card = players_hand["your_hand"]

    computers_card.append(random.choice(deck_cards))
    players_card.append(random.choice(deck_cards))
    if len(players_card) < 2:
        players_card.append(random.choice(deck_cards))
        computers_card.append(random.choice(deck_cards))
    print(
        f'Your cards: {players_card}, current score: {calculate_score(players_card)}'
    )
    print(f"Computer's first card: {computers_card[0]}")

    players_hand["computer_hand"] = computers_card
    players_hand["your_hand"] = players_card
    players_hand = check_game(players_hand)
    return players_hand


def check_game(players_hand):
    computers_card = players_hand["computer_hand"]
    players_card = players_hand["your_hand"]

    if black_jack(players_card):
        print_final_card(players_hand)
        print("Win with a Blackjack 😎")
        players_hand["game_ended"] = True
    elif black_jack(computers_card):
        print_final_card(players_hand)
        print("Lose, opponent has Blackjack 😱")
        players_hand["game_ended"] = True
    elif calculate_score(players_card) > 21:
        print_final_card(players_hand)
        print("You went over. You lose 😭")
        players_hand["game_ended"] = True
    elif calculate_score(computers_card) > 21:
        print_final_card(players_hand)
        print("Opponent went over. You win 😁")
        players_hand["game_ended"] = True
    elif calculate_score(players_card) == 21:
        print_final_card(players_hand)
        print("You win 😃")
        players_hand["game_ended"] = True
    elif calculate_score(computers_card) == 21:
        print_final_card(players_hand)
        print("You lose 😤")
        players_hand["game_ended"] = True
    else:
        players_hand["game_ended"] = False

    players_hand["computer_hand"] = computers_card
    players_hand["your_hand"] = players_card
    return players_hand


def calculate_score(cards):
    """"Take a list of cards and return the score calculated from the cards"""
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    #score = 0
    #for card in cards:
       # score = score + card
    return sum(cards)


def black_jack(cards):
    if cards[0] + cards[1] == 21:
        return True
    return False


def end_game(players_hand):
    players_hand = check_game(players_hand)
    if players_hand["game_ended"] == False:
        if calculate_score(players_hand["your_hand"]) > calculate_score(
                players_hand["computer_hand"]):
            print_final_card(players_hand)
            print("You win 😃")
            players_hand["game_ended"] = True
        elif calculate_score(players_hand["your_hand"]) < calculate_score(
                players_hand["computer_hand"]):
            print_final_card(players_hand)
            print("You lose 😤")
            players_hand["game_ended"] = True


def print_final_card(players_hand):
    computers_card = players_hand["computer_hand"]
    players_card = players_hand["your_hand"]

    print(
        f"Your final hand: {players_card}, final score: {calculate_score(players_card)}"
    )
    print(
        f"Computer's final hand: {computers_card}, final score: {calculate_score(computers_card)}"
    )



play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()


while play == "y":
    deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players_hand = {"your_hand": [], "computer_hand": [], "game_ended": False}
    print(logo)
  
    players_hand = draw_card(players_hand, deck_cards)
    while players_hand["game_ended"] == False:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if get_another_card == "y":
            players_hand = draw_card(players_hand, deck_cards)
            if players_hand["game_ended"]:
              get_another_card = "n"
        else:
            while calculate_score(players_hand["computer_hand"]) < 17:
                players_hand["computer_hand"].append(
                    random.choice(deck_cards))
            end_game(players_hand)
    
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()


