print("Percentage of your Subjects")

print("History")
a=int(input("Enter your total marks"))
b=int(input("Enter your obtained marks"))
c=(b/100)*a
if a==100:
  b<=100
  print(c,"%")
else:
    print("Invalid Marks")

print("Geography")
d=int(input("Enter your total marks"))
e=int(input("Enter your obtained marks"))
f=(e/100)*d
if d==100:
  e<=100
  print(f,"%")
else:
    print("Invalid Marks")

print("Mathematics")
g=int(input("Enter your total marks"))
h=int(input("Enter your obtained marks"))
i=(h/100)*g
if g==100:
  h<=100
  print(i,"%")
else:
    print("Invalid Marks")


print("Science")
j=int(input("Enter your total marks"))
k=int(input("Enter your obtained marks"))
l=(k/100)*j
print(l,"%")

print("Urdu")
m=int(input("Enter your total marks"))
n=int(input("Enter your obtained marks"))
o=(n/100)*m
print(o,"%")

print("Mutalla-e-Quran")
p=int(input("Enter your total marks"))
q=int(input("Enter your obtained marks"))
r=(q/100)*p
print(r,"%")

print("English")
s=int(input("Enter your total marks"))
t=int(input("Enter your obtained marks"))
u=(t/100)*s
print(u,"%")

print("Computer")
v=int(input("Enter your total marks"))
w=int(input("Enter your obtained marks"))
x=(w/100)*v
print(x,"%")

print("Total Percentage")
tmarks=int(a+d+g+j+m+p+s)
omarks=int(b+e+h+k+n+q+t+w)
percentage=(omarks/100)*tmarks
print(percentage)

