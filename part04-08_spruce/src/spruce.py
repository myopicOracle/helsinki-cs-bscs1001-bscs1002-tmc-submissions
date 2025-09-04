# Write your solution here

#     *  -- line 1, space 4+4, chars 1
#    ***  -- line 2, space 3+3, chars 3
#   *****  -- line 3, space 2+2, chars 5
#  *******  -- line 4, space 1+1, chars 7
# *********  -- line 5, space 0+0, chars 9
#     *

# Follows format 
## leaves and branches -- [left space] + [left chars] + [1 center char] + [right chars] + [right space]
## trunk -- [left space] + [1 center char] + [right space]

# variables needed: 
# height, current_line_number, fixed_char, variable_chars, padding


def spruce(height):
    print("a spruce!")
    for i in range(height):
        current_line = i + 1
        padding_length = int(( height - current_line ))
        # print("Log value of 'padding_length': ", padding_length)
        padding = padding_length * " "
        # print("Log value of 'padding': ", padding)
        var_length = int(( current_line - 1 ))
        # print("Log value of 'var_length': ", var_length)
        var = var_length * "*"
        # print("Log value of 'var': ", var)
        fixed = "*"
        leaves_and_branches = padding + var + fixed + var + padding
        print (leaves_and_branches)
    trunk_padding = (height - 1) * " "
    # print("Log value of 'trunk_padding': ", trunk_padding)
    tree_trunk = trunk_padding + "*" + trunk_padding
    print(tree_trunk)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)