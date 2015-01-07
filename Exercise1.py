ans1 = raw_input("Please enter the first number: ")

while not ans1.isdigit() or ans1 == "0":
    if ans1 == "0":
        ans1 = raw_input("The number has to be greater than 0. Try again: ")
    else:
        ans1 = raw_input("Just numbers please. Enter a number: ")


ans2 = raw_input("Please enter the second number: ")

while not ans2.isdigit() or ans2 == "0":
    if ans2 == "0":
        ans2 = raw_input("The number has to be greater than 0. Try again: ")
    else:
        ans2 = raw_input("Just numbers please. Enter a number: ")

ans1 = int(ans1)
ans2 = int(ans2)

print "The sum of %d and %d is: %d" % (ans1, ans2, ans1 + ans2)

print "The difference of %d and %d is: %d" % (ans1, ans2, ans1 - ans2)

print "The product of %d and %d is: %d" % (ans1, ans2, ans1 * ans2)

print "The quotient of %d and %d is: %d with remainder: %d" % (ans1, ans2, (ans1 / ans2), (ans1 % ans2))



