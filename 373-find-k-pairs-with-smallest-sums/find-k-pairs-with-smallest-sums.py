import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        h = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(h)
        r = []
        while h and len(r) < k:
            _, i, j = heapq.heappop(h)
            r.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return r