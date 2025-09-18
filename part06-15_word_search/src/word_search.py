# The exercise template includes the file words.txt, which contains words in English.

# Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.

# The search term may include lowercase letters and the following wildcard characters:

#     A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
#     An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane. There can only ever be a single asterisk in the search term.
#     If there are no wildcard characters in the search term, only words which match the search term exactly are returned.

# You may assume both wildcards are never used in the same search term.

# The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.

# If no matching words are found, the function should return an empty list.

# Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search for more information about them online.

# An example of the function in action:

# print(find_words("*vokes"))

# Sample output

# ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']

# ========================

def read_file(file_name: str) -> list:
  word_list = []

  with open(file_name) as new_file:
    for line in new_file:
      word = line.strip()
      word_list.append(word)

  return word_list


def find_words(search_term: str) -> list:
  word_list = read_file("words.txt")
  filtered_words = []

  if search_term.startswith("*"):
    for word in word_list:
      if word.endswith(search_term[1:]):
        filtered_words.append(word)
      else:
        continue

  elif search_term.endswith("*"):
    for word in word_list:
      if word.startswith(search_term[:-1]):
        filtered_words.append(word)
      else:
        continue

  elif "." in search_term:
    for word in word_list:
      if len(search_term) != len(word):
        continue
      else:
        condition = True
        for i in range(len(word)):
          if search_term[i] == ".":
            continue
          else:
            if search_term[i] == word[i]:
              continue
            else:
              condition = False
        if condition:
          filtered_words.append(word)
        else:
          continue

  else:
    for word in word_list:
      if word == search_term:
        filtered_words.append(word)
      else:
        continue

  # print(filtered_words) # debugger
  return filtered_words


# find_words("ca.") # testing


# Test cases

# result = find_words("ca.")
# print(f'find_words("ca."): {result} \n==========================\n')

# result = find_words("c.d.")
# print(f'find_words("c.d."): {result} \n==========================\n')

# result = find_words("a...e")
# print(f'find_words("a...e"): {result} \n==========================\n')

# result = find_words("reson*")
# print(f'find_words("reson*"): {result} \n==========================\n')

# result = find_words("*okes")
# print(f'find_words("*okes"): {result} \n==========================\n')


# ========================

if __name__ == "__main__":
  pass
