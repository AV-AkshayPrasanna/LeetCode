import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
        d = {(0, 1): 0}
        h = [(0, 0, 1)]
        while h:
            c, u, r = heapq.heappop(h)
            if d.get((u, r), 1e18) < c:
                continue
            if u == n - 1:
                return c
            for v, w in g[u]:
                nr = r + 1 if labels[v] == labels[u] else 1
                if nr > k:
                    continue
                nc = c + w
                if nc < d.get((v, nr), 1e18):
                    d[(v, nr)] = nc
                    heapq.heappush(h, (nc, v, nr))
        return -1