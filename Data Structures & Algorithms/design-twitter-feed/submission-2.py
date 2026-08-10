import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        tweets = []

        for tweet in self.tweets[userId]:
            maxHeap.append(tweet)
        
        for followeeId in self.following[userId]:
            for tweet in self.tweets[followeeId]:
                maxHeap.append(tweet)
        
        heapq.heapify(maxHeap)
        
        
        while maxHeap and len(tweets) < 10:
            time, tweet = heapq.heappop(maxHeap)
            tweets.append(tweet)


        return tweets
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
