"""
There are a few things at play here:

1. I need a user object that tracks who the user is following. In a real implementation of this, I might also include
   a way to track who is following the user, but that information is not useful in this simplified problem

2. What is a tweet in the context of this problem? A tweet in this problem is just a tweetId that needs to be returned
   from the getNewsFeed function

3. "Posting" a tweet therefore means recording the tweetId in some data structure. Since the only function that returns
   anything is the getNewsFeed function, and that function has a time component to it, I can record tweets with an
   ID that represents when they were posted. For example, a tweetId with an ID of 1 was posted before a tweet with an
   ID of 2.

4. The newsfeed needs to also get tweets from posted by other users the user follows, meaning the counter that represents
   "time" should be stored on the Twitter object itself as a static variable of sorts

5. With this in mind, the algorithmic complexity of this problem comes from efficiently finding the 10 most recent tweets
   from the user as well as other users the current user follows. I can use a max heap to create a priority queue and track
   tweets based on when they were posted (with the "time" coming from the counter stored in the Twitter object). When
   building a new feed, I iterate through the users tweets, as well as every user they follow. For each iteration, I add
   the most recent tweet from each user to a max heap. Then, I take the most recent tweet from this max heap and add it
   to my new feed object, which in this case is just a list. Finally, since I need to remove tweets from each users heap
   to build the news feed, I need to then add them back. I can use a hashmap where each key is the userId and each value
   is the array of their tweets processed to build this newsfeed.

   The main loop for this will run 10 times, i.e., constant time complexity. If there are n users, I will process at most 10
   of their tweets. If each user has tweeted t times, this algorithm has a runtime complexity of O(nlog(t)), with a memory
   complexity of O(10n) == O(n) (because we are storing at most 10 tweets for each user)

   time: O(nlog(t))
   memory: O(n)
"""
import heapq

class User:
    """
    User object tracks who the user is following as well as what tweets this user has created
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.followed_users = {}
        self.tweets = []
        heapq.heapify(self.tweets)
    
    def postTweet(self, tweet):
        """
        Called by main Twitter object to record a tweet made by the user. The tweet object is a tuple that has the "time"
        the tweet was made along with the tweetId itself, i.e., (time, ID)
        """
        heapq.heappush(self.tweets, tweet)
    
    def getTweet(self):
        """
        Returns the most recent tweet the user made
        """
        return heapq.heappop(self.tweets) if len(self.tweets) > 0 else None
    
    def follow(self, followee_id, followee):
        """
        Called by main Twitter object when this user follows another user.
        """
        self.followed_users[followee_id] = followee
    
    def unFollow(self, followee_id):
        """
        Called by main Twitter object when this user unfollows the user with followee_id
        """
        self.followed_users.pop(followee_id)


class Twitter:

    def __init__(self):
        """
        This object needs to store a global counter used to represent the time when a tweet was posted, as well as
        a map of user_ids -> user objects
        """
        self.time = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Creates a tweet object which is a tuple of (time, tweetId) and assign it to the users tweet heap. Creates the
        user if they don't exist
        """
        user = None
        if userId not in self.users.keys():
            user = User(userId)
            self.users[userId] = user
        else:
            user = self.users[userId]

        # Negate time so heap is a max heap
        user.postTweet((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Iterate through the users tweet list as well as every user they follow's tweet list. On each iteration, store each
        tweet in a max heap and take the top most value (the most recent tweet) as part of the new feed
        """
        news_feed = []
        user = self.users[userId]
        follow_list = user.followed_users
        most_recent_tweet = []
        heapq.heapify(most_recent_tweet)
        for _ in range(10):
            tweet = user.getTweet()
            # Store information as (time, (tweetId, userId))
            if tweet:
                heapq.heappush(most_recent_tweet, (tweet[0], (tweet[1], userId)))
            for u_id in follow_list.keys():
                u = follow_list[u_id]
                tweet = u.getTweet()
                if tweet:
                    heapq.heappush(most_recent_tweet, (tweet[0], (tweet[1], u_id)))
            # Take the most recent tweet and add it to the result. Remember to negate to undo previous negation
            news_feed.append(most_recent_tweet[0][1][1])
        # Rebuild each users tweet list
        while len(most_recent_tweet) > 0:
            tweet_info = heapq.heappop(most_recent_tweet)
            u_id = tweet_info[1][1]
            if u_id == userId:
                user.postTweet((tweet_info[0], tweet_info[1][0]))
            else:
                follow_list[u_id].postTweet((tweet_info[0], tweet_info[1][0]))
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Assignes the followeeId to the followerId User's follow list. Creates an object for follower and followee if
        they don't exist
        """
        follower = None
        followee = None
        if followerId not in self.users.keys():
            follower = User(followerId)
        else:
            follower = self.users[followerId]
        if followeeId not in self.users.keys():
            followee = User(followeeId)
        else:
            followee = self.users[followeeId]
        
        follower.follow(followeeId, followee)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        followerId stopped following followeeId
        """
        self.users[followerId].unFollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
