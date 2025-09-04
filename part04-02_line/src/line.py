# Write your solution here
def line(num, string):
    if string == "":
        line = num * "*"
        print(line)
    else:
        line = num * string[0]
        print(line)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")