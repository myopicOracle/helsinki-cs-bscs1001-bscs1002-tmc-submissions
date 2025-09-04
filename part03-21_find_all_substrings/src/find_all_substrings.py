# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = word.find(char)

condition = len(word)

while index >= 0 and len(word) > index + 2:
    print(word[index:(index+3)])
    new_word = word[index + 1:]
    word = new_word
    index = word.find(char)


