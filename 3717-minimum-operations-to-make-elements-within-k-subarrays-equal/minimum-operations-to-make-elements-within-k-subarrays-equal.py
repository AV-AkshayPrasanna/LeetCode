class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        v = sorted(set(nums))
        m = len(v)
        r = {a: i + 1 for i, a in enumerate(v)}
        c = [0] * (m + 1)
        s = [0] * (m + 1)
        L = m.bit_length()
        def upd(i, d, e):
            while i <= m:
                c[i] += d
                s[i] += e
                i += i & -i
        w = []
        t = 0
        for i in range(n):
            upd(r[nums[i]], 1, nums[i])
            t += nums[i]
            if i >= x:
                upd(r[nums[i - x]], -1, -nums[i - x])
                t -= nums[i - x]
            if i >= x - 1:
                q = (x + 1) // 2
                p = 0
                for b in range(L, -1, -1):
                    np = p + (1 << b)
                    if np <= m and c[np] < q:
                        p = np
                        q -= c[np]
                md = v[p]
                j = p + 1
                cl = sl = 0
                while j > 0:
                    cl += c[j]
                    sl += s[j]
                    j -= j & -j
                w.append(md * cl - sl + t - sl - md * (x - cl))
        inf = float("inf")
        f = [0] * (n + 1)
        for _ in range(k):
            g = [inf] * (n + 1)
            for i in range(x, n + 1):
                g[i] = min(g[i - 1], f[i - x] + w[i - x])
            f = g
        return f[n]