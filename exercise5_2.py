import string
import operator
import re

# remove the punctuation except for the single quote
def remove_punctuation(word):
    parsed_word = re.sub('[!"#$%&()\[\]*+,-./:;<=>?@\^_`{|}~]', '', word)

# remove the single quote before and after a word
    if len(parsed_word) > 1:
        if parsed_word[0] == "'":
            parsed_word = parsed_word[1:]
        if parsed_word[-1] == "'":
            parsed_word = parsed_word[0:-2]

    return parsed_word

file = open('bible.txt', 'r', encoding="utf-8-sig")


word_count = {}

for line in file:
    line = line.split()

    for word in line:
        word = word.lower()
        word = remove_punctuation(word)

        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

sorted_list = sorted(word_count.items(), key=operator.itemgetter(1))
sorted_list.reverse()

for key, value in sorted_list:
    print("%s ==> %s" % (key, value))

file.close()
print(file.closed)
#print(string.punctuation)
