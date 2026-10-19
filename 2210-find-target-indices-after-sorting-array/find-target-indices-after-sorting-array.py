class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = equal = 0
        for n in nums:
            if n < target:
                less += 1
            elif n == target:
                equal += 1
        return list(range(less, less + equal))