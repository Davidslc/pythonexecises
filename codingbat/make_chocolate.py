"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be
done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
make_chocolate(4, 1, 4) → 4
make_chocolate(6, 2, 7) → 2
make_chocolate(1, 2, 7) → -1
"""


def make_chocolate(small, big, goal):
    big = big * 5
    total = big + small

    while big > goal and small < goal:
        big = big - 5
        if big < goal and small + big < goal:
            return -1

    if big > goal and small >= goal:
        return small - (small - goal)

    elif total >= goal:
        return goal - big
    return -1

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
print(make_chocolate(4, 1, 4))
print(make_chocolate(6, 2, 7))
print(make_chocolate(1, 2, 7))
