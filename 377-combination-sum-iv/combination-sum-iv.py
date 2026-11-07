class Solution:
    def combinationSum4(self, nums, target):
        d = [1] + [0] * target
        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    d[i] += d[i - x]
        return d[target]