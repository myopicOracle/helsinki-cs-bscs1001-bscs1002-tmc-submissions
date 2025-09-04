# Write your solution here

argument = int(input("How many days?"))

days = 365
hours = 24
minutes = 60
seconds = 60

output = argument * hours * minutes * seconds

print(f"Seconds in that many days: {output}")