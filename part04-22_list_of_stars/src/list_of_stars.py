# Write your solution here

def list_of_stars(list):
  length = len(list)
  for i in range(length):
    print(list[i]*"*")

# Test Code
if __name__ == "__main__":
  list_of_stars([4,7,2,5,9])
