from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        r = -float("inf")
        for i in range(n):
            a = [0] * m
            for j in range(i, n):
                for x in range(m):
                    a[x] += matrix[x][j]
                s = [0]
                c = 0
                for v in a:
                    c += v
                    p = bisect_left(s, c - k)
                    if p < len(s):
                        r = max(r, c - s[p])
                    insort(s, c)
        return r