"""
https://leetcode.com/problems/maximum-product-subarray/
        	    2	1	-2	4	-2
            2	2	2	-4	-16	32
            1		1	-2	-8	16
            -2			-2	-8	16
            4				4	-8
            -2					-2


second approach
	2	1	-2	4	-2
max	2	2	-2	4	32
min	2	1	-4	-16	-8
"""


def maxProduct(nums):
    mat = [[0 for i in range(len(nums))] for j in range(len(nums))]
    mx_ = float('-inf')
    for i in range(len(nums)):
        mat[i][i] = nums[i]
        if nums[i] > mx_:
            mx_ = nums[i]

    for c in range(1, len(nums)):
        for r in range(c):
            mat[r][c] = mat[r][c - 1] * nums[c]
            if mat[r][c] > mx_:
                mx_ = mat[r][c]
    return mx_


def maxProductII(nums):
    mat = [[0 for i in range(len(nums))] for j in range(2)]
    mat[0][0], mat[1][0] = nums[0], nums[0]
    mx_ = nums[0]

    for i in range(1, len(nums)):
        mat[0][i] = max(mat[0][i - 1] * nums[i], mat[1][i - 1] * nums[i], nums[i])
        mx_ = mx_ if mat[0][i] < mx_ else mat[0][i]
        mat[1][i] = min(mat[0][i - 1] * nums[i], mat[1][i - 1] * nums[i], nums[i])
        mx_ = mx_ if mat[1][i] < mx_ else mat[0][i]

    return mx_



if __name__ == "__main__":
    assert maxProduct([2, 3, -2, 4]) == 6
    assert maxProduct([2, 3, -2, 4, -2]) == 96
    assert maxProduct([2, 0, -2, 4, -2]) == 16

    assert maxProductII([2, 3, -2, 4]) == 6
    assert maxProductII([2, 3, -2, 4, -2]) == 96
    assert maxProductII([2, 0, -2, 4, -2]) == 16
