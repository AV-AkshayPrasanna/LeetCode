from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        s = [0] * (4 * n)   # sum of d[i] in the node's range
        sq = [0] * (4 * n)  # sum of d[i]^2 in the node's range
        lz = [0] * (4 * n)  # pending range-add

        def apply(o, length, x):
            # update sq first: it needs the old s[o]
            sq[o] = (sq[o] + 2 * x * s[o] + x * x * length) % MOD
            s[o] = (s[o] + x * length) % MOD
            lz[o] += x

        def update(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(o, r - l + 1, 1)
                return
            m = (l + r) // 2
            if lz[o]:
                apply(2 * o, m - l + 1, lz[o])
                apply(2 * o + 1, r - m, lz[o])
                lz[o] = 0
            if ql <= m:
                update(2 * o, l, m, ql, qr)
            if qr > m:
                update(2 * o + 1, m + 1, r, ql, qr)
            s[o] = (s[2 * o] + s[2 * o + 1]) % MOD
            sq[o] = (sq[2 * o] + sq[2 * o + 1]) % MOD

        last = {}
        ans = 0
        for j, v in enumerate(nums):
            update(1, 0, n - 1, last.get(v, -1) + 1, j)
            last[v] = j
            ans = (ans + sq[1]) % MOD
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumCounts([1, 2, 1]))  # 15
    print(sol.sumCounts([2, 2]))     # 3