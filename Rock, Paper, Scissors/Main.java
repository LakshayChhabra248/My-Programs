import java.util.Random;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Exercise - 2 Solution
        // Rock, Paper, Scissors in Java

        // Creating a computer choice
        String compOption = "rps";
        Random randomOpt = new Random();

        int index = randomOpt.nextInt(compOption.length());
        // The Computer chosen letter
        char compChoice = compOption.charAt(index);
        String compChoose = "";
        switch (compChoice) {
            case 'r':
                compChoose = "Rock";
                break;
                
            case 'p':
                compChoose = "Paper";
                break;
                
            case 's':
                compChoose = "Scissors";
                break;
               
        
            default:
                System.out.print("Wrong Input!!");
                
        }

        // First lets take the input from the user 
        Scanner sc = new Scanner(System.in);
        String youChoose = "";
        System.out.println("Enter \nr. For Rock\np. For Paper\ns. For Scissors");
        String input = sc.next();
        input = input.toLowerCase();
        if (input.length() > 1){
            System.out.println("Wrong Input!!");
            
        }
        else{
            char userChoice = input.charAt(0);
            switch (userChoice) {
                case 'r':
                    youChoose = "Rock";
                    break;
                case 'p':
                    youChoose = "Paper";
                    break;
                case 's':
                    youChoose = "Scissors";
                    break;
            
                default:
                    System.out.print("Wrong Input!!");
                    break;
            }
            // Writing both Choices
            System.out.printf("You Choose: %s\n", youChoose);
            System.out.printf("Computer Choose: %s\n", compChoose);
    
            // Now checking the Condition for winning
            if (userChoice == compChoice) {
                System.out.println("The Game is tie");
            }
            else if ((userChoice == 'r' && compChoice == 's') || (userChoice == 'p' && compChoice == 'r') || (userChoice == 's' && compChoice == 'p')) {
                System.out.println("You Win the game");
            }
            else{
                System.out.println("You Lose the Game");
            }
        }

        

        sc.close();
    }
}
