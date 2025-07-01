print("Loops in Python")
print()
 #sum of whole numbers
num= int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    print(i)
    sum += i
else:
    print("Loop completed successfully.")
print("Sum of whole numbers:", sum)
print()

 #reversing
ask= int(input("Enter a number: "))
for a in range(ask,0,-1):
    print(a)
print()
 
  #reversing a string
user= input("Enter a string: ")
for b in user[::-1]:
    print(b, end="")
print()

#calculating the power of the giving number
nbase = int(input("Enter base: "))
exponent = int(input("Enter exponent (must be positive): "))
if exponent < 0:
    print("Exponent cannot be negative.")
    exponent = int(input("Please enter a positive exponent: "))
else:
 result = 1
for _ in range(exponent):
    result *= nbase

print("The number", nbase, "to the power of", exponent, "is", result)
