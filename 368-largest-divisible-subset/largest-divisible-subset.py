class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        d = [1] * n
        p = [-1] * n
        b = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and d[j] + 1 > d[i]:
                    d[i] = d[j] + 1
                    p[i] = j
            if d[i] > d[b]:
                b = i
        r = []
        while b >= 0:
            r.append(nums[b])
            b = p[b]
        return r