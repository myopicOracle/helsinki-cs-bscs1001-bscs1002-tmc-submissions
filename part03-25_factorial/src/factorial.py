# Write your solution here

while True: 
    num = int(input("Please type in a number: "))

    factorial = num

    if num > 0:

        for i in range(1, num):
            # print(i)
            factorial *= i
            # print(factorial)

        print(f"The factorial of the number {num} is {factorial}")

    else: 
        print("Thanks and bye!")
        break
    