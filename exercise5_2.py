import string


file = open('exercise5_book.txt', 'r', encoding="utf-8-sig")

removed_characters = file.

word_count = {}

# print(file.read())
for line in file:
    line = line.split()

    for word in line:
        word = word.lower()
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

for key, value in word_count.items():
    print("%s ==> %s" % (key, value))

file.close()
print(file.closed)
print(string.punctuation)
