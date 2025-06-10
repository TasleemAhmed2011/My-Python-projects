# can a student give his exam
def student_exam_eligibility():
    print("Welcome to the Student Exam Eligibility Checker!")
    print("Please answer the following questions to determine if you can give the exam.")

    # Check if the student has a medical problem
    problem = input("Do you have a medical problem? (yes/no): ")

    if problem == "yes":
        medical = input("Do you have a medical certificate? (yes/no): ")
        
        if medical == "yes":
            print("Thank you. Your certificate will be verified.")
        elif medical == "no":
            print("You need to submit a medical certificate.")
        else:
            print("Invalid answer. Please type yes or no.")
            
    elif problem == "no":
        print("Okay, no medical certificate needed.")
    else:
        print("Invalid answer. Please type yes or no.")
problem = input("Do you have a medical problem? (yes/no): ")

if problem == "yes":
    medical = input("Do you have a medical certificate? (yes/no): ")
    
    if medical == "yes":
        print("Thank you. Your certificate will be verified.")
    elif medical == "no":
        print("You need to submit a medical certificate.")
    else:
        print("Invalid answer. Please type yes or no.")
        
elif problem == "no":
    print("Okay, no medical certificate needed.")
else:
    print("Invalid answer. Please type yes or no.")

print()

total_days = 200
present_days = int(input("Enter number of days the student was present: "))
attendance_percent = (present_days / total_days) * 100

if present_days >= 0:
    if attendance_percent >= 75:
        print("Attendance:", attendance_percent, "%")
        print("Student is eligible to give the exam.")
    else:
        print("Attendance:", attendance_percent, "%")
        print("Student is NOT eligible to give the exam.")
else:
    print("Invalid input for present days.")

#calculating the amount of a person of electricity bill
def calculate_electricity_bill():
    print("Welcome to the Electricity Bill Calculator!")
    print("Please enter the number of units consumed to calculate your bill.")
units = int(input("Enter the number of units consumed: "))
if units < 0:
    print("Invalid input for units consumed.")
elif units < 15:
    print("Your electricity bill is free for this month.")
elif units < 50:
    bill = units * 2.60
    surcharge = 25
    print("Your electricity bill falls in the 16-49 units range.")
        
elif units <= 100:
    bill = 130 + ((units - 50) * 3.25)
    surcharge = 35
    print("Your electricity bill falls in the 50-100 units range.")
        
elif units <= 200:
    bill = 130 + (50 * 3.25) + 526 + ((units - 200) * 8.25)
    surcharge = 75
    print("Your electricity bill falls in the 101-200 units range.")
print()

total = bill + surcharge
print("\nYour total electricity bill is: %.2f" % total, "rupees.")

#which vehicle do you want
def vehicle_choice():
    print("Welcome to the Vehicle Choice Program!")
    print("Please choose a vehicle type to proceed.")
print("\nWhich vehicle do you want to buy?")
print("1. Car")
print("2. Bike")
vehicle_choice = input("Enter your choice (1 or 2): ")
if vehicle_choice == "1":
    car_type = input("What type of car do you want? (sedan/SUV): ").lower()
    
    if car_type == "sedan":
        print("You have chosen a sedan car.")
    elif car_type == "suv":
        print("You have chosen an SUV car.")
    else:
        print("Invalid choice for car type.")
elif vehicle_choice == "2":
    bike_type = input("What type of bike do you want? (sports/cruiser/scooty/electric/scooter): ").lower()
    
    if bike_type == "sports":
        print("You have chosen a sports bike.")
    elif bike_type == "cruiser":
        print("You have chosen a cruiser bike.")
    elif bike_type == "scooty":
        print("You have chosen a scooty.")
    elif bike_type == "electric":
        print("You have chosen an electric bike.")
    elif bike_type == "scooter":
        print("You have chosen a scooter.")
    else:
        print("Invalid choice for bike type.")

#main menu
while True:
    print("\nMain Menu:")
    print("1. Check Student Exam Eligibility")
    print("2. Calculate Electricity Bill")
    print("3. Choose Vehicle")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        student_exam_eligibility()
    elif choice == "2":
        calculate_electricity_bill()
    elif choice == "3":
        vehicle_choice()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
