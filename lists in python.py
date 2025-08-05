#all lists in python
list1 = [1,2.0,3.1,"4",True,"abc"]
list2 = ["mm","nn"]
print(list1)
print(type(list1))
print(len(list1))
  #indexing
print(list1[0])
print(list1[-1])
  #slicing
print(list1[0:3])
  #iteration
for item in list1:
    print(item)

  #concatenation
list3 = list1+list2
print(list3)

list1.extend(list2) 
print(list1)
list2.append("oo")
print(list2)

list4 =[1,1,1,90,12,34]
print(max(list4))
print(min(list4))
cnt = list4.count(1)
print(cnt)
list4.reverse()
print(list4)

nested_list = [[1,2,3],"abc",90]
sublist = nested_list[0]
print(sublist[0])

print([1,2,3]*3)
nested_list.insert(2,"new")
print(nested_list)
print(nested_list.pop())
print(nested_list)
print()

#lists
empty_list = []
print(empty_list)
list1 = [11,'Tasleem',13.7]
print(list1*3)
print('reversing using reverse() method')
my_fruits_list= ['apple', 'banana', 'Mango']
my_fruits_list.reverse()
print(my_fruits_list)
print('reversing using slicing')
my_fruits_list= my_fruits_list[::-1]
print(my_fruits_list)
print()

#word matching
words = ["abc", "xyz", "aba", "aa", "x"]
count = 0
for word in words:
    if len(word) >= 2:
        first_character = word[0]
        last_character = word[len(word) - 1]
        if first_character == last_character:
            count = count + 1
print("Number of strings with same first and last character:", count)
print()


#playing with list
print("\n11 and 14 my favourute numbers.\n 7 is for legends Dhoni and Ronaldo.\n56 for all time bobby king.\n18 for king cheeku and 45 for master hitman.")
print(  )
num = [11,14,7,56,18,45]
print("The list of numbers are:",num)
total = 0
for number in num:
 total=total+number
print("The total of the numbers in the list is:",total)
val=len(num)
print("The total elements in the list is:",val)
average=total/val
r_average=round(average,2)
print('The average of numbers in list is:',r_average)
print()

# Square values in a range and categorize them as even or odd
print("Square values in a range and categorize them as even or odd")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
even_squares = []
odd_squares = []

for number in range(start, end + 1):
    square = number * number
    squares.append(square)
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
