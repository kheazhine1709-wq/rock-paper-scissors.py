import random

CHOICES = ["rock", "paper", "scissors"]

# what beats what: key beats value
BEATS = {
  "rock": "scissors",
  "paper": "rock",
  "scissors": "paper",
}

def get_user_choice():
    while True:
        choice = input("choose rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
        if choice == "quit":
            return None
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please try again")
  
def get_computer_choice():
    return random.choice(CHOICES)

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif BEATS[user] == computer:
        return "user"
    else:
        return "computer"

def play():
    print("=== Rock, Paper, Scissors ===")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            break

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's s tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

   print("\nFinal Score.")
   print(f"You: {user_score} | Computer: {computer_score}")
   if user_score > computer_score:
       print("Congratulations, You won the game!")
   elif user_score < computer_score:
       print("Computer won the game! Better luck next time")
   else:
       print("It's a tie!")

if __name__ == "__main__":
    play()
