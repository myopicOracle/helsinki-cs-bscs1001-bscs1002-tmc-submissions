# Write your solution here

while True: 

    string = input("Please type in a string: ")

    char = "-"
    repeat = len(string)

    if string == "":
        break

    print(string)
    print(char * repeat)