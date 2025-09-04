# Write your solution here

f = int(input("Please type in a temperature (F):"))

c = (f - 32) * 5/9

print(f"{f} degrees Fahrenheit equals {c} degrees Celsius")

if c < 0:
    print("Brr! It's cold in here!")
