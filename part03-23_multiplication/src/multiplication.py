# Write your solution here

num = int(input("Please type in a number: "))

operand_1 = 1
operand_2 = 1

while operand_1 <= num:
    while operand_2 <= num:
        print(f"{operand_1} x {operand_2} = { operand_1 * operand_2 }")
        operand_2 += 1
    operand_2 = 1
    # print(f"{operand_1} * {operand_2} = { operand_1 * operand_2 }")
    operand_1 += 1