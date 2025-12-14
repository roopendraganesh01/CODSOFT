# Tic-Tac-Toe AI using Minimax Algorithm
# CodSoft Artificial Intelligence Internship - Task 2

import math

PLAYER = 'X'
AI = 'O'
EMPTY = ' '

board = [EMPTY] * 9

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def is_winner(player):
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_draw():
    return EMPTY not in board

def minimax(is_maximizing):
    if is_winner(AI):
        return 1
    if is_winner(PLAYER):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                score = minimax(True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    board[move] = AI

def player_move():
    move = int(input("Enter position (1-9): ")) - 1
    if board[move] == EMPTY:
        board[move] = PLAYER
    else:
        print("Invalid move. Try again.")
        player_move()

def game():
    print("Tic-Tac-Toe AI (You = X, AI = O)")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner(PLAYER):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move()
        print("AI played:")
        print_board()
        if is_winner(AI):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    game()
