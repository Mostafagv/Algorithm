"""
Elements of programming interview in python

Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
"""


def even_odd(A):
    p_even, p_odd = 0, len(A)-1
    while p_even < p_odd:
        if A[p_even] % 2 == 0:
            p_even += 1
        else:
            A[p_even], A[p_odd] = A[p_odd], A[p_even]
            p_odd -= 1
    return A


if __name__ == "__main__":
    print("test 1: ", even_odd([1, 2, 3, 4]) == [4, 2, 3, 1])
    print("test 1: ", even_odd([1, 2, 4, 3]) == [4, 2, 3, 1])

