class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        s = list(s)
        par = [0] * n
        dep = [0] * n
        tin = [0] * n
        sz = [1] * n
        order = []
        st = [0]
        seen = [False] * n
        seen[0] = True
        while st:
            u = st.pop()
            tin[u] = len(order)
            order.append(u)
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    par[v] = u
                    dep[v] = dep[u] + 1
                    st.append(v)
        for u in reversed(order):
            if u:
                sz[par[u]] += sz[u]
        L = 16
        up = [par]
        for k in range(1, L):
            p = up[-1]
            up.append([p[p[i]] for i in range(n)])
        t = [0] * (n + 2)
        def add(i, x):
            i += 1
            while i <= n + 1:
                t[i] ^= x
                i += i & -i
        def get(i):
            i += 1
            r = 0
            while i > 0:
                r ^= t[i]
                i -= i & -i
            return r
        def rng(u, x):
            add(tin[u], x)
            add(tin[u] + sz[u], x)
        def lca(a, b):
            if dep[a] < dep[b]:
                a, b = b, a
            d = dep[a] - dep[b]
            for k in range(L):
                if d >> k & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(L - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return par[a]
        for i in range(n):
            rng(i, 1 << (ord(s[i]) - 97))
        r = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u = int(p[1])
                rng(u, (1 << (ord(s[u]) - 97)) ^ (1 << (ord(p[2]) - 97)))
                s[u] = p[2]
            else:
                a, b = int(p[1]), int(p[2])
                l = lca(a, b)
                m = get(tin[a]) ^ get(tin[b]) ^ (1 << (ord(s[l]) - 97))
                r.append(m & (m - 1) == 0)
        return r