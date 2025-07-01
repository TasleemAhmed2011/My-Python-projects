#printing stars in a pattern 
def print_stars():
    rows=int(input("Enter the number of rows: "))
    for i in range(1,rows+1):
        for _ in range(i):
            print("*", end="")
        print()
print()

#making a triangle pattern by numbers
def print_triangle():
    k=1
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows + 1):
        for _ in range(1, i + 1):
            print(k, end="")
            k += 1
        print()
print()

#making diamond pattern by numbers
def print_diamond():
    rows = int(input("Enter the number of rows: "))
    space = rows - 1
    for i in range(1, rows + 1):
        for _ in range(1, space + 1):
          print(end=" ")
        space -= 1
        num=1
        for _ in range( i * 2 - 1):
          print(num, end="")
          num += 1
        print()
print()

#MAKING A MIRROR TRIANGLE PATTERN
def print_mirror_triangle():
    rows = int(input("Enter the number of rows: "))
    for i in range(rows, 0, -1):
        for _ in range(i):
            print("*", end="")
        print()
        
#main menu
def main_menu():
    print("1. Print Stars")
    print("2. Print Triangle")
    print("3. Print Diamond")
    print("4. Print Mirror Triangle")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print_stars()
    elif choice == "2":
        print_triangle()
    elif choice == "3":
        print_diamond()
    elif choice == "4":
        print_mirror_triangle()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()
main_menu()
