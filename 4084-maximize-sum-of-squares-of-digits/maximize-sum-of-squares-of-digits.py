class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        q, r = divmod(sum, 9)
        return "9" * q + str(r) * (r > 0) + "0" * (num - q - (r > 0))