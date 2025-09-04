# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

count_of = 0
sum_of = 0
negatives = 0
positives = 0

while True:
    num = int(input("Number: "))
    sum_of += num

    print("Number: ", num)
    if num == 0:
        break

    count_of += 1

    if num > 0:
        positives += 1
        print("positives", positives)
    else:
        negatives += 1
        print("negatives", negatives)
        
print(f"Numbers typed in {count_of}")
print(f"The sum of the numbers is {sum_of}")
print(f"The mean of the numbers is {round((sum_of / count_of),2)}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
