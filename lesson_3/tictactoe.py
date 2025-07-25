import os
import random

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
CENTER_SQUARE = 5
WINNING_MARKER_COUNT = 3
MATCH_POINT = 5

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
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

def display_move_order(player):
    prompt(f"{player.capitalize()} will make the first move.")
    wait_for_input()

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def board_full(board):
    return len(empty_squares(board)) == 0

def determine_winner(board):
    for line in WINNING_LINES:
        markers = [board[square] for square in line]

        if markers.count(PLAYER_MARKER) == WINNING_MARKER_COUNT:
            return "player"
        if markers.count(COMPUTER_MARKER) == WINNING_MARKER_COUNT:
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

def alternate_player(player):
    return 'computer' if player == 'player' else 'player'

def get_starting_player():
    clear_screen()
    prompt("Choose who gets the first move ((p)layer, (c)omputer, (r)andom):")
    return input().strip().lower()

def validate_player(start):
    conversion = {'p': 'player', 'c': 'computer', 'r': 'random'}

    while start not in ['player', 'computer', 'random', 'p', 'c', 'r']:
        prompt("Please input a valid choice ((p)layer, (c)omputer, (r)andom): ")
        start = input().strip().lower()

    if len(start) == 1:
        start = conversion[start]

    if start == 'random':
        start = random.choice(['player', 'computer'])

    return start

def choose_square(board, player):
    return player_chooses_square(board) if player == "player" else computer_chooses_square(board)

def choose_random_square(board):
    return random.choice(empty_squares(board))

def choose_center_square(board):
    return CENTER_SQUARE if board[CENTER_SQUARE] == ' ' else None

def computer_chooses_square(board):
    square = find_optimal_square(board)
    board[square] = COMPUTER_MARKER

def find_at_risk_square(board, line, marker):
    marker_line = [board[num] for num in line]

    if marker_line.count(marker) == 2 and marker_line.count(INITIAL_MARKER) == 1:
        return line[marker_line.index(INITIAL_MARKER)]

    return None

def find_optimal_square(board):
    for marker in (COMPUTER_MARKER, PLAYER_MARKER):
        for line in WINNING_LINES:
            square = find_at_risk_square(board, line, marker)
            if square:
                return square

    square = choose_center_square(board)
    if square:
        return square

    return choose_random_square(board)

def player_chooses_square(board):
    valid_choices = [str(num) for num in empty_squares(board)]

    while True:
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
            current_player = validate_player(get_starting_player())
            display_move_order(current_player)
            board = initialize_board()

            while True:
                display_board(board)
                choose_square(board, current_player)
                current_player = alternate_player(current_player)
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
