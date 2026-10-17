class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # indices ordered by (digit sum, value) -> target arrangement
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))

        # order[j] = original index of the element that belongs at position j
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = order[j]
        return n - cycles