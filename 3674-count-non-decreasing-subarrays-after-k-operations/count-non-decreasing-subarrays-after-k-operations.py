from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        P = [0]
        for x in nums:
            P.append(P[-1] + x)
        q = deque()
        c = 0
        r = n - 1
        res = 0
        for l in range(n - 1, -1, -1):
            x = nums[l]
            e = l
            while q and q[0][2] <= x:
                s, t, v = q.popleft()
                c -= v * (t - s + 1) - (P[t + 1] - P[s])
                e = t
            q.appendleft([l, e, x])
            c += x * (e - l + 1) - (P[e + 1] - P[l])
            while c > k:
                c -= q[-1][2] - nums[r]
                q[-1][1] -= 1
                if q[-1][1] < q[-1][0]:
                    q.pop()
                r -= 1
            res += r - l + 1
        return res