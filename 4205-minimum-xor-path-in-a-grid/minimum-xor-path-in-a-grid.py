class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        d = [[set() for _ in range(n)] for _ in range(m)]
        d[0][0].add(grid[0][0])
        for i in range(m):
            for j in range(n):
                for p in ((i - 1, j), (i, j - 1)):
                    if p[0] >= 0 and p[1] >= 0:
                        for x in d[p[0]][p[1]]:
                            d[i][j].add(x ^ grid[i][j])
        return min(d[-1][-1])