"""Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(str):
    if len(str) < 2:
        return str
    else:
        back_str = str[-1]
        middle_str = str[1:-1]
        front_str = str[0]
        return back_str + middle_str + front_str

print(front_back('ab'))
