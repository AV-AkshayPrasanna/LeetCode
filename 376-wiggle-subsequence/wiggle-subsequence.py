class Solution:
    def wiggleMaxLength(self, nums):
        u = d = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                u = d + 1
            elif nums[i] < nums[i - 1]:
                d = u + 1
        return max(u, d)