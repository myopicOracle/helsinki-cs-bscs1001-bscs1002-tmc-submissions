# Write your solution here

number = int(input("Please type in a number: "))

low = 1
high = number

while low <= high:
    print(low)
    if low != high:
        print(high)
    low += 1
    high -= 1
