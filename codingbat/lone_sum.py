"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""


def lone_sum(a, b, c):
    sum = a + b + c
    if a == b and a == c:
        return 0
    elif a == b:
        return sum - (a + b)
    elif a == c:
        return sum - (a + c)
    elif b == c:
        return sum - (b + c)
    else:
        return sum

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))