import tkinter as tk
from tkinter import messagebox

# Constants for the game
PLAYER = 'X'
AI = 'O'
EMPTY = None

# Function to evaluate the board (Minimax)
def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return 10 if row[0] == AI else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return 10 if board[0][col] == AI else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return 10 if board[0][0] == AI else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return 10 if board[0][2] == AI else -10
    return 0

# Minimax function
def minimax(board, depth, is_max_turn):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not any(EMPTY in row for row in board):
        return 0

    if is_max_turn:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, not is_max_turn))
                    board[i][j] = EMPTY
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = min(best, minimax(board, depth + 1, not is_max_turn))
                    board[i][j] = EMPTY
        return best

# Function to find the best move for AI
def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Function to check for a winner or draw
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    # Check for draw (if all cells are filled)
    if all(cell != EMPTY for row in board for cell in row):
        return 'DRAW'

    return None

# Class for the Tic-Tac-Toe Game with Tkinter GUI
class TicTacToe:
    def __init__(self, root):
        self.board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
        self.current_player = PLAYER
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.root = root
        self.create_widgets()
    
    def create_widgets(self):
        self.root.config(bg='#333333')  # Dark background color for window
        self.header = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 24, 'bold'), bg='#333333', fg='white')
        self.header.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, 
                                               text='', 
                                               font=('Arial', 40, 'bold'), 
                                               height=3, 
                                               width=6,  # Larger button size
                                               bg='#666666',  # Dark button background
                                               fg='#FFFFFF',  # White text for empty cells
                                               relief='solid', 
                                               activebackground='#888888', 
                                               command=lambda i=i, j=j: self.player_move(i, j))
                self.buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)
        
        self.status_label = tk.Label(self.root, text="Your Turn!", font=('Arial', 14), bg='#333333', fg='white')
        self.status_label.grid(row=4, column=0, columnspan=3, pady=10)

    def player_move(self, i, j):
        if self.board[i][j] == EMPTY:
            self.board[i][j] = PLAYER
            self.buttons[i][j].config(text=PLAYER, fg='#003366')  
            winner = check_winner(self.board)
            if winner:
                self.game_over(winner)
            elif any(EMPTY in row for row in self.board):
                self.ai_move()

    def ai_move(self):
        best_move = find_best_move(self.board)
        i, j = best_move
        self.board[i][j] = AI
        self.buttons[i][j].config(text=AI, fg='#00ff99')  
        winner = check_winner(self.board)
        if winner:
            self.game_over(winner)

    def game_over(self, winner):
        if winner == 'DRAW':
            messagebox.showinfo("Game Over", "It's a draw!")
        elif winner == AI:
            messagebox.showinfo("Game Over", "AI wins!")
        else:
            messagebox.showinfo("Game Over", "Player wins!")
        self.reset_game()

    def reset_game(self):
        self.board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', fg='white')  # Reset text and color

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe - Battle of Wits")

# Create the game instance
game = TicTacToe(root)

# Start the main loop
root.mainloop()

