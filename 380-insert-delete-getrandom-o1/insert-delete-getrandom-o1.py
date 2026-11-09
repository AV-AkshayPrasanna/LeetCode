import random

class RandomizedSet:
    def __init__(self):
        self.a = []
        self.m = {}

    def insert(self, val):
        if val in self.m:
            return False
        self.m[val] = len(self.a)
        self.a.append(val)
        return True

    def remove(self, val):
        if val not in self.m:
            return False
        i = self.m.pop(val)
        x = self.a.pop()
        if i < len(self.a):
            self.a[i] = x
            self.m[x] = i
        return True

    def getRandom(self):
        return random.choice(self.a)