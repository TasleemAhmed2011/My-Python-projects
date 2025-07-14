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

