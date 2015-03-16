"""Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes
the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""


def near_hundred(n):
    return n > 189 and n < 211 or n > 89 and n < 111


print(near_hundred(211))