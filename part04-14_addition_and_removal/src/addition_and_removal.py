# Write your solution here
# Sample output

# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: r
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: x
# Bye!

my_list = []
print(f"The list is now {my_list}")

num = 1

while True:
  command = input("a(d)d, (r)emove or e(x)it: ")
  if command == "d":
    my_list.append(num)
    num += 1
    print(f"The list is now {my_list}")
  elif command == "r":
    my_list.pop(-1)
    num -= 1
    print(f"The list is now {my_list}")
  elif command == "x":
    print("Bye!")
    break
  else:
    print("Please enter d, r, or x only.")
  
