# Write your solution here

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
op = input("Operation: ")

add = op == "add"
# print(add)

multiply = op == "multiply"
# print(multiply)

subtract = op == "subtract"
# print(subtract)

# if op == "add":
if add:
    print(f"{num1} + {num2} = {num1 + num2}")
# if op == "multiply":
elif multiply:
    print(f"{num1} * {num2} = {num1 * num2}")
# if op == "subtract":
elif subtract:
    print(f"{num1} - {num2} = {num1 - num2}")
else:
    pass

