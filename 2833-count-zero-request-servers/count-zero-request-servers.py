class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        c = [0] * (n + 1)
        r = [0] * len(queries)
        a = b = 0
        z = n
        for t, i in sorted((q, i) for i, q in enumerate(queries)):
            while b < len(logs) and logs[b][1] <= t:
                s = logs[b][0]
                if c[s] == 0:
                    z -= 1
                c[s] += 1
                b += 1
            while a < len(logs) and logs[a][1] < t - x:
                s = logs[a][0]
                c[s] -= 1
                if c[s] == 0:
                    z += 1
                a += 1
            r[i] = z
        return r