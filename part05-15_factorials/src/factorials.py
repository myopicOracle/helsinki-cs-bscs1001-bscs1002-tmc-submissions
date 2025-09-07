# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

# ========================

def get_factorial(num: int) -> int:
  num_to_factorial = 1

  for i in range(1, num + 1):
    num_to_factorial *= i

  return num_to_factorial


def factorials(n: int) -> dict:
  first = 1
  last = n

  factorial_dict = {}
  for i in range(first, last + 1):
    factorial_dict[i] = get_factorial(i)

  return factorial_dict


# k = factorials(5)
# print(k)
# print(k[1])
# print(k[3])
# print(k[5])

# ========================
if __name__ == "__main__":
  pass
