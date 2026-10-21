class Solution:
    def integerBreak(self, n: int) -> int:
        # Small cases: must split into at least 2 parts
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Use as many 3s as possible
        q, r = divmod(n, 3)
        if r == 0:
            return 3 ** q
        if r == 1:
            # Replace one 3 + 1 with 2 + 2 (4 > 3 * 1)
            return 3 ** (q - 1) * 4
        return 3 ** q * 2