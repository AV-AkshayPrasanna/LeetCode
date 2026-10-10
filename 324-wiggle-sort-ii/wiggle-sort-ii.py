from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        arr = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2

        small = arr[:mid][::-1]
        large = arr[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large