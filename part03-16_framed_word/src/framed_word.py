# Write your solution here

word = input("Word: ")

char = "*"
space = " "
fill = 30 - len(word)

alpha = 0
omega = 0

if len(word) % 2 == 0:
    half = fill // 2
    alpha = half - 1
    omega = half - 1
    # print(len(word))
    # print(fill)
    # print(alpha)
    # print(omega)
else:
    half = fill // 2
    alpha = half - 1
    omega = half - 0
    # print(len(word))
    # print(fill)
    # print(alpha)
    # print(omega)

print("******************************")
print(f"{char}{space * alpha}{word}{space * omega}{char}")
print("******************************")