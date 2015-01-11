from sys import exit


def menu():
# this is the menu
    print '*' * 25
    print "EXERCISE 4 - MENU"
    print '*' * 25
    print "1. Write input to file"
    print "2. Write input to screen"
    print "3. Quit"
    print '*' * 25
    print ""

    choice = raw_input("Enter your choice [1-3] : ")
    choice = choice.lower()

# three choices are asked for. Except for the 3rd choice to exit, choices 1 or 2 are executed.
    while choice != "3" or choice != "three" or choice != "quit":

        if choice == "2" or choice == "two":
            choice2 = raw_input("Enter a phrase: ")
            print "You entered: " + "'" + choice2 + "'\n"
            menu()

        elif choice == "1" or choice == "one":
            choice1 = raw_input("Enter a phrase: ")
            print "You entered: " + "'" + choice1 + "'\n"
            with open('exercise4.txt', 'w') as f:
                f.write(choice1)
            menu()

        elif choice == "3" or choice == "three" or choice == "quit":
            print "\nGood bye"
            exit()

        else:
            print "\nThat's not a choice. Try again.\n"
            menu()

menu()






