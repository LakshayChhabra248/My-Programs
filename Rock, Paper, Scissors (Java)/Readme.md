# Rock, Paper, Scissors Game in Java 
This document describes the Java code for a Rock, Paper, Scissors game implemented in the ```Main.java``` file.

## Functionality
* The program simulates a Rock, Paper, Scissors game between the user and the computer. 
* The computer randomly chooses rock, paper, or scissors, and the user enters their choice through the console. 
* The program then compares the choices and declares the winner (user, computer, or tie) based on the classic Rock-Paper-Scissors rules.

## Code Breakdown
The code is divided into several sections:

1.  Computer Choice:

    * Creates a string compOption containing "rps" (representing rock, paper, scissors).
    * Uses Random to generate an index within the length of compOption.
    * Extracts the character at the generated index using charAt().
    * Uses a switch statement to convert the character to a human-readable choice string (rock, paper, or scissors) and stores it in compChoose.
2. User Input:

    * Creates a Scanner object to read user input.
    * Prompts the user to enter "r" for rock, "p" for paper, or "s" for scissors.
    * Reads user input using next().
    * Converts the input to lowercase to handle case-insensitive input.
    * Checks if the input length is greater than 1 (indicating invalid input) and prints an error message if true.
    * Otherwise, extracts the first character of the input and uses a switch statement to convert it to a human-readable choice string (rock, paper, or scissors) and stores it in youChoose.
3. Displaying Choices:

    * Prints both the user's and computer's choices using formatted strings (printf).
4. Determining the Winner:

    * Uses an if statement to check for a tie (both choices are the same character).
    * Otherwise, uses an else-if statement with nested conditions to determine the winner based on the classic Rock-Paper-Scissors rules.
    * Prints a message declaring the winner \
    ```("The Game is tie", "You Win the game", or "You Lose the Game")```
5. Closing Scanner:

    * Closes the Scanner object to release resources.
    * Running the Code
    * Save the code as ```Main.java```.
    * Compile the code using a Java compiler 
    * Run the compiled class using Java runtime 
    * Follow the prompts to enter your choice (r, p, or s).
    * The program will announce the winner (you, computer, or tie).
* This code provides a basic example of a Rock, Paper, Scissors game in Java. You can extend it further by adding features like multiple rounds, scorekeeping, or a graphical interface.