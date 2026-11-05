class Solution:
    def getMoneyAmount(self, n):
        d = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(2, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                d[i][j] = min(k + max(d[i][k - 1], d[k + 1][j]) for k in range(i, j))
        return d[1][n]