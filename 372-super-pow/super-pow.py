class Solution:
    def superPow(self, a, b):
        r = 1
        for d in b:
            r = pow(r, 10, 1337) * pow(a, d, 1337) % 1337
        return r