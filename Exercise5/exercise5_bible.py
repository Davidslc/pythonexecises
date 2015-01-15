import string
import operator
import re
import urllib.request


def remove_punctuation(word):
    parsed_word = re.sub('[!"#$%&()\[\]*+,-./:;<=>?@\^_`{|}~]', '', word)

    if len(parsed_word) > 1:
        if parsed_word[0] == "'":
            parsed_word = parsed_word[1:]
        if parsed_word[-1] == "'":
            parsed_word = parsed_word[0:-2]

    return parsed_word

down_load_file = urllib.request.urlopen('http://www.gutenberg.org/files/10/10.txt').read()
# file = down_load_file.read()
print(down_load_file)
word_count = {}

# for line in file:
#     line = line.split()
#
#     for word in line:
#         word = word.lower()
#         word = remove_punctuation(word)
#
#         if word not in word_count:
#             word_count[word] = 1
#         else:
#             word_count[word] += 1
#
# sorted_list = sorted(word_count.items(), key=operator.itemgetter(1))
# sorted_list.reverse()
#
# for key, value in sorted_list:
#     print("%s ==> %s" % (key, value))
down_load_file.close()
file.close()
print(own_load_file)
print(file.closed)
# print(string.punctuation)

