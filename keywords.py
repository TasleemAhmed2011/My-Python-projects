a = input("Enter a string: ")
a_char = input("Enter a character to find: ")
i = 1
for char in a:
    if char == a_char:
        print(f"Character found in letter {i}: {char}")
        break
    else:
        print(f"Character not found in letter {i}")
    i += 1
print()

# Bitwise operations example
for x in range(10):
    if x & 20 == 0:
        print("Twist")
    elif x & 15 == 0:
        pass
    elif x & 5 == 0:
        print("fizz")
    elif x & 3 == 0:
        print("buzz")
    else:
        print(f"{x}")
print()

#number fom 1 to 10 in reverse skipping 5
for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)
print()

#due payment example
def calculate_due():
    bill = float(input("Enter bill amount: "))
    paid = float(input("Enter amount paid: "))

    if bill < 0 or paid < 0:
        print("Invalid input")
        return

    if paid == bill:
        print("No due amount")
        return 0

    if paid > bill:
        extra = paid - bill
        print("Extra paid. Returning:", extra)
        return 0

    for i in range(1, 4):
        if paid < bill:
            due = bill - paid
            print("Due amount is:", due)
            break
        else:
            continue

    return bill - paid

due = calculate_due()
if due:
    print("Final due:", due)


