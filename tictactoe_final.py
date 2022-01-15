"""
Cameron Barrett
Elder Hunter
W02 Prove: Developer - Solo Code Submission
Tic Tac Toe Assignment
CSE 210
01/12/2021
"""

winner = None
game_running = True
player_pos = {"X":[], "O":[]}
current_player = "X"

def main():
    global game_running
    board = draw_board()
    while game_running:
        display_board(board)
        player_pos = player_turn(current_player, board)
        flip_player()
        if check_for_winner(board) == "X" or check_for_winner(board) == "O":
            game_running = False
        elif check_for_tie(player_pos) == True:
            game_running = False
        else:
            game_running = True
    display_board(board)
    if check_for_winner(board):
        print(f"{winner} Wins!")
    else:
        print("Tie!")
    print("Good game. Thanks for playing!")

def draw_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def display_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}\n")

def player_turn(player, board):
    valid = False
    bad_input = True
    while bad_input:
        try:
            while not valid:
                position = int(input(f"{player}'s turn to choose a square (1-9): "))
                if board[position - 1] != "X" and board[position - 1] != "O":
                    valid = True
                else:
                    print("\nPosition already chosen. Choose a different position.\n")
            board[position - 1] = player
            player_pos[player].append(position)
            bad_input = False
        except:
            print("\nPlease type a number between (1-9)\n")
    return player_pos

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_for_winner(board):
    global winner
    row_winner = check_rows(board)
    column_winner = check_columns(board)
    diagonal_winner = check_diagonals(board)
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return winner

def check_rows(board):
    row_one = board[0] == board[1] == board[2] != type(int)
    row_two = board[3] == board[4] == board[5] != type(int)
    row_three = board[6] == board[7] == board[8] != type(int)
    if row_one:
        return board[0]
    elif row_two:
        return board[3]
    elif row_three:
        return board[6]
    return

def check_columns(board):
    column_one = board[0] == board[3] == board[6] != type(int)
    column_two = board[1] == board[4] == board[7] != type(int)
    column_three = board[2] == board[5] == board[8] != type(int)
    if column_one:
        return board[0]
    elif column_two:
        return board[1]
    elif column_three:
        return board[2]
    return

def check_diagonals(board):
    diagonal_one = board[0] == board[4] == board[8] != type(int)
    diagonal_two = board[6] == board[4] == board[2] != type(int)
    if diagonal_one:
        return board[0]
    elif diagonal_two:
        return board[2]
    return

def check_for_tie(player_pos):
    if len(player_pos["X"]) + len(player_pos["O"]) == 9:
        return True
    return False

if __name__ == "__main__":
    main()
