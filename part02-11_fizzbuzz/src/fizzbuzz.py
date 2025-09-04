# Write your solution here

num = int(input("Number: "))

three = (num % 3) == 0
five = (num % 5) == 0

if three and five:
    print("FizzBuzz")
elif three:
    print("Fizz")
elif five:
    print("Buzz")
else:
    print("")