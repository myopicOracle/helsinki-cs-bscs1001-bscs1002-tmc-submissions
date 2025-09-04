# Write your solution here

print("Person 1:")
name_1 = input("Name: ")
age_1 = int(input("Age: "))
print("Person 2:")
name_2 = input("Name: ")
age_2 = int(input("Age: "))

if age_1 > age_2:
    print(f"The elder is {name_1}")
elif age_1 < age_2:
    print(f"The elder is {name_2}")
else:
    print(f"{name_1} and {name_2} are the same age")
