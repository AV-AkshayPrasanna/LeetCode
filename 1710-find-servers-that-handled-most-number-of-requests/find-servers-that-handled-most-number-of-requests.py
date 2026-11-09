import heapq
from bisect import bisect_left

class Solution:
    def busiestServers(self, k, arrival, load):
        f = list(range(k))
        b = []
        c = [0] * k
        for i, t in enumerate(arrival):
            while b and b[0][0] <= t:
                s = heapq.heappop(b)[1]
                j = bisect_left(f, s)
                f.insert(j, s)
            if not f:
                continue
            j = bisect_left(f, i % k)
            if j == len(f):
                j = 0
            s = f.pop(j)
            c[s] += 1
            heapq.heappush(b, (t + load[i], s))
        m = max(c)
        return [i for i in range(k) if c[i] == m]