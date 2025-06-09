def age_restrictions():
    var1 = int(input("Enter your age: "))
    if var1 < 18:
        print("You cannot drive any vehicle as you have not got a licence.")
        print("You cannot vote as you are under 18.")
    else:
        print("You can vote as you are above 18.")
    print()

def profit_and_loss_calculator():
    print("Profit and Loss Calculator")
    cprice = float(input("Enter the cost price of the item: "))
    sprice = float(input("Enter the selling price of the item: "))
    if sprice > cprice:
        print("Profit:", sprice - cprice)
    elif sprice < cprice:
        print("Loss:", cprice - sprice)
    else:
        print("No Profit No Loss")
    print()

def great_and_small_number_checker():
    print("Great and small number checker")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 > num2:
        print("Great number:", num1)
        print("Small number:", num2)
    elif num1 < num2:
        print("Great number:", num2)
        print("Small number:", num1)
    else:
        print("Both numbers are equal.")
    print()

def odd_or_even_checker():
    print("Odd or Even Number Checker")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even number:", num)
    else:
        print("Odd number:", num)
    print()

def leap_year_checker():
    print("Leap Year Checker")
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
    print()

def temp_checker():
    print("Clothing Recommendation Based on Temperature")
    temperature = float(input("Enter the temperature in Celsius for yourself: "))
    if temperature > 25:
        print("It's a hot day. Wear light clothes.")
    else:
        print("It's a cold day. Wear heavy clothes.")
    print()

while True:
    print("\nWhich program do you want to run?")
    print("1. Age restrictions")
    print("2. Profit and loss calculator")
    print("3. Great and small number checker")
    print("4. Odd or Even Number Checker")
    print("5. Leap Year Checker")
    print("6. Clothing recommendation based on temperature")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        age_restrictions()
    elif choice == "2":
        profit_and_loss_calculator()
    elif choice == "3":
        great_and_small_number_checker()
    elif choice == "4":
        odd_or_even_checker()
    elif choice == "5":
        leap_year_checker()
    elif choice == "6":
        temp_checker()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
