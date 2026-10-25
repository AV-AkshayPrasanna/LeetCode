from bisect import bisect_left

class SummaryRanges:
    def __init__(self):
        self.a = []

    def addNum(self, value):
        a = self.a
        i = bisect_left(a, [value])
        if i > 0 and a[i-1][1] >= value:
            return
        if i < len(a) and a[i][0] == value:
            return
        l = i > 0 and a[i-1][1] == value - 1
        r = i < len(a) and a[i][0] == value + 1
        if l and r:
            a[i-1][1] = a[i][1]
            a.pop(i)
        elif l:
            a[i-1][1] = value
        elif r:
            a[i][0] = value
        else:
            a.insert(i, [value, value])

    def getIntervals(self):
        return self.a