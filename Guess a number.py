import random

while True:
    secret_number = random.randint(0, 200)
    print("\nWelcome to the Guess a Number Game!")
    print("I have chosen a number between 0 and 200.")
    print("You have 15 guesses to find it.")

    for guess_number in range(1, 16):  # 1 to 15 guesses
        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("🎉 Correct! You guessed the number!")
            break
        else:
            print("❌ Wrong guess.")

            # Give a different hint for each guess
            if guess_number == 1:
                if secret_number % 2 == 0:
                    print("Hint 1: The number is even.")
                else:
                    print("Hint 1: The number is odd.")

            elif guess_number == 2:
                if secret_number > 100:
                    print("Hint 2: The number is greater than 100.")
                else:
                    print("Hint 2: The number is 100 or less.")

            elif guess_number == 3:
                if secret_number % 5 == 0:
                    print("Hint 3: The number is divisible by 5.")
                else:
                    print("Hint 3: The number is not divisible by 5.")

            elif guess_number == 4:
                print(f"Hint 4: The number is between {secret_number - 10} and {secret_number + 10}.")

            elif guess_number == 5:
                print(f"Hint 5: The number is closer to {secret_number//10*10}.")

            elif guess_number == 6:
                print(f"Hint 6: The first digit is {str(secret_number)[0]}.")

            elif guess_number == 7:
                print(f"Hint 7: The last digit is {str(secret_number)[-1]}.")

            elif guess_number == 8:
                if secret_number > 150:
                    print("Hint 8: The number is greater than 150.")
                else:
                    print("Hint 8: The number is 150 or less.")

            elif guess_number == 9:
                if secret_number % 3 == 0:
                    print("Hint 9: The number is divisible by 3.")
                else:
                    print("Hint 9: The number is not divisible by 3.")

            elif guess_number == 10:
                print(f"Hint 10: The number is between {secret_number - 20} and {secret_number + 20}.")

            elif guess_number == 11:
                if secret_number % 4 == 0:
                    print("Hint 11: The number is a multiple of 4.")
                else:
                    print("Hint 11: The number is not a multiple of 4.")

            elif guess_number == 12:
                if secret_number % 7 == 0:
                    print("Hint 12: The number is a multiple of 7.")
                else:
                    print("Hint 12: The number is not a multiple of 7.")

            elif guess_number == 13:
                is_prime = True
                if secret_number < 2:
                    is_prime = False
                else:
                    for i in range(2, int(secret_number**0.5) + 1):
                        if secret_number % i == 0:
                            is_prime = False
                            break
                if is_prime:
                    print("Hint 13: The number is prime.")
                else:
                    print("Hint 13: The number is not prime.")

            elif guess_number == 14:
                digit_sum = sum(int(d) for d in str(secret_number))
                print(f"Hint 14: The sum of the digits is {digit_sum}.")

            elif guess_number == 15:
                if secret_number > 100:
                    print("Hint 15: The number is in the upper half of the range.")
                else:
                    print("Hint 15: The number is in the lower half of the range.")

    else:
        # If loop completes without break
        print(f"\nGame Over! The secret number was {secret_number}.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
