#example of nested loops
for char in range(5):
    for i in range(1,11):
        print(i, end="")
    print()  # Moves to the next line after each outer loop iteration
print()

#how many prime numbers between a range
upper = int(input("Enter the upper limit: "))
lower = int(input("Enter the lower limit: "))
for num in range(upper, lower + 1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
print()

#character occurence in a string
string = input("Enter a word: ")
char = input("Enter a character to count: ")
count = 0
i= 0
while (i < len(string)):
    if(string[i] == char):
        count += 1
    i += 1
print("Count of", char, "in", string, "is:", count)
print()

# Calculate the product of the middle digits of a number
num = input("Enter a 3 or more digit number: ")
if len(num) <= 2:
    print("No middle digits to multiply.")
else:
    middle_digits = num[1:-1]
    product = 1
    for digit in middle_digits:
        product *= int(digit)
    print("Product of the middle digits is:", product)
print()

# Ask the user to enter a decimal number 
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:] 
print("Binary number is:", binary)

