import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        f = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(f)
        b = []
        r = []
        t = 0
        for j, d in enumerate(tasks):
            t = max(t, j)
            if not f:
                t = max(t, b[0][0])
            while b and b[0][0] <= t:
                e, w, i = heapq.heappop(b)
                heapq.heappush(f, (w, i))
            w, i = heapq.heappop(f)
            r.append(i)
            heapq.heappush(b, (t + d, w, i))
        return r