
class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-time.time(), tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for post in self.posts[userId]:
            heappush(heap, post)
        for user in self.following[userId]:
            for post in self.posts[user]:
                heappush(heap, post)
        cnt = 0
        ans = []
        while heap and cnt < 10:
            time, tweetId = heappop(heap)
            ans.append(tweetId)
            cnt +=1
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)