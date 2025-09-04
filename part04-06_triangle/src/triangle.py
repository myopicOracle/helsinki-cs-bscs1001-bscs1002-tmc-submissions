# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        line = num * "*"
        print(line)
    else:
        line = num * string[0]
        print(line)

def triangle(size):
    # You should call function line here with proper parameters
    characters = 1
    for i in range (size):
        line(characters, "#")
        characters += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
