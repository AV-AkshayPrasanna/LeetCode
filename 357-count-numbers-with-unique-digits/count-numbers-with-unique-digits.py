class Solution:
    def countNumbersWithUniqueDigits(self, n):
        r, p, a = 1, 9, 9
        for _ in range(min(n, 10)):
            r += p
            p *= a
            a -= 1
        return r