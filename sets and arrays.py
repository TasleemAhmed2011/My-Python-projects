s1 = {1,2,3,33,44,555,"111",111,44.00,555}
print(s1)
s1.add(25)
print(s1)
s2 = {(1,2,3),11,12}
print(s2)

s3 = set([1,2,3,4,5,6])
print(s3)
print(type(s3))
print(s3.pop())
print(s3)
print()

# Sets and Arrays in Python
in1=input("Enter the first element of first set:")
in2=input("Enter the second element of first set:")
in3=input("Enter the first element of second set:")
in4=input("Enter the second element of second set:")
print()
s1={in1,in2}
s2={in3,in4}
print("Set1 is:",s1)
print("Set2 is:",s2)
print()
s_inter=s1.intersection(s2)
s_union=s1.union(s2)
s_diff1=s1.difference(s2)
s_diff2=s2.difference(s1)
s_symdiff=s1.symmetric_difference(s2)
print("The intersection of set1 and set2 is:",s_inter)
print("The union of set1 and set2 is:",s_union)
print("The difference of set1 and set2 from set1 to set2 is:",s_diff1)
print("The difference of set1 and set2 from set2 to set1 is:",s_diff2)
print("The symmetric difference of set1 and set2 is:",s_symdiff)
print()

## Arrays in Python
import array as arr

a = arr.array('i', [1, 2, 3, 4, 1, 1, 3, 4])
print(a)
print(type(a))
print(a.count(1))
a.reverse()
print(a)



