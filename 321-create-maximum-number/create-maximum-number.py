from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums, t):
            drop = len(nums) - t
            stack = []

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:t]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        best = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = pick_max(nums1, i)
            b = pick_max(nums2, k - i)
            candidate = merge(a, b)

            if candidate > best:
                best = candidate

        return best