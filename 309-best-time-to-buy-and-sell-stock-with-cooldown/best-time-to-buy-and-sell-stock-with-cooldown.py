from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold

            hold = max(hold, rest - price)
            sold = prev_hold + price
            rest = max(rest, prev_sold)

        return max(sold, rest)