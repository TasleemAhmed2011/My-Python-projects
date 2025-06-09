import math

def average_program():
    print("This program will ask you to enter 5 numbers within specific ranges and calculate their total.")
    print("Please enter numbers as follows:")
    print("1st number: between 0 and 50")
    print("2nd number: between 0 and 35")
    print("3rd number: between 0 and 36")
    print("4th number: between 0 and 90")
    print("5th number: between 0 and 99")
    print("The average will also be calculated.")
    print("Let's begin!")
    var1 = int(input("Enter the 1st number (0-50): "))
    var2 = int(input("Enter the 2nd number (0-35): "))
    var3 = int(input("Enter the 3rd number (0-36): "))
    var4 = int(input("Enter the 4th number (0-90): "))
    var5 = int(input("Enter the 5th number (0-99): "))
    total = (var1 + var2 + var3 + var4 + var5)
    print("The total is: " + str(total))
    print("The average is: " + str(total / 5))
    print()

def count_notes_program():
    ask= int(input("How many money do you have currently? (in pkr) "))
    print("Let's count the notes you have.")
    note5000 = ask // 5000
    note1000 = (ask % 5000) // 1000
    note500 = (ask % 1000) // 500
    note100 = (ask % 500) // 100
    note50 = (ask % 100) // 50
    note20 = (ask % 50) // 20
    note10 = (ask % 20) // 10
    print("You have:")
    print(note5000, "notes of 5000")
    print(note1000, "notes of 1000")
    print(note500, "notes of 500")
    print(note100, "notes of 100")
    print(note50, "notes of 50")
    print(note20, "notes of 20")
    print(note10, "notes of 10")
    print("You have", ask, "pkr in total.")

def percentage_program():
    print("Let's calculate your percentage for 5 common subjects (each out of 100).")
    math_marks = int(input("Enter marks obtained in Math (out of 100): "))
    english_marks = int(input("Enter marks obtained in English (out of 100): "))
    science_marks = int(input("Enter marks obtained in Science (out of 100): "))
    urdu_marks = int(input("Enter marks obtained in Urdu (out of 100): "))
    hindi_marks = int(input("Enter marks obtained in Hindi (out of 100): "))
    total_marks = math_marks + english_marks + science_marks + urdu_marks + hindi_marks
    percentage = (total_marks / 500) * 100
    print("Your total marks are:", total_marks, "out of 500.")
    print("Your percentage is:", percentage, "%.")
    if percentage < 50:
        print("Grade: U (Ungraded/Fail)")
        print("You are Fail.")
    elif 90 <= percentage <= 100:
        print("Grade: A* (EXCELLENT)")
    elif 80 <= percentage < 90:
        print("Grade: A (MEETS STANDARD)")
    elif 70 <= percentage < 80:
        print("Grade: B (GOOD PERFORMANCE)")
    elif 60 <= percentage < 70:
        print("Grade: C (AVERAGE)")
    elif 50 <= percentage < 60:
        print("Grade: D (BELOW AVERAGE)")
    print()

def square_root_program():
    print("Let's calculate the square root of a number.")
    number = float(input("Enter a number to find its square root: "))
    square_root = number ** 0.5
    print("The square root of", number, "is:", square_root)

# Main menu
while True:
    print("\nWhich program do you want to run?")
    print("1. Average of 5 numbers")
    print("2. Count money notes")
    print("3. Calculate percentage")
    print("4. Find square root")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        average_program()
    elif choice == "2":
        count_notes_program()
    elif choice == "3":
        percentage_program()
    elif choice == "4":
        square_root_program()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

