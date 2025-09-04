# Write your solution here

# limit = int(input("Limit: "))

# prev = 0
# num = 0

# while num < 10:
#     prev = num 
#     print("prev: ", prev)
#     num += 1
#     print("num: ", num)
#     sum = prev + num
#     print("sum: ", sum)
#     print("--------------")

# print(sum)

limit = int(input("Limit: "))

num = 0
sum = 0

while sum < limit:
    num += 1
    # print("num: ", num)
    sum += num
    # print("sum: ", sum)
    # print("--------------")

print(sum)
