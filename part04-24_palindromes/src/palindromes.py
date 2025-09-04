# Write your solution here
# Note, that at this time the main program should not be written inside

# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!

# def palindromes(string):
#   print("string: ", string)
#   print("string[::-1]: ", string[::-1])
#   print("list(reversed(string)): ", list(reversed(string)))
#   print("string[::-1]: ", string[::-1])
#   asc = list(string)
#   print("asc: ", asc)
#   desc = asc[::-1]
#   print("desc: ", desc)
#   if asc == desc:
#     return True
#   else: 
#     return False
  
def palindromes(string):
  return string == string[::-1]

# print(palindromes("neverod00045doreven"))

while True:
  user_input = input("Please type in a palindrome: ")
  if palindromes(user_input):
    print(f"{user_input} is a palindrome!")
    break
  else:
    print("that wasn't a palindrome")

if __name__ == "__main__":
  palindromes("neveroddoreven")
