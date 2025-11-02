Program(Tic-Tac-Toe with Minimax):-
import math

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

# Check winner
def check_winner(board):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # cols
        [0,4,8], [2,4,6]             # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = [" "] * 9
    print("You are X. Computer is O.")
    print_board(board)

    while True:
        # Player move
        move = int(input("Enter your move (0-8): "))
        if board[move] == " ":
            board[move] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)
        if check_winner(board):
            break

        # Computer move
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("Computer places O at position", ai_move)
        print_board(board)

        if check_winner(board):
            break

    winner = check_winner(board)
    if winner == "Draw":
        print("It's a Draw!")
    else:
        print("Winner is:", winner)

# Run the game
play_game()
Output:
You are X. Computer is O.
|   |   |   |
|   |   |   |
|   |   |   |

Enter your move (0-8): 0
| X |   |   |
|   |   |   |
|   |   |   |

Computer places O at position 4
| X |   |   |
|   | O |   |
|   |   |   |

...
Winner is: O
