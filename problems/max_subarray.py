"""
https://leetcode.com/problems/maximum-subarray/
"""


def maxSubArray(nums: list) -> int:
    if max(nums) <= 0:
        return max(nums)
    nums = [0] + nums
    mx = 0
    for i in range(1, len(nums)):
        nums[i] = max(0, nums[i - 1] + nums[i])
        mx = mx if nums[i] < mx else nums[i]
    return mx


if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(maxSubArray([-2, -5]) == -2)
    print(maxSubArray([-2, 1]) == 1)
