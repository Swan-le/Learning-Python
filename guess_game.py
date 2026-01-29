import random

def start_game():
    #1. Game start
    choice = input("Do you want to play a game? (yes or no?)").strip().lower()
    
    #2. Check for yes
    if choice == "yes":
        print("\nGreat choice! I'm thinking of a number between 1 & 500.")
        print("Lets see how many tries it takes to guess correctly.")

        #Auto geneerate number
        secret_number = random.randint(1,500)
        attempts = 0
        guessed_correctly = False

        #3. The guessing Loop
        while not guessed_correctly:
            try:
                guess = int(input("\nEnter your guess: "))
                attempts += 1

                if guess > 500:
                    print("Your guess is outside the guess range, try a lower number")
                elif guess < secret_number:
                    print("Too low! Try again Noob!")
                elif guess > secret_number:
                    print("Too high! Try again")
                elif guess > 500:
                    print("Your number is outside the guessing range, try a number under 500")
                else:
                    print(f"Congrats! You found it in {attempts} attemps!")
                    guessed_correctly = True
            except ValueError:
                print("Please enter a valid whole number.")
    else:
        print("Better luck next time.")

# Run the game
if __name__ == "__main__":
    start_game()
