"""Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""


def first_half(str):
    half_str = len(str) / 2
    first_part = str[:-int(half_str)]
    return first_part

print(first_half('HelloThere'))