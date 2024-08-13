# Guess The Number Game
This repository contains the code for a simple number guessing game in Java. Players try to guess a randomly generated number between 1 and 100 within the fewest tries. The game supports multiple players, allowing them to compete for the lowest number of guesses.

## Features:

* Generates a random number between 1 and 100.
* Allows multiple players to participate.
* Tracks the number of guesses for each player.
* Determines the winner with the lowest number of guesses.
* Provides user-friendly prompts and messages.
## Code Structure:

* ### Game Class:
Contains methods for generating random numbers (genRandNum()), taking user input (takeUserInput()), handling the core gameplay loop (isCorrectNumber()), and retrieving the number of guesses (getResult()).
The isCorrectNumber() method manages the logic for multiple players, including getting names, playing individual rounds, storing scores, and finding the winner.
* ### Main Class:
Creates a Game object and starts the game by calling the isCorrectNumber() method.
## How to Play:

1. Clone or download the repository.
2. Open the project in a Java IDE (e.g., Eclipse, IntelliJ IDEA).
3. Run the Main class to start the game.
4. Enter the number of players when prompted.
5. Each player will enter their name and guess the random number.
6. The game will announce the winner with the lowest number of guesses.
## Requirements:

Java Development Kit (JDK)
Further Enhancements:

Implement difficulty levels with different number ranges.
Add a timer to limit guess time for each player.
Improve visual feedback for higher/lower guesses.

# Feel free to contribute or modify this code for further development!
