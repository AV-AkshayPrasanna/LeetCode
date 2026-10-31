class Solution:
    def uniquePaths(self, grid):
        M = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]
        R[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    D[i + 1][j] = (D[i + 1][j] + R[i][j]) % M
                    R[i][j + 1] = (R[i][j + 1] + D[i][j]) % M
                else:
                    t = (R[i][j] + D[i][j]) % M
                    if i == m - 1 and j == n - 1:
                        return t
                    R[i][j + 1] = (R[i][j + 1] + t) % M
                    D[i + 1][j] = (D[i + 1][j] + t) % M