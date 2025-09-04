# Write your solution here

sentence = ""
stored_word = ""

while True: 

    word = input("Please type in a word: ")

    if word == stored_word or word == "end":
        print(sentence.strip())
        break
    else: 
        sentence += " " + word

    stored_word = word

