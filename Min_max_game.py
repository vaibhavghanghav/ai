def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("|".join(row))
    print()

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def minimax(board, is_maximizing):
    if check_winner(board, 'O'): return 1  # AI wins
    if check_winner(board, 'X'): return -1  # Human wins
    if ' ' not in board: return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_score = max(best_score, minimax(board, False))
                board[i] = ' '
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_score = min(best_score, minimax(board, True))
                board[i] = ' '
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human move
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] == ' ':
            board[human_move] = 'X'
        else:
            print("Invalid move, try again.")
            continue

        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break

play_game()
