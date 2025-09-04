# Write your solution here

def squared(text, size):
    for row_number in range(size):
        result = ""
        for column_number in range(size):
            character_position = row_number * size + column_number
            character_index = character_position % len(text)
            character = text[character_index]
            result = result + character
        print(result)

# squared("aybabtu", 5)