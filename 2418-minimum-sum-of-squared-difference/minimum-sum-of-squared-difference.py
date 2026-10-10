from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        for i in range(len(diff) - 1):
            cost = (diff[i] - diff[i + 1]) * (i + 1)

            if k >= cost:
                k -= cost
            else:
                level = diff[i] - k // (i + 1)
                remainder = k % (i + 1)
                return (
                    sum(d * d for d in diff[i + 1:])
                    + remainder * (level - 1) ** 2
                    + (i + 1 - remainder) * level ** 2
                )

        return 0