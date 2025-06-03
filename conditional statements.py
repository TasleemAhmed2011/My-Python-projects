var1=int(input("Enter your age: "))
if var1 < 18:
    print("You cannot drive any vehicle as you have not got a licence.")

if var1 < 18:
    print("You cannot vote as you are under 18.")
else:
    print("You can vote as you are above 18.")

print("Profit and Loss Calculator")
cprice = float(input("Enter the cost price of the item: "))
sprice = float(input("Enter the selling price of the item: "))

if sprice > cprice:
    print("Profit:", sprice - cprice)
elif sprice < cprice:
    print("Loss:", cprice - sprice)
else:
    print("No Profit No Loss")

print("Great and small number checker ")
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

print("Odd or Even Number Checker")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number:", num)
else:
    print("Odd number:", num)

print("Leap Year Checker")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")