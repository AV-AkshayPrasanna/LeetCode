from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            longest = 1

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))

            return longest

        return max(dfs(r, c) for r in range(m) for c in range(n))