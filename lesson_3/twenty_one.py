# refactor main loop if you can
# pylint this shit

import random
import os

MATCH_POINT = 5
FACE_VALUE = 10
ACE_VALUE = 11
DEALER_STAY = 17
TWENTY_ONE = 21
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♠', '♣', '♥', '♦']

def prompt(msg):
    print(f"==> {msg}")

def clear_screen():
    os.system("clear")

def wait_for_input():
    print("")
    input("Press enter to continue:")

def ask_play_again():
    clear_screen()
    prompt("Would you like to play again? (y/n)")

def display_greeting():
    clear_screen()
    prompt("Welcome to Twenty One. Good luck on the virtual tables!")
    wait_for_input()

def display_goodbye():
    prompt("Thanks for playing Twenty One!")

def display_underline():
    prompt("--------------------------------")

def initialize_deck():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append([rank, suit])

    return deck

def calculate_total(hand):
    face_cards = ('J', 'Q', 'K')
    ranks = extract_ranks(hand)
    total = 0

    for rank in ranks:
        if rank in face_cards:
            total += FACE_VALUE
        elif rank == "A":
            total += ACE_VALUE
        else:
            total += int(rank)

    if "A" in ranks and total > TWENTY_ONE:
        total -= FACE_VALUE

    return total

def display_all_hands(dealer, player):
    clear_screen()
    prompt(f"Dealer: {join_cards(dealer)}")
    prompt(f"Player: {join_cards(player)}")
    display_underline()

def shuffle(deck):
    random.shuffle(deck)

def reset_hands(dealer, player):
    dealer.clear()
    player.clear()

def reset_score(score):
    for player in score:
        score[player] = 0

def busted(hand):
    return calculate_total(hand) > TWENTY_ONE

def deal_starting_cards(deck, dealer, player):
    deal_one_card(deck, dealer)
    deal_two_cards(deck, player)

def deal_one_card(deck, hand):
    hand.append(deck.pop())

def deal_two_cards(deck, hand):
    for _ in range(2):
        hand.append(deck.pop())

def display_total(dealer, player):
    if len(dealer) == 1:
        prompt("Dealer's total is ?")
    else:
        prompt(f"Dealer's total is {calculate_total(dealer)}.")

    prompt(f"Player's total is {calculate_total(player)}.")
    display_underline()

def extract_ranks(hand):
    return [rank for rank, _ in hand]

def join_cards(hand):
    if len(hand) == 1:
        return f"{''.join(hand[0])}, ?"

    return ", ".join([rank + suit for rank, suit in hand])

def retrieve_yes_or_no():
    answer = input().strip().lower()

    while not valid_yes_or_no(answer):
        prompt("Please input a valid answer (y/n)")
        answer = input().strip().lower()

    clear_screen()
    return (answer in ['y', 'yes'])

def valid_yes_or_no(answer):
    return answer in ['y', 'yes', 'n', 'no']

def retrieve_hit_or_stay():
    prompt("Would you like to (h)it or (s)tay?")
    return input().strip().lower()

def validate_decision(action):
    conversion = {'h': 'hit', 's': 'stay'}

    while action not in ['hit', 'stay', 'h', 's']:
        prompt("Please input a valid decision ((h)it or (s)tay):")
        action = input().strip().lower()

    if len(action) == 1:
        action = conversion[action]

    return action

def determine_winner(dealer, player):
    dealer_total = calculate_total(dealer)
    player_total = calculate_total(player)

    if dealer_total > player_total:
        return "dealer"
    if player_total > dealer_total:
        return "player"

    return "tie"

def display_winner(winner):
    if winner == "player":
        prompt("Player wins!")
    elif winner == "dealer":
        prompt("Dealer wins!")
    else:
        prompt("It's a tie!")

def display_score(score):
    player_score = score["player"]
    dealer_score = score["dealer"]

    if player_score == MATCH_POINT:
        prompt(f"Player wins the match {player_score}:{dealer_score}!")
    elif dealer_score == MATCH_POINT:
        prompt(f"Dealer wins the match {dealer_score}:{player_score}!")
    elif player_score > dealer_score:
        prompt(f"Player is leading {player_score}:{dealer_score}")
    elif dealer_score > player_score:
        prompt(f"Dealer is leading {dealer_score}:{player_score}")
    else:
        prompt(f"It is currently tied {player_score}:{dealer_score}")

def update_score(score, winner):
    if winner in score.keys():
        score[winner] += 1

def play_twenty_one():
    player_hand = []
    dealer_hand = []
    score = {'player': 0, 'dealer': 0}
    display_greeting()

    while True:
        reset_score(score)
        while True:
            deck = initialize_deck()
            shuffle(deck)
            reset_hands(dealer_hand, player_hand)
            deal_starting_cards(deck, dealer_hand, player_hand)

            while True:
                display_all_hands(dealer_hand, player_hand)
                display_total(dealer_hand, player_hand)
                action = validate_decision(retrieve_hit_or_stay())

                if action == "hit":
                    deal_one_card(deck, player_hand)

                if action == "stay" or busted(player_hand):
                    break

            display_all_hands(dealer_hand, player_hand)
            display_total(dealer_hand, player_hand)

            if busted(player_hand):
                prompt("Player busts. Dealer wins!")
                update_score(score, 'dealer')
                display_score(score)
                wait_for_input()
                continue

            prompt("Player chose to stay!")
            wait_for_input()

            deal_one_card(deck, dealer_hand)
            while True:
                display_all_hands(dealer_hand, player_hand)
                display_total(dealer_hand, player_hand)

                if calculate_total(dealer_hand) < DEALER_STAY:
                    prompt("Dealer hits.")
                    deal_one_card(deck, dealer_hand)
                    wait_for_input()

                if calculate_total(dealer_hand) >= DEALER_STAY or busted(dealer_hand):
                    break

            display_all_hands(dealer_hand, player_hand)
            display_total(dealer_hand, player_hand)

            if busted(dealer_hand):
                prompt("Dealer busts. Player wins!")
                update_score(score, "player")
                display_score(score)
            else:
                winner = determine_winner(dealer_hand, player_hand)
                display_winner(winner)
                update_score(score, winner)
                display_score(score)
            wait_for_input()

            if max(score.values()) == MATCH_POINT:
                break

        ask_play_again()
        play_again = retrieve_yes_or_no()

        if not play_again:
            break

    display_goodbye()

play_twenty_one()