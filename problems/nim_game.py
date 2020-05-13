def canWinNim(n: int) -> bool:
    """

    """
    if n < 4:
        return True
    mat = [0 for i in range(n + 1)]
    for i in range(4):
        mat[i] = 1

    for i in range(4, n + 1):
        mat[i] = max(1 - mat[i - 1], 1 - mat[i - 2], 1 - mat[i - 3])
    # print(mat)
    return mat[-1]


if __name__ == '__main__':
    print(canWinNim(6) == 1)
    print(canWinNim(8) == 0)