class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        b = float("inf")
        for i in range(n):
            s = 0
            for j in range(i, min(n, i + r)):
                s += nums[j]
                if j - i + 1 >= l and 0 < s < b:
                    b = s
        return -1 if b == float("inf") else b