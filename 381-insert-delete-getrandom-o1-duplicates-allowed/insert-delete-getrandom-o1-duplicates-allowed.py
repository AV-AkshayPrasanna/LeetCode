import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.a = []
        self.m = defaultdict(set)

    def insert(self, val):
        r = not self.m[val]
        self.m[val].add(len(self.a))
        self.a.append(val)
        return r

    def remove(self, val):
        if not self.m[val]:
            return False
        i = self.m[val].pop()
        x = self.a[-1]
        self.a[i] = x
        self.m[x].add(i)
        self.m[x].discard(len(self.a) - 1)
        self.a.pop()
        return True

    def getRandom(self):
        return random.choice(self.a)