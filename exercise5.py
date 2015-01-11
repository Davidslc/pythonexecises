from string import ascii_letters
from random import choice
from random import randint

# to clear file
with open('exercise_five.dat', 'w') as clear:
    clear.write("")

# generate a random string of random length
def generate_random_string():

    random_number = randint(0, 61)

    random_letters = ""

    for letter in range(0, random_number):
        random_letter = choice(ascii_letters)
        random_letters += random_letter

# print the random strings to a file, line by line
    print(random_letters)
    with open('exercise_five.dat', 'a+') as f:
        f.write(random_letters + "\n")

# count the number of each letter
    count = {}
    for character in random_letters:
        count[character] = count.get(character, 0) + 1

# format and print the count
    for key, value in count.items():
        print("%s ==> %s" % (key, value))

# create 10 lines of random strings of random length
for i in range(0, 10):
    generate_random_string()
