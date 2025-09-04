# Write your solution here
import math

num1 = int(input("How many students on the course? "))
num2 = int(input("Desired group size? "))

print(f"Number of groups formed: {math.ceil(num1 / num2)}")