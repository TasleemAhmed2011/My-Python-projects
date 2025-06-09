var1="Ahmed"
var2=40
var3=40.6
var4= True
var11=type(var1)
var22=type(var2)
var33=type(var3)
var44=type(var4)
print("\nAhmed is a " + str(var11) + "." + "\n40 is a " + str(var22) + "." + "\n40.6 is a "+str(var33)+"." + "\nAhmed is my father that is true  " + str(var44) + ".")
print("Indexes")
str=input("\nEnter a string: ")
print("The string you entered is: " + str)
print("The length of the string is: " + str(len(str)))
print(str[::   -1])  # Reverses the string
print(str[::   3]) # Prints every 3rd character
print(str[:0])  # Prints an empty string
print(str[0:5])  # Prints the first 5 characters
print(str[5:])  # Prints the string from the 5th character to the end

#congratulation message
congrats = "\nCongratulations on winning the gold medal! We're proud of you. Keep up the great work!"
ucongrats = congrats.upper()
print(ucongrats)
