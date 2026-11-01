class Solution:
    def getSum(self, a, b):
        m = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & m, ((a & b) << 1) & m
        return a if a < 0x80000000 else ~(a ^ m)