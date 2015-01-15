# a function that takes a file name as a parameter

def open_file(file_name):
    try:
        with open(file_name, "r") as f:
            f.read(file_name)
    except:
        print("I can't find: " + file_name)

# second function that also takes a file name

def open_file_two(file_name_two):
    with open(file_name, "r") as f:
            f.read(file_name_two)



try:
    open_file_two("snow.txt")
except:
    print("Sorry, but I can't find file: " + file_name_two)

open_file("blah.txt")

