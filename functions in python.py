# Simple function program

name = input("Enter your name: ")
print("Hello, " + name)
print("Hope you are Fine!")
print("Have a great day ahead!")

# Addition of two numbers using function

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def add1():
    global num1, num2
    num1=12
    num2=13
    print()
add1()
print("Sum of two numbers is: ", num1 + num2)
print()

# Calculator functions
def calc_add(x, y):
    return x + y

def calc_subtract(x, y):
    return x - y

def calc_multiply(x, y):
    return x * y

def calc_divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Welcome to our simple calculator!")
    print("For operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print("The sum of ", num1, " and ", num2, " is: ", calc_add(num1, num2))
    elif choice == 2:
        print("The difference of ", num1, " and ", num2, " is: ", calc_subtract(num1, num2))
    elif choice == 3:
        print("The product of ", num1, " and ", num2, " is: ", calc_multiply(num1, num2))
    elif choice == 4:
        print("The result of dividing ", num1, " by ", num2, " is: ", calc_divide(num1, num2))
    else:
        print("Invalid choice.")
    print("\nHow was my calculator? \nIf you like it, please give it a big thumbs up! \nIf you like it then I'll try to make a more complex calculator for you only guys!\nThanks for using my calculator!")
    ask = input("Do you want to give a like? (yes/no): ")
    if ask == 'yes':
        print("Thanks Guys! You are awesome! 👍")
    elif ask == 'no':
        print("What else can I do!!. 👎")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    print()

#circumfence of circle function
def circumference_of_circle(radius):
    print("Calculating the circumference of a circle...")
    print("The formula for circumference is 2πr")
    if radius < 0:
        return "Error: Radius cannot be negative."
    elif radius == 0:
        return "The circumference of a circle with radius 0 is 0."
    elif radius > 0:
        pi = 3.14
        return 2 * pi * radius
radius = float(input("Enter the radius of the circle: "))
print("The circumference of the circle is:", circumference_of_circle(radius))

