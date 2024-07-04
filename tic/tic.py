import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the game board
board = [" " for _ in range(9)]

# Player symbols
player = "X"
ai = "O"

# Button list to access buttons easily
buttons = []

def check_winner(board, symbol):
    # Check rows, columns and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

def check_tie(board):
    return " " not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, ai):
        return 1
    if check_winner(board, player):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = ai
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move():
    best_score = float('-inf')
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def on_click(index):
    if board[index] == " ":
        board[index] = player
        buttons[index].config(text=player, state="disabled", bg="lightblue")
        if check_winner(board, player):
            messagebox.showinfo("Game Over", "Player wins!")
            root.quit()
        elif check_tie(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()
        else:
            ai_index = best_move()
            board[ai_index] = ai
            buttons[ai_index].config(text=ai, state="disabled", bg="lightcoral")
            if check_winner(board, ai):
                messagebox.showinfo("Game Over", "AI wins!")
                root.quit()
            elif check_tie(board):
                messagebox.showinfo("Game Over", "It's a tie!")
                root.quit()

# Create buttons for the board
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: on_click(i), bg="lightgrey")
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
