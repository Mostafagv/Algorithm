"""
source : https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

0-1 Knapsack Problem | DP-10
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum
total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
which represent values and weights associated with n items respectively. Also given an integer W
which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the
weights of this subset is smaller than or equal to W. You cannot break an item, either pick the
complete item, or don’t pick it (0-1 property).

weight = 10, val = 60
weight = 20, val = 100
weight = 30, val = 120
W = 50
"""

# weight = [10, 20, 30]
# value = [60, 100, 120]
# W = 50


def knapsack(weight, value, W):
    def helper(w, v, remain_w, reward):
        if len(w) == 1:
            return reward+v[0] if w[0] <= remain_w else reward
        rp = 0
        if remain_w-w[0]>0:
            # pick item
            rp = helper(w[1:], v[1:], remain_w-w[0], reward+v[0]) + reward
        # do not pick
        rd = helper(w[1:], v[1:], remain_w, reward)
        return max(rd, rp)

    if len(weight) == 0:
        return 0
    r = helper(weight, value, W, 0)
    return r


if __name__ == "__main__":
    print('test 1: ', knapsack([10], [10], 5) == 0)
    print('test 2: ', knapsack([10], [10], 20) == 10)
    print('test 3: ', knapsack([10, 20], [10, 20], 20) == 20)
    print('test 4: ', knapsack([10, 20], [10, 20], 30) == 30)
    print('test 5: ', knapsack([], [], 30) == 0)
    print('test 6: ', knapsack([10, 20, 30], [60, 100, 120], 50) == 220)
    print('test 7: ', knapsack([0], [0], 30) == 0)

