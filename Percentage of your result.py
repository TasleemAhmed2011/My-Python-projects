print("\n📘 SUBJECT PERCENTAGE & GRADE CALCULATOR\n")

# ------------------ GRADE HELPER ------------------ #

def get_grade(obtained, boundaries):
    for grade, min_marks in boundaries.items():
        if obtained >= min_marks:
            return grade
    return "U"


def calculate_subject(subject, max_marks, grade_limits):
    print(f"\n--- {subject} ---")
    print(f"Total Marks: {max_marks}")

    obtained = int(input("Enter Obtained Marks: "))

    if obtained < 0 or obtained > max_marks:
        print("❌ Invalid marks entered!")
        return 0, 0

    percentage = (obtained / max_marks) * 100
    grade = get_grade(obtained, grade_limits)

    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    return max_marks, obtained


# ------------------ FIXED GRADE BOUNDARIES ------------------ #

# PST – 150
pst_grades = {
    "A*": 112,
    "A": 99,
    "B": 87,
    "C": 76,
    "D": 66,
    "E": 55,
    "F": 0
}

# ISL – 100
isl_grades = {
    "A*": 74,
    "A": 66,
    "B": 58,
    "C": 50,
    "D": 42,
    "E": 34,
    "F": 0
}

# URDU – 100
urdu_grades = {
    "A*": 91,
    "A": 81,
    "B": 70,
    "C": 58,
    "D": 47,
    "E": 37,
    "F": 0
}

# GENERIC 100 MARK SUBJECTS
generic_100_grades = {
    "A*": 90,
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50,
    "U": 0
}

# GENERIC 50 MARK SUBJECTS
generic_50_grades = {
    "A*": 40,
    "A": 30,
    "B": 20,
    "C": 15,
    "D": 10,
    "U": 0
}


# ------------------ MAIN CALCULATOR FUNCTION ------------------ #

def run_calculator():
    overall_total = 0
    overall_obtained = 0

    # PST
    t, o = calculate_subject("Pakistan Studies (PST)", 150, pst_grades)
    overall_total += t
    overall_obtained += o

    # ISL
    t, o = calculate_subject("Islamiat", 100, isl_grades)
    overall_total += t
    overall_obtained += o

    # URDU
    t, o = calculate_subject("Urdu", 100, urdu_grades)
    overall_total += t
    overall_obtained += o

    # MATHS
    t, o = calculate_subject("Maths", 100, generic_100_grades)
    overall_total += t
    overall_obtained += o

    # ENGLISH
    t, o = calculate_subject("English", 50, generic_50_grades)
    overall_total += t
    overall_obtained += o

    # SCIENCE
    t, o = calculate_subject("Science", 100, generic_100_grades)
    overall_total += t
    overall_obtained += o

    # COMPUTER
    t, o = calculate_subject("Computer", 100, generic_100_grades)
    overall_total += t
    overall_obtained += o

    # MQ
    t, o = calculate_subject("M.Q", 50, generic_50_grades)
    overall_total += t
    overall_obtained += o

    # OVERALL %
    print("\n===============================")
    print("📊 OVERALL RESULT")
    print(f"Total Marks (All Subjects): {overall_total}")
    print(f"Total Obtained Marks:       {overall_obtained}")

    if overall_total > 0:
        overall_percentage = (overall_obtained / overall_total) * 100
        print(f"Overall Percentage: {overall_percentage:.2f}%")
    else:
        print("Cannot calculate overall percentage (total marks = 0)")

    print("===============================\n")



# ------------------ LOOP ADDED HERE ------------------ #

while True:
    run_calculator()
    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again not in ("yes", "y"):
        print("\nThank you for using the calculator! 👋")
        break
