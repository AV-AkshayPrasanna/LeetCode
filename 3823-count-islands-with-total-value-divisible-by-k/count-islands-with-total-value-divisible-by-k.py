class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        r = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    s = 0
                    st = [(i, j)]
                    s += grid[i][j]
                    grid[i][j] = 0
                    while st:
                        x, y = st.pop()
                        for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0 <= a < m and 0 <= b < n and grid[a][b]:
                                s += grid[a][b]
                                grid[a][b] = 0
                                st.append((a, b))
                    if s % k == 0:
                        r += 1
        return r