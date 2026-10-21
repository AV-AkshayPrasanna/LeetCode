class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Length 2 and unsorted: only single-character substrings are allowed
        if n == 2:
            return -1

        mn, mx = min(s), max(s)

        # Min already at the front -> sort s[1:]
        # Max already at the back  -> sort s[:-1]
        if s[0] == mn or s[-1] == mx:
            return 1

        # Two operations work if a min exists in s[:-1] or a max exists in s[1:]
        if mn in s[:-1] or mx in s[1:]:
            return 2

        # Min only at the last position and max only at the first position
        return 3