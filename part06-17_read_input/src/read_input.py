# Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function. The function should return the final valid integer value typed in by the user.

# An example of the function in action:

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)

# Sample output

# Please type in a number: seven
# You must type in an integer between 5 and 10
# Please type in a number: -3
# You must type in an integer between 5 and 10
# Please type in a number: 8
# You typed in: 8

# ========================

def read_input(instructions: str, lower_bound: int, upper_bound: int) -> int:

  error_message = f"You must type in an integer between {lower_bound} and {upper_bound}"

  while True:

    try:
      user_input = int(input(instructions))

      if user_input > lower_bound and user_input < upper_bound:
        return user_input
    
    except ValueError:
      pass

    print(error_message)
    

# number = read_input("Please type in a number: ", 5, 10) # testing
# print("You typed in:", number) # testing
  

# ========================

if __name__ == "__main__":
  pass
