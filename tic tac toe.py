import math

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def evaluate_board(board):
    if check_win(board, "X"):
        return 10
    if check_win(board, "O"):
        return -10
    return 0

def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate_board(board)
    
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, alpha, beta, False))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, alpha, beta, True))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    board = initialize_board()
    while True:
        print_board(board)
        
        if check_win(board, "O"):
            print("You win!")
            break
        
        if is_board_full(board):
            print("It's a tie!")
            break
        
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == " ":
                board[row][col] = "O"
            else:
                print("Cell already taken. Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")
            continue
        
        if check_win(board, "O"):
            print_board(board)
            print("You win!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
       
        row, col = find_best_move(board)
        board[row][col] = "X"
        print(f"AI chooses ({row}, {col})")

        if check_win(board, "X"):
            print_board(board)
            print("AI wins!")
            break

if __name__ == "__main__":
   play_game()