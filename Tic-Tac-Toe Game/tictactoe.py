import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = "X"
        self.game_active = True
        self.board = [""] * 9
        self.game_mode = None  # Player-vs-player or player-vs-computer

        # Use a frame for better organization and resizing
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.menu_buttons_frame = tk.Frame(self.main_frame)
        self.menu_buttons_frame.grid(row=0, column=0, sticky="nsew")

        self.game_board_frame = tk.Frame(self.main_frame)

        # Configure grid weights for responsiveness
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Create Menu Buttons with grid weights
        play_player_button = tk.Button(self.menu_buttons_frame, text="Play against Player", font=("Arial", 16), command=lambda: self.start_game("player"))
        play_player_button.grid(row=0, column=0, sticky="nsew")
        play_computer_button = tk.Button(self.menu_buttons_frame, text="Play against Computer", font=("Arial", 16), command=lambda: self.start_game("computer"))
        play_computer_button.grid(row=0, column=1, sticky="nsew")

        self.menu_buttons_frame.grid_columnconfigure(0, weight=1)
        self.menu_buttons_frame.grid_columnconfigure(1, weight=1)

        self.buttons = []

        # Create Message Label
        self.message_label = tk.Label(self.game_board_frame, text="", font=("Arial", 20))
        self.message_label.grid(row=3, column=0, columnspan=3, sticky="nsew")

        # Create New Game Button
        new_game_button = tk.Button(self.game_board_frame, text="New Game", font=("Arial", 16), command=self.start_new_game)
        new_game_button.grid(row=4, column=0, columnspan=3, sticky="nsew")

        # Configure grid weights for the game board frame
        for i in range(5):  # 3 rows for buttons, 1 for message, 1 for new game
            self.game_board_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.game_board_frame.grid_columnconfigure(i, weight=1)

    def start_game(self, mode):
        self.game_mode = mode
        self.menu_buttons_frame.grid_forget()
        self.game_board_frame.grid(row=0, column=0, sticky="nsew")
        self.create_board()
        self.message_label.config(text="Player X's Turn")

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.game_board_frame, text="", font=("Arial", 40), width=3, height=1,
                              command=lambda index=i: self.button_click(index))
            # Use sticky to make buttons expand
            button.grid(row=i // 3, column=i % 3, sticky="nsew")
            self.buttons.append(button)

    def button_click(self, index):
        if self.board[index] == "" and self.game_active:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.disable_buttons()
                return
            self.current_player = "O" if self.current_player == "X" else "X"
            self.message_label.config(text=f"Player {self.current_player}'s Turn")

            if self.game_mode == "computer" and self.current_player == "O" and self.game_active:
                self.computer_move()

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ""):
                self.message_label.config(text=f"Player {self.board[condition[0]]} wins!")
                self.game_active = False
                return True

        if "" not in self.board:
            self.message_label.config(text="It's a draw!")
            self.game_active = False
            return True

        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def enable_buttons(self):
        for button in self.buttons:
            button.config(state="normal")

    def start_new_game(self):
        self.current_player = "X"
        self.game_active = True
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        if self.game_mode == "player":
            self.message_label.config(text="Player X's Turn")
        elif self.game_mode == "computer":
            self.message_label.config(text="Player X's Turn")
        self.enable_buttons()

    def computer_move(self):
        if self.game_active:
            best_move = self.find_best_move()
            self.button_click(best_move)

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner_minimax(board):
            if is_maximizing:
                return -1
            else:
                return 1

        if "" not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def check_winner_minimax(self, board):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for condition in win_conditions:
            if (board[condition[0]] == board[condition[1]] == board[condition[2]] != ""):
                return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
