""" Write a script that tries to open a file that does not exist. Create a function that takes
a file name, tries to open a file with that name, but does not handle the exception in
the function. Instead, handle it in the code that calls the function.

• Copy your code and modify it so that the exception is handled in the function itself
rather than in the calling code (that is, the code which calls the function).

• Summary:

1. Create a function that takes a file name as a parameter
2. Create a second function that also takes a file name as a parameter
3. In your main script, make a call to both functions
4. One function should handle the exception that will be raised
5. The other function should NOT handle the exception (which means that your
main script must handle it)
"""

# a function that takes a file name as a parameter
def open_file(file_name):
    try:
        with open(file_name, "r") as f:
            print(f.read())
    except:
        print("I can't find: " + file_name)

# second function that also takes a file name

def open_file_two(file_name_two):
    with open(file_name_two, "r") as f_two:
                print(f_two.read())



# open_file("bubble.txt")

try:
    open_file("bubble.txt")
    open_file_two("exercise5_bok.txt")

except:
    print("That isn't in this directory")

