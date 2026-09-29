import random

# Score tracking
user_score = 0
computer_score = 0
ties = 0

print("=" * 40)
print("     ROCK, PAPER, SCISSORS GAME")
print("=" * 40)

while True:

    # User input
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (1/2/3): ")

    # Convert number to choice
    if user_choice == "1":
        user = "rock"
    elif user_choice == "2":
        user = "paper"
    elif user_choice == "3":
        user = "scissors"
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
        continue

    # Computer selection
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    # Display choices
    print("\nYour choice     :", user)
    print("Computer choice :", computer)

    # Game logic
    if user == computer:
        print("Result: It's a TIE!")
        ties += 1

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("Result: YOU WIN!")
        user_score += 1

    else:
        print("Result: COMPUTER WINS!")
        computer_score += 1

    # Display score
    print("\n----- SCORE -----")
    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)
    print("Ties           :", ties)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

# Final result
print("\n" + "=" * 40)
print("           FINAL SCORE")
print("=" * 40)

print("Your Score     :", user_score)
print("Computer Score :", computer_score)
print("Ties           :", ties)

print("\nThanks for playing!")