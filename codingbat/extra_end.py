"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""


def extra_end(str):
    if len(str) > 1:
        str_end = str[-2:]
        return str_end * 3
    else:
        return "Your string needs to be at least 2 characters! Try again."

print(extra_end('Happy'))