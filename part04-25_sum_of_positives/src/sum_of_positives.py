# Write your solution here

def sum_of_positives(list: list) -> int:
  positives_in_list = []
  for i in list:
    if i > 0:
      positives_in_list.append(i)
      # print(positives_in_list)
  # print(positives_in_list)
  return sum(positives_in_list)

# print(sum_of_positives([12, -7, 34, -21, 0, 8, -15, 27, -3, 19, -42, 6, -9, 31, -25, 14, -1, 23, -17, 5]))

if __name__ == "__main__":
  sum_of_positives([12, -7, 34, -21, 0, 8, -15, 27, -3, 19, -42, 6, -9, 31, -25, 14, -1, 23, -17, 5])