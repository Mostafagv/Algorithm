"""
Elements of programming interview in python

A string is a sequence of characters. A string may encode an integer, e.g., “123” encodes 123.
In this problem, you are to implement methods that take a string representing an integer and return
the corresponding integer, and vice versa. Your code should handle negative integers.
"""

def string_to_int(s):
    dict_ = {'1': 1
        , '2': 2
        , '3': 3
        , '4': 4
        , '5': 5
        , '6': 6
        , '7': 7
        , '8': 8
        , '9': 9
        , '0': 0
             }
    if len(s) == 1:
        return dict_[s]
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]

    return -1 * (dict_[s[-1]]+string_to_int(s[:-1])*10) if is_negative else dict_[s[-1]]+string_to_int(s[:-1])*10

if __name__ == '__main__':
    print(string_to_int('1234'))
    print(string_to_int('-1234'))