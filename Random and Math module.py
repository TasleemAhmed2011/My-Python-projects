import random
# A Number Game
playing=True
number=str(random.randint(0,9))
print("I will generate any number in between 0 to 9 and you have to guess one at a time!")
print("The game ends when you get the correct number only.")
while playing:
  guess=input("Enter your guess: ")

  if guess==number:
    print("You guessed it right!")
    print("The number was:", number)
    playing=False
  else:
    print("Wrong guess! Try again.")
print()

#Rock Paper Scissors
choices = ['rock', 'paper', 'scissors']
while True:
    computer_choice = random.choice(choices)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
    else:
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print("Rock beats scissors.")
            print("You win!")
        elif user_choice == 'paper' and computer_choice == 'rock':
            print("Paper beats rock.")
            print("You win!")
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print("Scissors beats paper.")
            print("You win!")
        elif user_choice == 'rock' and computer_choice == 'paper':
            print("Paper beats rock.")
            print("You lose!")
        elif user_choice == 'paper' and computer_choice == 'scissors':
            print("Scissors beats paper.")
            print("You lose!")
        elif user_choice == 'scissors' and computer_choice == 'rock':
            print("Rock beats scissors.")
            print("You lose!")
    play = input("Do you want to play again? (yes/no): ").lower()
    if play != 'yes':
        break
print("Thanks for playing!")
print()


import math
angle = float(input("Enter angle in degrees: "))
radian = math.radians(angle)
sin_value = round(math.sin(radian), 4)
cos_value = round(math.cos(radian), 4)
tan_value = round(math.tan(radian), 4)
print(f"Sine: {sin_value}, Cosine: {cos_value}, Tangent: {tan_value}")
print()
