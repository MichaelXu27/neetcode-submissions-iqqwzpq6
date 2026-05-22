class Twitter:

    def __init__(self):
        self.time = 0
        self.user_map = defaultdict(set) #user to dic of userIds that the person follows
        self.user_posts = defaultdict(list) # user to their posts
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        merged = []

        users = set(self.user_map[userId])
        users.add(userId)

        for user in users:
            for post in self.user_posts[user]:
                heapq.heappush(merged, (-post[0], post[1]))
        
        ret = []
        while merged and len(ret) < 10:
            _, tweetId = heapq.heappop(merged)
            ret.append(tweetId)

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_map[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)