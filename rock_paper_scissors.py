import random 

def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice 
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"
    
def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        print("\nNew Round!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou choose: {user_choice.capitalize()}")
        print(f"Computer chooses: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScore => You: {user_score}, Computer: {computer_score}")

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

    print("\nThanks for playing!")
    print(f"Final Score => You: {user_score}, Computer: {computer_score}")
    print("Goodbye!")

play_game()

