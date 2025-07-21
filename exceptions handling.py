try:
    num=int(input("Enter a number: "))
    print("The number entered is ",num)
except ValueError as ex:
    print("Exception: ", ex)
print()

#finally block example
try:
    num1,num2=eval(input("Enter two numbers separated by a comma: "))
    result=num1/num2
except ZeroDivisionError:
    print("Exception: Division by zero is not allowed.")
except SyntaxError:
    print("Exception: Invalid input format. Please enter two numbers separated by a comma.")
except:
    print("Wrong input")
else:
    print("The result of the division is: ", result)
finally:
    print("Smoothly Executed")
print()

#Bye Bye
valid=False
while not valid:
    try:
        num=int(input("Enter a number: "))
        while num%2==0:
            print("bye")
            valid=True
    except ValueError:
        print("Invalid! Please enter a valid number.")
print()

#taking the age and checking whether odd or even
try:
    age=int(input("Enter your age: "))
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError:
    print("Invalid! Please enter a valid number.")
finally:
    print("Thank you for using the age checker.")
print()