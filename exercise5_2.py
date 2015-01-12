
file = open('exercise5_book.txt', 'r+', encoding="utf-8-sig")


word_count = {}

for word in file.read().split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

for key, value in word_count.items():
    print("%s ==> %s" % (key, value))

file.close()
print(file.closed)
