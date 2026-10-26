from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        a = []
        for _, h in envelopes:
            i = bisect_left(a, h)
            if i == len(a):
                a.append(h)
            else:
                a[i] = h
        return len(a)