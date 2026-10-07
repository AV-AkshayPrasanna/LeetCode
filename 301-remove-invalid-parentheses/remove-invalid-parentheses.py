from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()

        def remove(s, start, last, left, right):
            balance = 0

            for i in range(start, len(s)):
                if s[i] == left:
                    balance += 1
                elif s[i] == right:
                    balance -= 1

                if balance >= 0:
                    continue

                for j in range(last, i + 1):
                    if s[j] == right and (j == last or s[j - 1] != right):
                        remove(
                            s[:j] + s[j + 1:],
                            i,
                            j,
                            left,
                            right
                        )
                return

            reversed_s = s[::-1]

            if left == '(':
                remove(reversed_s, 0, 0, ')', '(')
            else:
                result.add(reversed_s)

        remove(s, 0, 0, '(', ')')
        return list(result)