# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

index_of_char = word.find(char)

if index_of_char >= 0 and len(word) > index_of_char + 2:
    print(word[index_of_char:(index_of_char+3)])

