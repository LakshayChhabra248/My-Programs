// Importing Some essential liabraries
import java.util.Scanner;
import java.util.Random;

class Game {
    // Declaring some Required Variable

    // For Computer Number
    private int compNum;
    // For User Number
    private int userNum;
    // For Number of Guesses
    private int noOfGuesses;

    // Scanner Object
    private Scanner sc = new Scanner(System.in);

    // Random Object
    Random rd = new Random();

    // Method 1 = Generate Random Number
    public void genRandNum() {
        compNum = rd.nextInt(100) + 1;
    }

    // Method 2 = Take User Input
    public void takeUserInput(String message) {
        System.out.print(message);
        userNum = sc.nextInt();

    }

    // Method 3 = Main Game Logic
    public void isCorrectNumber() {

        // To play with multiple players
        System.out.print("Number of Players: ");
        int noOfPlayer = sc.nextInt();

        // Array to Store Scores and Names
        int [] scoreArray = new int[noOfPlayer];
        String [] nameArray = new String[noOfPlayer];

        // Loop to Play with Multiple Players
        for (int index = 0; index < noOfPlayer; index++) {
            noOfGuesses = 0;
            // Clearing Buffer
            sc.nextLine();

            // Taking Name of Player
            System.out.printf("Name of Player %d: ", index + 1);
            String name = sc.nextLine();

            // Main Game Logic
            boolean gusessed = false;
            genRandNum();

            // Using Method 2 to Take User Input
            takeUserInput(name + " Enter a Number (0 - 100): ");

            // Main Game Loop
            while (!gusessed) {
                if (userNum == compNum) {
                    System.out.println("You gusessed it Right");
                    noOfGuesses += 1;
                    gusessed = true;
                } else if (userNum < compNum) {
                    System.out.println("Guess A Higher Number");
                    noOfGuesses += 1;
                    takeUserInput("Enter Again: ");

                } else if (userNum > compNum) {
                    System.out.println("Guess A Lower Number");
                    noOfGuesses += 1;
                    takeUserInput("Enter Again: ");
                }
            }

            // Storing Score and Name
            scoreArray[index] = getResult();
            nameArray[index] = name;
        }

        // Displaying Scores
        for (int index = 0; index < noOfPlayer; index++)
        {
             System.out.printf("%s : %d\n", nameArray[index], scoreArray[index]);
        }

        // Finding Winner
        int minScore = scoreArray[0];
        String winner = nameArray[0];
        for (int index = 1; index < noOfPlayer; index++)
        {
            if (scoreArray[index] < minScore)
            {
                minScore = scoreArray[index];
                winner = nameArray[index];
            }
        }

        // Displaying Winner
        System.out.printf("Winner is %s with %d Guesses\n", winner, minScore);
    }

    // Method 4 = Get Result
    public int getResult() {
        return noOfGuesses;
    }
}

public class Main {
    public static void main(String[] args) {
     
        // Printing Welcome Message
        System.out.print("Lets Start A Game\n");

        // Creating Object of Game Class
        Game numGame = new Game();
        // Starting Game
        numGame.isCorrectNumber();
    }
}
