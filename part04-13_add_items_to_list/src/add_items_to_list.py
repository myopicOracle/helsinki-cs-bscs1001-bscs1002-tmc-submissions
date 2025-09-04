# Write your solution here

def add_items_to_list():
  my_list = []
  num_items = int(input("How many items: "))
  for i in range(num_items):
    item = int(input(f"Item {i + 1}: "))
    my_list.append(item)
  return my_list

print(add_items_to_list())