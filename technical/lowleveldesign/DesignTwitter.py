from collections import defaultdict

class Tweet:
    
    def __init__(self, tweetId, userId):
        self.tweetId = tweetId
        self.userId = userId
        
class User:

    def __init__(self, userId):
        self.userId = userId
        self.tweets = list()
        self.MAX_TWEETS = 10

    def getNewsFeed(self):
        return self.tweets

    def post(self, tweetId, followers, users):

        for userId in followers:
            user = users[userId]
            user.tweets.append(tweetId)

            if len(user.tweets) > self.MAX_TWEETS:
                user.tweets.pop(0)
                
class UserService:
    
    def __init__(self):
        

class Twitter(object):

    def __init__(self):
        self.users = defaultdict(User)
        self.followers = defaultdict(list)

    def postTweet(self, userId, tweetId):
        if userId not in self.users:
            self.addUser(userId)

        self.users[userId].post(tweetId, self.followers[userId], self.users)
        
    def addUser(self, userId):
        #Create user
        self.users[userId] = User(userId)

        #Subscribe to yourself
        self.followers[userId].append(userId)

    def getNewsFeed(self, userId):
        return self.users[userId].tweets[::-1]

    def follow(self, followerId, followeeId):
        if followerId not in self.users:
            self.addUser(followerId)
            
        if followeeId not in self.users:
            self.addUser(followeeId)
            
        self.followers[followeeId].append(followerId)

    def unfollow(self, followerId, followeeId):
        self.followers[followerId].remove(followeeId)
        
twitter = Twitter()
twitter.postTweet(1, 5)
assert twitter.getNewsFeed(1)  == [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
assert twitter.getNewsFeed(1) == [6, 5]
