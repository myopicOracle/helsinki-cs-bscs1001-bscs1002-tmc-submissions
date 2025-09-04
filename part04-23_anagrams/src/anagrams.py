# Write your solution here

def anagrams(str1, str2):
#   print(str1)
#   print(str2)
  a = sorted(str1)
#   print(a)
  b = sorted(str2)
#   print(b)
  if a == b:
    return True
  else:
    return False

if __name__ == "__main__":
  print(anagrams("team", "mate"))