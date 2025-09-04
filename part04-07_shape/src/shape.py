# Copy here code of line function from previous exercise and use it in your solution
def line(num, string):
    if string == "":
        line = num * "*"
        print(line)
    else:
        line = num * string[0]
        print(line)

def triangle(size, character):
    # You should call function line here with proper parameters
    length = 1
    for i in range (size):
        line(length, character)
        length += 1

def box_of_hashes(width, height, character):
    # You should call function line here with proper parameters
    for i in range(height):
        line(width, character)

def shape(width, char_1, height, char_2):
    triangle(width, char_1)
    box_of_hashes(width, height, char_2)
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")