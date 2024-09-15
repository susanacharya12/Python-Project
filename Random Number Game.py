import random
print("Welcome To Random Number Guessing Game ! ")
from Pythonlogo import logo
print(logo)
def random_guessing_game():
    game_over = False
    # Ask the user to choose a difficulty level
    print("Choose a difficulty level:")
    print("1. Easy (Numbers 1-10)")
    print("2. Medium (Numbers 1-50)")
    print("3. Hard (Numbers 1-100 with 5 attempts)")

    difficulty = input("Enter 1 for Easy, 2 for Medium, 3 for Hard: ").strip()
    # Set the range and number of attempts based on difficulty level
    if difficulty == '1':
        max_number = 10
        attempts = None  # Unlimited attempts
        print("You have chosen Easy difficulty.")
    elif difficulty == '2':
        max_number = 50
        attempts = None  # Unlimited attempts
        print("You have chosen Medium difficulty.")
    elif difficulty == '3':
        max_number = 100
        attempts = 5  # Limit of 5 attempts
        print("You have chosen Hard difficulty.")
    else:
        print("Invalid choice, defaulting to Easy.")
        max_number = 10
        attempts = None

    # Generate a random number based on the difficulty level
    random_number = random.randint(1, max_number)
    print(random_number)

    current_attempts = 0

    # Start the guessing loop
    while not game_over:
        try:
            user_choice = int(input(f"Enter a number between 1 and {max_number}: "))

            if user_choice == random_number:
                print("Congratulations! You've guessed the correct number.")
                game_over = True
            elif user_choice > random_number:
                print("The Entered Number is Larger than the predicted number.")
                print("Enter a Smaller number.")
            elif user_choice < random_number:
                print("The Entered Number is Smaller than the predicted number.")
                print("Enter a Bigger number.")

            # Increment the number of attempts if playing on hard mode
            if attempts is not None:
                current_attempts += 1
                if current_attempts >= attempts:
                    print(f"Game over! You've used all {attempts} attempts. The number was {random_number}.")
                    game_over = True

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def play_game():
    while True:
        random_guessing_game()

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            print("\n " * 30)

        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break  # Exit the loop if the user doesn't want to play again


# Start the game
play_game()
