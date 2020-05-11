"""
Elements of programming interview in python

A palindromic string is one which reads the same when it is reversed.
"""

def is_palindromic(s):
    t = True
    for i in range(len(s)//2):
        t = t and (s[i] == s[len(s)-1-i])
    return t
if __name__ == "__main__":
    print(is_palindromic('cabac')==True)
    print(is_palindromic('caac')==True)
    print(is_palindromic('caad')==False)