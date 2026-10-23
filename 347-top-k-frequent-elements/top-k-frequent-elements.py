from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        return [x for x, _ in Counter(nums).most_common(k)]