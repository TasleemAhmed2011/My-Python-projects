print("While loops in Python")
print()

#sum of natural numbers
natural_num = int(input("Enter a number to which the sum will end starting from 1: "))
sum = 0
i = 1
while i <= natural_num:
    sum += i
    i += 1
    print("Current sum is:", sum)
print("The sum of natural numbers up to", natural_num, "by", i, "is:", sum)
print()

#infinite loop
i=int(input("Enter a number to start the infinite loop: "))
while i*0<1:
    print("\nThis will run forever unless stopped.","\n Computer 'Bhai meri bass hogai hai!🙏💔✨'")
print()

#armstrong numbers 3 digits

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

