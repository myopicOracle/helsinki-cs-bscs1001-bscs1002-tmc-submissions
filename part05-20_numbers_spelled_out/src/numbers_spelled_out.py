# Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words. 

# NB: Please don't formulate each spelled out number by hand. Figure out how you can use loops and dictionaries in your solution.

# ========================


def dict_of_numbers() -> dict:
  ones = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
  teens = [ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
  tens = [ "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]

  my_dictionary = {}
  teens_index = 0

  for i in range(0, 100):

    if i < 10:
      my_dictionary[i] = ones[i]
      
    elif i < 20:
      my_dictionary[i] = teens[teens_index]
      teens_index += 1

    else: # 20-99
      word = ""
      tens_digit = i // 10
      ones_digit = i - (tens_digit * 10)

      if ones_digit == 0:
        word = tens[tens_digit]
        # print(f"At key '{i}', value is '{word}'.")
      else:
        word = f"{tens[tens_digit]}-{ones[ones_digit]}"
        # print(f"At key '{i}', value is '{word}'.")

      my_dictionary[i] = word

  return my_dictionary


# numbers = dict_of_numbers()
# print(numbers)
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])

# ========================

if __name__ == "__main__":
  pass
