# Write your solution here

num1 = float(input("How many times a week do you eat at the student cafeteria? "))
num2 = float(input("The price of a typical student lunch? "))
num3 = float(input("How much money do you spend on groceries in a week? "))

total = (num1 * num2) + num3

print(f"""Average food expenditure:
Daily: {total / 7} euros
Weekly: {total} euros""")