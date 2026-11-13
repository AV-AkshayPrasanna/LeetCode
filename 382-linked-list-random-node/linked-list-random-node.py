import random

class Solution:
    def __init__(self, head):
        self.h = head

    def getRandom(self):
        r = 0
        n = 0
        p = self.h
        while p:
            n += 1
            if random.randrange(n) == 0:
                r = p.val
            p = p.next
        return r