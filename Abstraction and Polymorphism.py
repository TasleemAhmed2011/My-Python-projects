#Class Animal
from abc import ABC, abstractmethod
class animal(ABC):
     def move(self):
          pass

class human(animal):

     def move(self):
          print("I can walk and run")

class snake(animal):

        def move(self):
            print("I can crawl")

class dog(animal):

        def move(self):
            print("I can bark")

class lion(animal):
        def move(self):
            print("I can roar")

class cat(animal):
        def move(self):
            print("I can meow")

class monkey(animal):
        def move(self):
            print("I can climb trees")

R=human()
R.move()
S=snake()
S.move()
D=dog()
D.move()
L=lion()
L.move()
C=cat()
C.move()
M=monkey()
M.move()
print()

#Abstract class
from abc import ABC, abstractmethod
class absclass():
      
      def print(self,x):
          print("Passes vlalue is:",x)

      @abstractmethod
      def task(self):
            print("We are in the ABsclass.")

class test_class(absclass):

      def task(self):
            print("We are in the test_class task.")

obj=test_class()
obj.task()
obg.print(100)

#info of country

# Class 1
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


# Class 2
class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


# Class 3
class Pakistan:
    def capital(self):
        print("Islamabad is the capital of Pakistan.")

    def language(self):
        print("Urdu is the national language of Pakistan.")

    def type(self):
        print("Pakistan is a developing country.")


# Creating objects
obj_india = India()
obj_usa = USA()
obj_pakistan = Pakistan()

# Calling the methods
print("---- India Info ----")
obj_india.capital()
obj_india.language()
obj_india.type()

print("\n---- USA Info ----")
obj_usa.capital()
obj_usa.language()
obj_usa.type()

print("\n---- Pakistan Info ----")
obj_pakistan.capital()
obj_pakistan.language()
obj_pakistan.type()
print()

# Cars
# Class 1
class BMW:
    def start(self):
        print("BMW engine starts with a smooth sound.")

    def stop(self):
        print("BMW engine stops.")

    def accelerate(self):
        print("BMW accelerates fast with 625 horsepower.")


# Class 2
class Ferrari:
    def start(self):
        print("Ferrari engine roars loudly!")

    def stop(self):
        print("Ferrari engine turns off.")

    def accelerate(self):
        print("Ferrari accelerates super fast with 710 horsepower.")


# Polymorphism function
def road_test(car):
    car.start()
    car.accelerate()
    car.stop()


# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Run the same function for both cars
print("---- BMW Test ----")
road_test(bmw_car)

print("\n---- Ferrari Test ----")
road_test(ferrari_car)


# Cars

