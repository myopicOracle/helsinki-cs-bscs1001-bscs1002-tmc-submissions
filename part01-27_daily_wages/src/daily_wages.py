# Write your solution here

wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ").strip().lower()

double = "sunday"

if day == double:
    print(f"Daily wages: {wage * 2 * hours} euros")
else:
    print(f"Daily wages: {wage * hours} euros")