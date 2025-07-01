print("While loops in Python")
print()

#sum of natural numbers
def sum_of_natural_numbers(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
        print("Current sum is:", sum)
    print("The sum of natural numbers up to", n, "is:", sum)
    print()

#infinite loop
def infinite_loop():
    print("This is an infinite loop. Press Ctrl+C to stop it.")
    while True:
        pass
i=int(input("Enter a number to start the infinite loop: "))
while i*0<1:
    print("\nThis will run forever unless stopped.","\n Computer 'Bhai meri bass hogai hai!🙏💔✨'")
print()

#armstrong numbers 3 digits
def armstrong_number():
    num = int(input("Enter a 3-digit number to check if it is an Armstrong number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")
print()

#checking he total number of digits in a number
def count_digits():
    num = int(input("Enter a number to count its digits: "))
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("The total number of digits is:", count)
print()
