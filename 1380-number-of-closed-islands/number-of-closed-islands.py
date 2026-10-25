class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        def f(i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            if grid[i][j]:
                return 1
            grid[i][j] = 1
            a = f(i+1, j)
            b = f(i-1, j)
            c = f(i, j+1)
            d = f(i, j-1)
            return a & b & c & d
        return sum(f(i, j) for i in range(m) for j in range(n) if not grid[i][j])