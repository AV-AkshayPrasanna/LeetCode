class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0  # nums[i] >= 1
            for s in range(0, n, k):
                # count cyclic descents inside the block
                desc = 0
                lo = hi = nums[s]
                for i in range(s, s + k):
                    nxt = nums[i + 1] if i + 1 < s + k else nums[s]
                    if nums[i] > nxt:
                        desc += 1
                        if desc > 1:
                            break
                    if nums[i] < lo: lo = nums[i]
                    if nums[i] > hi: hi = nums[i]
                if desc > 1 or lo < prev_max:
                    ok = False
                    break
                prev_max = hi
            if ok:
                ans += k
        return ans