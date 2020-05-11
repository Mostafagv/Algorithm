def fibunacci(N):
    """
   F(0) = 0,   F(1) = 1
   F(N) = F(N - 1) + F(N - 2), for N > 1.
   """

    def helper(N):
        if array[N] != -1:
            return array[N]

        if N < 2:
            array[N] = N
            return array[N]

        array[N] = helper(N - 1) + helper(N - 2)
        return array[N]

    array = [-1 for i in range(N + 1)]
    helper(N)
    return array[-1]


if __name__ == '__main__':
    print(fibunacci(6) == 8)
    print(fibunacci(0) == 0)
    print(fibunacci(1) == 1)
    print(fibunacci(2) == 1)
