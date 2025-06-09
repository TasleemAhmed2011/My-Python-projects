#average
import math
import random
print("This program will generate 5 random numbers and calculate their total.")
print("The numbers will be between 0 and 50, 0 and 35, 0 and 36, 0 and 90, and 0 and 99 respectively.")
print("The average will also be calculated.")
print("Let's begin!")
var1 = math.floor(random.random() * 50)
var2 = math.floor(random.random() * 35)
var3 = math.floor(random.random() * 36)
var4 = math.floor(random.random() * 90)
var5 = math.floor(random.random() * 99)
total = (var1 + var2 + var3 + var4 + var5)
print("The total is: " + str(total))
print("The average is: " + str(total / 5))
print()
#counting the notes
ask= int(input("How many money do you have currently? (in pkr) "))
print("Let's count the notes you have.")
note5000 = ask // 5000
note1000 = (ask % 5000) // 1000
note500 = (ask % 1000) // 500
note100 = (ask % 500) // 100
note50 = (ask % 100) // 50
note20 = (ask % 50) // 20
note10 = (ask % 20) // 10
print("You have:")
print(note5000, "notes of 5000")
print(note1000, "notes of 1000")
print(note500, "notes of 500")
print(note100, "notes of 100")
print(note50, "notes of 50")
print(note20, "notes of 20")
print(note10, "notes of 10")
print("You have", ask, "pkr in total.")

#percentage calculation
print()
print("Let's calculate your percentage for 5 common subjects (each out of 100).")
subjects = ["Math", "English", "Science", "Urdu", "Hindi"]
marks = []
# Collect marks for each subject one by one in a simple way
math_marks = int(input("Enter marks obtained in Math (out of 100): "))
english_marks = int(input("Enter marks obtained in English (out of 100): "))
science_marks = int(input("Enter marks obtained in Science (out of 100): "))
urdu_marks = int(input("Enter marks obtained in Urdu (out of 100): "))
hindi_marks = int(input("Enter marks obtained in Hindi (out of 100): "))

# Add all marks
total_marks = math_marks + english_marks + science_marks + urdu_marks + hindi_marks

# Calculate percentage
percentage = (total_marks / 500) * 100

# Print results
print("Your total marks are:", total_marks, "out of 500.")
print("Your percentage is:", percentage, "%.")
