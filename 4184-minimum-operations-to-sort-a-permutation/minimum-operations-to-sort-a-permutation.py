from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = nums[0]
        INF = float('inf')
        ans = INF

        # Case 1: rotation of sorted
        if all(nums[i] == (k + i) % n for i in range(n)):
            if k == 0:
                ans = 0
            else:
                ans = min(ans, n - k, k + 2)

        # Case 2: rotation of reversed sorted
        if all(nums[i] == (k - i) % n for i in range(n)):
            m = (k + 1) % n
            ans = min(ans, 1 + min(m, (n - m) % n))

        return -1 if ans == INF else ans