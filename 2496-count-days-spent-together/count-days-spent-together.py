class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        d = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        f = lambda s: d[int(s[:2]) - 1] + int(s[3:])
        return max(0, f(min(leaveAlice, leaveBob)) - f(max(arriveAlice, arriveBob)) + 1)