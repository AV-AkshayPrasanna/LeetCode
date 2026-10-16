from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {w: i for i, w in enumerate(words)}
        res = []

        def is_pal(s: str) -> bool:
            return s == s[::-1]

        for i, w in enumerate(words):
            n = len(w)
            for k in range(n + 1):
                left, right = w[:k], w[k:]

                # left is a palindrome -> reverse(right) + w
                if is_pal(left):
                    j = index.get(right[::-1])
                    if j is not None and j != i:
                        res.append([j, i])

                # right is a palindrome -> w + reverse(left)
                # k < n skips the empty-right split, already covered above
                if k < n and is_pal(right):
                    j = index.get(left[::-1])
                    if j is not None and j != i:
                        res.append([i, j])

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(sol.palindromePairs(["bat", "tab", "cat"]))
    print(sol.palindromePairs(["a", ""]))