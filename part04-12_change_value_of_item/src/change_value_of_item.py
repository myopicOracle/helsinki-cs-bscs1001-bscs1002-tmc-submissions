# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
  index = int(input("Index: "))
  if index == -1:
    break
  new_value = int(input("New Value: "))
  new_list = my_list
  new_list[index] = new_value
  print(new_list)