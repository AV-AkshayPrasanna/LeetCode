class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def check(a, b, start):
            while start < n:
                total = str(a + b)

                if not num.startswith(total, start):
                    return False

                start += len(total)
                a, b = b, a + b

            return True

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break

            a = int(num[:i])

            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                b = int(num[i:j])

                if check(a, b, j):
                    return True

        return False