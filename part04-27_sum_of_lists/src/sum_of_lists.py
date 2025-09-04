# Write your solution here

def list_sum(a : list, b: list) -> list:
  # print(a, b)
  c = []
  for i in range(len(a)):
    c.append(a[i] + b[i])
  return c

# a = [1, 2, 3]
# b = [7, 8, 9]

# print(list_sum(a,b))

if __name__ == "__main__":
  list_sum([1, 2, 3], [7, 8, 9])