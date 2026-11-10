class Solution:
    def climbStairs(self, n, costs):
        d = [0] + [float("inf")] * n
        for j in range(1, n + 1):
            for k in (1, 2, 3):
                if j - k >= 0:
                    d[j] = min(d[j], d[j - k] + costs[j - 1] + k * k)
        return d[n]