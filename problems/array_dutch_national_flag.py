"""
Elements of programming interview in python

reorders the array to make all the elements less than or equal to the pivot appear first,
followed by all the elements greater than the pivot.

A = ⟨0, 1, 2, 0, 2, 1, 1⟩ pivot 3
A[3] = 0
⟨0, 0, 1, 2, 2, 1, 1⟩


"""

def dutch_flag_partition(pivot_index, A):
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < A[pivot_index]:
            A[equal],A[smaller] = A[smaller], A[equal]
            smaller, equal = smaller+1, equal+1
        elif A[equal] == A[pivot_index]:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

    print(A)


if __name__ == "__main__":
    dutch_flag_partition(3, [0, 1, 2, 0, 2, 1, 1])
    dutch_flag_partition(1, [0, 1, 2, 0, 2, 1, 1])