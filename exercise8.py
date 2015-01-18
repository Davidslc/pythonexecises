from time import clock

# This function generates fibonacci numbers using recursion. This first one isn't efficient.
def fib_naive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_naive(n-1) + fib_naive(n-2)

# This second function (combination of fib_helper and fib_improved) is much more efficient.
def fib_helper(n):
    if n == 0:
        return
    else:
        return fib_improved(n, 0, 1)

def fib_improved(n, p0, p1):
        if n == 1:
            return p1
        else:
            return fib_improved(n-1, p1, p0 + p1)


# This for loop compares both functions, measuring the run time of each.
for num in range(0, 41):
    start = clock()
    result = fib_naive(num)
    stop = clock()
    difference = (stop - start) * 1000  # clock returns a value in seconds.
    print("fib_naive (%s) = %s taking %.1fms" % (num, result, difference))

    start = clock()
    result2 = fib_helper(num)
    stop = clock()
    difference = (stop - start) * 1000  # clock returns a value in seconds.
    print("fib_improved (%s) = %s taking %.1sms\n" % (num, result2, difference))


