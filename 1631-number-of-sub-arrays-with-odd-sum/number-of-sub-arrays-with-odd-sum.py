class Solution:
    def numOfSubarrays(self, arr):
        e, o, p, r = 1, 0, 0, 0
        for x in arr:
            p ^= x & 1
            if p:
                r += e
                o += 1
            else:
                r += o
                e += 1
        return r % (10**9 + 7)