from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                result += len(distinct) ** 2

        return result