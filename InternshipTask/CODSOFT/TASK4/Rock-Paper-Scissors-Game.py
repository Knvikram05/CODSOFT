import random;
user_score = 0
computer_score = 0

while True:
    print("Welcome to Rock-Paper-Scissors Game!")
    user_choice = input("Choose: rock, paper, or scissors:")
    computer_choice = random.choice(['rock','paper','scissors'])

    #main game Logic
    if user_choice == computer_choice:
        result = "Its a Tie!!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "you lose!!"
        computer_score += 1


    #result Displaying
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {result}")

    # Display Scores
    print(f"Your score: {user_score} | Computer's score: {computer_score}")

    # Play Again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

print("Thanks for playing!")        