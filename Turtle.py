#MAKING A POLYGON
import turtle

def polygon():
    turtle.Screen().bgcolor("orange")
    turtle.pensize(5)
    turtle.pencolor("blue")
    turtle.Screen().setup(300, 400)
    polygon = turtle.Turtle()
    polygon.fillcolor("yellow")
    for i in range(8):
        polygon.forward(60)
        polygon.right(360 / 8)
    turtle.done()

#making a star
def star():
    turtle.Screen().bgcolor("Aqua")
    board = turtle.Turtle()
    board.fillcolor("red")
    board.forward(100)
    board.left(120)
    board.forward(100)
    board.left(120)
    board.forward(100)
    board.penup()
    board.right(150)
    board.forward(50)
    board.pendown()
    board.right(90)
    board.forward(100)
    board.right(120)
    board.forward(100)
    board.right(120)
    board.forward(100)
    turtle.done()

#spiral pattern
def spiral():
    turtle.Screen().bgcolor("Aqua")
    turtle.pencolor("red")
    turtle.pensize(3)
    circle = turtle.Turtle()
    circle.speed(15)
    for i in range(200):
        circle.forward(i * 2)
        circle.right(40)
    turtle.done()


#Main Menu
def main_menu(): 
    print("1. Draw Polygon")
    print("2. Draw Star")
    print("3. Draw Spiral")
    choice = input("Enter your choice: ")
    if choice == "1":
        polygon()
    elif choice == "2":
        star()
    elif choice == "3":
        spiral()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main_menu()
