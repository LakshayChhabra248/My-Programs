# Welcome to rock, paper, scissors game

# importing required modules
import random as rd

def chk_winner(user_option):
    
    """
    This function determines the winner of a single round of Rock, Paper, Scissors.

    Args:
        user_option (str): The user's choice ('r', 'p', or 's').

    Returns:
        int: 1 if the user wins, -1 if the computer wins, 0 if it's a tie.
    """


    option_means = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    options = ['r', 'p', 's']
    win_matrix = [[0, -1, 1], 
                  [1, 0, -1],
                  [-1, 1, 0]]
    
    comp_option = rd.choice(options)
    
    print("Your choice: ", option_means[user_option])    
    print("Computer's choice: ", option_means[comp_option])
    # Lets check the winner

    answer = win_matrix[options.index(user_option)][options.index(comp_option)]
    if answer == 0:
        print("It's a tie")
        
    elif answer == 1:
        print("You win")

    else:
        print("You lose")
    return answer


# Welcome message
print("Let's Play Rock, Paper and Scissors")

# Lets make the logic for the hi-score in the game

# Opening File for Hi-score printing in starting
with open("Hi-Score.txt", 'r') as file:

    # Printing the previous high score
    data = file.readline()
    hi_score = int(data.split(':')[1].strip())
    user_hi = data.split(':')[0].strip()

    print("Previous High Score: ", hi_score)
    print("Holder: ", user_hi)

# defining initial variables
user_name = input("Enter your name: ")
end = False
score = 0

# Loop to play the game
while not end:
    # Try block to handle exceptions
    try:
        # Getting user input
        user_option = (input("Enter your choice(r/p/s or q to quit): ")).lower()
        # Quitting the game
        if user_option == 'q':
            end = True
            break
        a = chk_winner(user_option)
        # Incremeting score based on the result
        if a == 1:
            score += 10
        elif a == -1:
            score -= 5
        
    # Handling exceptions
    except ValueError and KeyError:
        print("Invalid input")
    except KeyboardInterrupt:
        
        break
# End of the game
if score > hi_score:
    with open("Hi-Score.txt", 'w') as file:
        s_text = f"{user_name} : {score}"
        file.write(s_text)
        print("Congratulations! New high score recorded.")
    print("Score: ", score)
else:
    print("Score: ", score)
print("\nThanks for playing")