class Solution:
    def longestMonotonicSubarray(self, nums):
        u = d = r = 1
        for i in range(1, len(nums)):
            u = u + 1 if nums[i] > nums[i - 1] else 1
            d = d + 1 if nums[i] < nums[i - 1] else 1
            r = max(r, u, d)
        return r