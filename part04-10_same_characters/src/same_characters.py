# Write your solution here

def same_chars(string, a, b):
    if a < 0 or a > len(string) - 1 or b < 0 or b > len(string) - 1:
        return False
    else: 
        # print("string[a]: ", string[a], " | ", "string[b]: ", string[b])
        return string[a] == string[b]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 5))
    # print(same_chars("abc", 0, 3))