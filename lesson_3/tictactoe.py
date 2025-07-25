import os
import random

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_MARKER_COUNT = 3
MATCH_POINT = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7]  # diagonal
    ]

def prompt(message):
    print(f'===> {message}')

def clear_screen():
    os.system('clear')

def wait_for_input():
    input("Press any key to continue:")

def ask_play_again():
    clear_screen()
    prompt("Would you like to play again? (y/n)")

def display_board(board):
    clear_screen()
    
    prompt(f"You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print()

def display_greeting():
    clear_screen()
    prompt(f"Welcome to Tic Tac Toe. First to {MATCH_POINT} wins. Good luck!")
    wait_for_input()

def display_goodbye():
    prompt("Thanks for playing Tic Tac Toe!")

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def board_full(board):
    return len(empty_squares(board)) == 0

def determine_winner(board):
    for line in WINNING_LINES:
        marker_line = [board[num] for num in line]
        if marker_line.count(PLAYER_MARKER) == WINNING_MARKER_COUNT:
            return "player"
        if marker_line.count(COMPUTER_MARKER) == WINNING_MARKER_COUNT:
            return "computer"
        
    return None

def display_results(winner, score):
    prompt(f"{winner.capitalize()} wins!") if winner else prompt("It's a tie!")
    prompt(f"The score is Player: {score["player"]} - Computer: {score["computer"]}")
    wait_for_input()

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(lst, delimiter = ", ", prepend_word = "or"):
    new_lst = [str(el) for el in lst]
    
    match len(new_lst):
        case 0:
            return ""
        case 1:
            return new_lst[0]
        case 2:
            return f"{new_lst[0]} {prepend_word} {new_lst[1]}"

    new_lst[-1] = f"{prepend_word} {new_lst[-1]}"
    return delimiter.join(new_lst)

def computer_chooses_square(board):
    square = find_optimal_square(board) or random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def find_optimal_square(board):
    square = None
    
    for line in WINNING_LINES:
        marker_line = [board[num] for num in line]
        
        if marker_line.count(COMPUTER_MARKER) == 2 and marker_line.count(INITIAL_MARKER) == 1:
            square = line[marker_line.index(INITIAL_MARKER)]

        if marker_line.count(PLAYER_MARKER) == 2 and marker_line.count(INITIAL_MARKER) == 1:
            square = line[marker_line.index(INITIAL_MARKER)]

    return square


def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = PLAYER_MARKER

def update_score(winner, score):
    if winner:
        score[winner] += 1

def winner_detected(board):
    return bool(determine_winner(board))

def end_of_game(board):
    return winner_detected(board) or board_full(board)

def end_of_match(score):
    return max(score.values()) == MATCH_POINT

def retrieve_yes_or_no():
    answer = input().strip().lower()

    while not valid_yes_or_no(answer):
        prompt("Please input a valid answer (y/n)")
        answer = input().strip().lower()

    clear_screen()
    return (answer in ['y', 'yes'])

def valid_yes_or_no(answer):
    return answer in ['y', 'yes', 'n', 'no']

def play_tic_tac_toe():
    display_greeting()

    while True:
        score = {'player': 0, 'computer': 0}
        while True:
            board = initialize_board()

            while True:
                display_board(board)

                player_chooses_square(board)
                if end_of_game(board): break

                computer_chooses_square(board)
                if end_of_game(board): break
            
            winner = determine_winner(board)
            update_score(winner, score)
            display_board(board)
            display_results(winner, score)

            if end_of_match(score): break
        
        ask_play_again()
        play_again = retrieve_yes_or_no()

        if not play_again:
            break
    
    display_goodbye()

play_tic_tac_toe()