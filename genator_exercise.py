"""
Write a generator function that will return a sequence of floating point numbers

Call the function frange and have it take 3 parameters - start, stop and increment.  Assuming I pass 0, 4 and .5 as
the 3 parameters, I should see output like:

0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
"""

def frange(start, stop, increment):


    while start < stop:
        yield start
        start += increment

for n in frange(0, 4, 0.5):
    print(n)