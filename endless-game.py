import random

def start_game():
    choice = input("I bet you won't win this game, do you want to try? (Yes / No)").strip().lower()

    if choice == "yes":
        print("\nGreat! Pick a number 1 through 10.")
        print("Let's see if you can win. Muahah...")

        attempts = 0 
        guessed_correctly = False

        while not guessed_correctly: 
            secret_number = random.randint (1, 10)

            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess == secret_number:
                    print("\nWOW! That's Amazing, you won")
                    guessed_correctly = True
                else:
                    if attempts >= 9:
                        print(f"\nThis is boring, I'm Leaving!")
                        print("Bye Bye!")
                        break

                    hint = "Too high!" if guess > secret_number else "Too Low!"
                    print(f"{hint}! Try again.")
            except ValueError:
                print("Please enter a valid number (1 - 10)")
    else:
        print("Aww too bad, come back soon!")
        print("Bye, Bye")
if __name__ == "__main__":
    start_game()

