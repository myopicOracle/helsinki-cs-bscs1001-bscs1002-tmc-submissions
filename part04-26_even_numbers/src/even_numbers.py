# Write your solution here

def even_numbers(my_list):
  evens_in_list = []
  for i in my_list:
    if i % 2 == 0:
      evens_in_list.append(i)
      print(evens_in_list)
  print(evens_in_list)
  return(evens_in_list)

# print(even_numbers([12, -7, 34, -21, 0, 8, -15, 27, -3, 19, -42, 6, -9, 31, -25, 14, -1, 23, -17, 5]))

if __name__ == "__main__":
  even_numbers([12, -7, 34, -21, 0, 8, -15, 27, -3, 19, -42, 6, -9, 31, -25, 14, -1, 23, -17, 5])
  