# Ask The User For Their Information
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

# Store In Dictionary
person_info = {"Name": name, "Hometown": hometown}

if age.isdigit():
    person_info["Age"] = int(age)
else:
    print("Enter a valid age")

# Print Only The Available Information
for key in person_info:
    print(person_info[key], sep="\n")

