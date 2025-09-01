class vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vehicle):

    def __init__(self, max_speed, mileage, brand, model, capacity):
        vehicle.__init__(self,max_speed, mileage)
        self.brand = brand
        self.model = model
        self.capacity = capacity
        


    def display(self):
        print("Brand is: ", self.brand)
        print("Model is: ", self.model)
        print("Capacity is: ", self.capacity)
        print("Max Speed is: ", self.max_speed)
        print("Mileage is: ", self.mileage)
        
bus1 = Bus(120, 15, "Mercedes", "Sprinter", 50)
bus2 = Bus(100, 12, "Volvo", "9400", 60)
bus3 = Bus(90, 10, "Scania", "Citywide", 55)
bus4 = Bus(110, 14, "Ashok Leyland", "Viking", 70)
bus5 = Bus(95, 11, "MAN", "Lions Coach", 65)

bus1.display()
print()
bus2.display()
print()
bus3.display()
print()
bus4.display()
print()
bus5.display()
print()
 

 #Employee Inheritance
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)

class Employee(Person):
    def __init__(self, name, id, salary, post):
        super().__init__(name, id)
        self.salary = salary
        self.post = post

    def display(self):
        super().display()
        print("Salary:", self.salary)
        print("Post:", self.post)

a = Employee("Tasleem", 11, 1400000, "Chief Executive Officer")
b = Employee("Ibraheem", 13, 800000, "Finance Manager")
c = Employee("Hamza", 12, 750000, "Cyber Security")
d = Employee("Yousuf", 15, 700000, "Software Engineer")
e = Employee("Ayesha", 14, 900000, "Doctor")

a.display()
print()
b.display()
print()
c.display()
print()
d.display()
print()
e.display()
print()

#Super Penguin
class Bird:
    def __init__(self): 
        print("Bird is ready") 

    def WhoIsThis(self):
        print("Bird ")

    def swim(self):
        print("Swim faster")

class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def WhoIsThis(self):
        print("Penguin ")

    def run(self):
        print("Run faster")

peggy=penguin()
peggy.WhoIsThis()
peggy.run()
peggy.swim()
print()

#Bus Fare

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() + super().fare() * 0.10

capacity = int(input("Enter number of passengers: "))
bus1 = Bus(capacity)
print("Total Bus Fare:", bus1.fare())

