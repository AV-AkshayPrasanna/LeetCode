from collections import defaultdict
from heapq import nlargest

class Twitter:
    def __init__(self):
        self.t = 0
        self.p = defaultdict(list)
        self.f = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.t += 1
        self.p[userId].append((self.t, tweetId))

    def getNewsFeed(self, userId):
        a = []
        for u in self.f[userId] | {userId}:
            a += self.p[u][-10:]
        return [x for _, x in nlargest(10, a)]

    def follow(self, followerId, followeeId):
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.f[followerId].discard(followeeId)