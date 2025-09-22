# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. Please see the example below.
# Sample output

# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt

# The contents of the file inscribed.txt would be
# Sample data

# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

# ========================

# user_input_name = "Ada" # testing
# user_input_file = "inscribed.txt" # testing
user_input_name = input("Whom should I sign this to: ")
user_input_file = input("Where shall I save it: ")

with open(user_input_file, "w") as my_file:
  my_file.write(f"Hi {user_input_name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


# ========================

if __name__ == "__main__":
  pass
