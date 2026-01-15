def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    print("Welcome to Tic-Tac-Toe!")
    print("Instructions: The game is played on a 3x3 grid.")
    print("Players take turns placing their mark (X or O) in an empty cell.")
    print("To make a move, enter the row number and the column number separated by a space.")
    print("Rows and columns are numbered 1, 2, and 3.")
    print("The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")
    print("When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    print("-" * 30)
    print_board(board)

    while True:
        player = players[turn % 2]
        try:
            move = input(f"Player {player}, enter row and column (1-3) separated by space: ")
            r_input, c_input = map(int, move.split())
            r, c = r_input - 1, c_input - 1
            if not (0 <= r <= 2 and 0 <= c <= 2):
                 raise IndexError("Coordinates out of range")
            if board[r][c] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 1 and 3.")
            continue

        board[r][c] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        
        if is_full(board):
            print("It's a draw!")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
