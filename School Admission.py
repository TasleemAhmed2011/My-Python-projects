import random

school_name = "The Benchmark School"

# Age ranges for each class
age_ranges = {
    "1": (6.0, 6.9), "2": (7.0, 7.9), "3": (8.0, 8.9), "4": (9.0, 9.9),
    "5": (10.0, 10.9), "6": (11.0, 11.9), "7": (12.0, 12.9), "8": (13.0, 13.9),
    "O-1": (14.0, 14.9), "O-2": (15.0, 15.9), "O-3": (16.0, 16.9)
}

# total students
n = int(input("How many students are there for admission? "))

# seats available (random number between 1 and n)
seats = random.randint(1, n)
print("Seats available in the school:", seats)

# loop for each student
for i in range(1, n + 1):
    print(f"\n--- Student {i} ---")
    name = input("Enter student's name: ")
    age = float(input("Enter age (e.g. 6.5): "))
    class_label = input("Enter class (1-8 or O-1/O-2/O-3): ")
    prev_school = input("Enter previous school: ")

    p1 = float(input("Enter percentage of previous class 1: "))
    p2 = float(input("Enter percentage of previous class 2: "))
    p3 = float(input("Enter percentage of previous class 3: "))
    admission_test = float(input("Enter Admission Test percentage: "))

    avg = (p1 + p2 + p3) / 3

    # check age
    if class_label in age_ranges:
        min_age, max_age = age_ranges[class_label]
        age_ok = (min_age <= age <= max_age)
    else:
        age_ok = False

    # check academics
    academic_ok = (avg >= 65 and p1 >= 50 and p2 >= 50 and p3 >= 50)

    # check test
    test_ok = (admission_test >= 60)

    # final decision
    if age_ok and academic_ok and test_ok:
        decision = "ADMITTED"
    elif avg >= 60 or admission_test >= 55:
        decision = "REVIEW"
    else:
        decision = "REJECTED"

    # summary
    print("\nAdmission Summary")
    print("=================")
    print("School:", school_name)
    print("Name:", name)
    print("Age:", age)
    print("Class:", class_label)
    print("Previous School:", prev_school)
    print(f"Percentages: {p1}%, {p2}%, {p3}%")
    print(f"Average: {avg:.2f}%")
    print("Admission Test %:", admission_test)
    print("Age Check:", "OK" if age_ok else "Not OK")
    print("Decision:", decision)
