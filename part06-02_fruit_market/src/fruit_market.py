# The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:

    # banana;6.50
    # apple;4.95
    # orange;8.0
    # ...etc...

# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.

# ========================

def read_fruits() -> dict:

  with open("fruits.csv") as new_file:
    fruit_dict = {}

    for line in new_file:
      line = line.replace("\n", "")
      # print("line: ", line)
      item = line.split(";")
      name = (item[0])
      price = float(item[1])
      # print("name: ", name)
      # print("price: ", price)
      fruit_dict[name] = price
      # print("Fruit dict is now: ", fruit_dict)

    return fruit_dict

# print(read_fruits())

# ========================

if __name__ == "__email__":
  read_fruits()