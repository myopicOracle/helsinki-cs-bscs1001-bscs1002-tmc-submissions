# Write your solution here

string = input("Please type in a string: ")
substring = ["a","e","o"]

for i in range(0,len(substring)):
    condition = substring[i] in string
    value_if_true = f"{substring[i]} found"
    value_if_false = f"{substring[i]} not found"
    print(value_if_true if condition else value_if_false)

# substring = "a"
# condition = substring in string
# value_if_true = f"{substring} found"
# value_if_false = f"{substring} not found"
# print(value_if_true if condition else value_if_false)

# substring = "e"
# condition = substring in string
# print(value_if_true if condition else value_if_false)

# substring = "o"
# condition = substring in string
# print(value_if_true if condition else value_if_false)
