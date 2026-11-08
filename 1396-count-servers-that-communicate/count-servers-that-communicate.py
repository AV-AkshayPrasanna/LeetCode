class Solution:
    def countServers(self, grid):
        r = [sum(x) for x in grid]
        c = [sum(x) for x in zip(*grid)]
        return sum(1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] and (r[i] > 1 or c[j] > 1))