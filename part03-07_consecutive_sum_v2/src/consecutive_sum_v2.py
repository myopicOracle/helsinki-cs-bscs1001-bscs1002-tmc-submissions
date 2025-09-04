# Write your solution here

limit = int(input("Limit: "))

num = 1
sum = 0
statement = f"{num} "
new = f""

while sum < limit:
    # print("num_t0: ", num)
    sum += num
    # print("sum: ", sum)
    num += 1
    # print("num_t1: ", num)
    # print("--------------")
    statement = f"The consecutive sum: 1 {new}= {sum}"
    new += f"+ {num} "


print(statement)
