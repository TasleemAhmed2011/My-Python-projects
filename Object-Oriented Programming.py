class fruits():
    def __init__(self,n,c):
     self.name = n
     self.color = c
    def display(self):
         print(self.name+" is " + self.color+" in color.")

fruit1 = fruits("Apple", "Red")
fruit1.display()
fruit2 = fruits("Banana", "Yellow")
fruit2.display()
fruit3 = fruits("Grapes", "Green")
fruit3.display()
fruit4 = fruits("Orange", "Orange")
fruit4.display()
fruit5 = fruits("Pineapple", "Brown")
fruit5.display()
print()

#Vehicles

class vehicle():
    def __init__(self, s, mo, m):
        self.max_speed = s
        self.mileage = m
        self.model = mo
    def display(self):
        print("The " + self.model + " has a maximum speed of " + str(self.max_speed) + " km/h, With the mileage of " + str(self.mileage))
        print()  
car6 = vehicle(340, "Bugatti Chiron", 5)
car6.display()
car7 = vehicle(355, "Lamborghini Sian", 6)
car7.display()
car8 = vehicle(320, "Ferrari SF90 Stradale", 7)
car8.display()
car9 = vehicle(310, "McLaren 720S", 8)
car9.display()
car10 = vehicle(305, "Porsche 911 Turbo S", 9)
car10.display()
car11 = vehicle(300, "Aston Martin DBS Superleggera", 10)
car11.display()
car12 = vehicle(295, "Rolls-Royce Phantom", 12)
car12.display()
car13 = vehicle(290, "Bentley Continental GT", 13)
car13.display()
car14= vehicle(285, "Nissan GTR", 14)
car14.display()
print()

#Class Parrot

class Parrot():

    species = "bird"
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

blu= Parrot("Blu", "blue", 10)
woo= Parrot("Woo", "green", 15)

print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

print("{} is {} and is {} years old.".format(blu.name, blu.color, blu.age))
print("{} is {} and is {} years old.".format(woo.name, woo.color, woo.age))
print()

#String UpperCase

class String():
 
  def __init__(self):
      self.str1 =""

  def get_string(self):
      self.str1=input("Enter a string: ")

  def print_string(self):
      print("Result is: "+ self.str1.upper())
      
str1 = String()

str1.get_string()
str1.print_string()
print()

#Employee In and Out

class Employee():

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print('Employee deleted')

def Create_obj():
        print('Creating an employee object')
        obj= Employee()
        print('Employee object created')
        return obj
print('Calling Create_obj()')
obj = Create_obj()
print('Program Ended')
print()

#pair elements

class pair_elements:
  def twoSum(self, nums, target):
    lookup = {}
    
    for i,num in enumerate(nums):
       if target - num in lookup:
            return (lookup [target  - num], i)
       lookup[num] = i
       
value= int(input("Enter sum for which you want to make this search: "))
x=pair_elements().twoSum((10,20,30,40,50,60,70), value)
print(x)



