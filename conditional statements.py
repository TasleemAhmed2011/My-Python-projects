var1=int(input("Enter your age: "))
if var1 < 18:
    print("You cannot drive any vehicle as you have not got a licence.")

if var1 < 18:
    print("You cannot vote as you are under 18.")
else:
    print("You can vote as you are above 18.")

print("Profit and Loss Calculator")
cprice = float(input("Enter the cost price of the item: "))
sprice = float(input("Enter the selling price of the item: "))

if sprice > cprice:
    print("Profit:", sprice - cprice)
elif sprice < cprice:
    print("Loss:", cprice - sprice)
else:
    print("No Profit No Loss")

