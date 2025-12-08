# ---- TIC TAC TOE CONSOLE GAME ----

board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

board_keys = list(board.keys())


def print_board(b):
    print()
    print(b['7'] + ' | ' + b['8'] + ' | ' + b['9'])
    print('--+---+--')
    print(b['4'] + ' | ' + b['5'] + ' | ' + b['6'])
    print('--+---+--')
    print(b['1'] + ' | ' + b['2'] + ' | ' + b['3'])
    print()


def check_win(b, mark):
    # rows
    if (b['7'] == b['8'] == b['9'] == mark) or \
       (b['4'] == b['5'] == b['6'] == mark) or \
       (b['1'] == b['2'] == b['3'] == mark) or \
       (b['7'] == b['4'] == b['1'] == mark) or \
       (b['8'] == b['5'] == b['2'] == mark) or \
       (b['9'] == b['6'] == b['3'] == mark) or \
       (b['7'] == b['5'] == b['3'] == mark) or \
       (b['9'] == b['5'] == b['1'] == mark):
        return True
    return False


def game():
    turn = 'X'
    count = 0

    print("Welcome to Tic Tac Toe!")
    print("Positions:")
    print("7 | 8 | 9")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("1 | 2 | 3")
    print()

    for _ in range(9):
        print_board(board)
        print("It is your turn,", turn)
        move = input("Choose a position (1-9): ")

        if move not in board:
            print("Invalid position! Try again.")
            continue

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled. Try again.")
            continue

        # check win
        if count >= 5:
            if check_win(board, turn):
                print_board(board)
                print("*****", turn, "wins! *****")
                break

        # draw
        if count == 9:
            print_board(board)
            print("Game is a draw!")
            break

        # change player
        turn = 'O' if turn == 'X' else 'X'

    print("\nGame over.")


# ---- VERY IMPORTANT: CALL THE GAME ----
if __name__ == "__main__":
    game()
    print("Created By Tasleem Ahmed.")