# 🕹️ Tic Tac Toe: Conquer the Grid! 🕹️

A classic game of strategy and skill, now brought to your desktop with a sleek GUI and a challenging AI opponent!

## ✨ Features

*   **Intuitive GUI:** Play on a user-friendly 3x3 grid with a clean and modern interface built using Tkinter.
*   **Two Game Modes:**
    *   **Player vs Player:** Challenge your friends in a local head-to-head match.
    *   **Player vs Computer:** Test your skills against a formidable AI opponent powered by the minimax algorithm.
*   **Intelligent AI:** The computer opponent uses the minimax algorithm to make optimal moves, providing a real challenge even for experienced players.
*   **Clear Game Feedback:** See whose turn it is, who has won, or if the game is a draw with clear text messages.
*   **Easy New Game Setup:**  Start a new game with a single button click.

## 🚀 How to Play

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/LakshayChhabra/tictactoe-python-gui.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd tictactoe-python-gui
    ```
3.  **Run the game:**
    ```bash
    python tictactoe.py
    ```
4.  Choose the desired game mode when prompted with the initial menu.
5.  Take turns placing "X"s and "O"s on the grid by clicking the buttons.
6.  The first player to get three in a row (horizontally, vertically, or diagonally) wins!

## 🛠️ Technologies Used

*   **Python:** The primary programming language.
*   **Tkinter:** For the graphical user interface.
*   **Minimax Algorithm:** Implemented for the AI computer opponent.

## 💡 Behind the Code

The `tictactoe.py` script is structured as follows:

*   **`TicTacToe` Class:** Manages the game logic and GUI.
*   **`button_click(self, index)`:** Handles user clicks and updates the game board.
*   **`check_winner(self)`:** Verifies win conditions and draw scenarios.
*    **`minimax(self, board, depth, is_maximizing)`**: Recursive implementation of the minimax Algorithm.
*    **`find_best_move(self)`:** Calls the minimax function and chooses the best move for computer.
*   **`computer_move(self)`:** Calls the computer's move using best move algorithm.
*   **`start_new_game(self)`:** Resets the game board for a new round.
*   **Game Modes:** Includes both single player (vs computer) and multi player.


## 🙋‍♂️ Let's Connect!

If you have any questions, suggestions, or just want to chat about coding, feel free to reach out:

*   **Email:** lakshaychhabra248@gmail.com
*  **LinkedIn:** [Link to my LinkedIn profile](https://www.linkedin.com/in/lakshay-chhabra-941b08235/)

## ❤️ Show Your Support

If you enjoy this project, consider giving it a star ⭐! It helps to keep me motivated to create more awesome things.

Happy Gaming! 🎉
