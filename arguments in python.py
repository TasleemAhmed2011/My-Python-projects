# tip a waiter
def tip_calc(bill_amount, tip_percent):
    tip = bill_amount * tip_percent / 100
    total = bill_amount + tip
    tip = round(tip, 2)
    print("\nYour total amount is: " + str(total) + "\nFrom which the bill is: " + str(bill_amount) + " \nAnd the tip is: " + str(tip))
    return total

bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
tip_calc(bill, tip_percent)
print()

#cube of the cube
print()

# factorial of numbers
def factorial(tasleem):
    if tasleem == 0 or tasleem == 1:
        return 1
    else:
        return tasleem * factorial(tasleem - 1)
number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")