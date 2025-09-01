import random

letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all_characters = letters_lower + letters_upper + numbers

password = ""
for i in range(10):
    password += random.choice(all_characters)

print("Generated Password:", password)
