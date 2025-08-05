my_info={"Name":"Tasleem Ahmed","Age":14,"City":"Karachi"}
n=my_info["Name"]
a=my_info["Age"]
c=my_info["City"]
l=len(my_info)
print("My name is",n,",and my age is",a,".I live in City",c,".")
my_info["Name"]="Tasleem Ahmed Sabri"
my_info["Age"]=13.7
print("Original dictionary:⤴ \n","My name is",my_info["Name"],",and my age is",my_info["Age"],".I live in City",c,".")
print("Updated dictionary:⤴\n ","I talked about all the things in my dictionary that all are countable to",l)
print()
print("Methods in Dicionary:")
print(my_info.items())
print(my_info.values())
print(my_info.keys())
print(my_info.get("City"))
my_info.clear()
print()


# Dictionary in Python to store country codes
country_code = {
    'India': '+91', 'Pakistan': '+92', 'China': '+86', 'Japan': '+81', 'USA': '+1',
    'UK': '+44', 'Afghanistan': '+93', 'Bangladesh': '+880', 'France': '+33', 'Germany': '+49',
    'Canada': '+1', 'Srilanka': '+94', 'Australia': '+61', 'New Zealand': '+64', 'West Indies': '+1',
    'Russia': '+7', 'Saudi Arab': '+966', 'UAE': '+971', 'South Africa': '+27', 'Turkey': '+90',
    'Spain': '+34', 'Brazil': '+55', 'Italy': '+39', 'Egypt': '+20', 'Indonesia': '+62',
    'Malaysia': '+60', 'Maldives': '+960', 'Thailand': '+66', 'Kuwait': '+965', 'Qatar': '+974',
    'Iran': '+98', 'Iraq': '+964', 'Nepal': '+977', 'Bhutan': '+975', 'Philippines': '+63',
    'Singapore': '+65', 'Vietnam': '+84', 'Myanmar': '+95', 'Norway': '+47', 'Sweden': '+46',
    'Denmark': '+45', 'Switzerland': '+41', 'Netherlands': '+31', 'Belgium': '+32', 'Portugal': '+351',
    'Mexico': '+52', 'Argentina': '+54', 'South Korea': '+82', 'Nigeria': '+234'
}
country = input("Enter your Country: ").strip()
print(f"Country code: {country_code.get(country, 'Not found')}")
print()



# Count the number of repetitions of a specific value in a dictionary
dict = {'Codingal': 8, 'is': 2, 'best': 4, 'for': 3, 'Code': 4, 'year': 4, 'exit': 4}

cnt = 0
rpt = 4
for k in dict:
    if dict[k] == rpt:
        cnt += 1

print(f"The number of repetition is {cnt}")

