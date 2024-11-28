

class Twitter:


    def __init__(self):
        
        self.id = 0
        self.post = {}
        self.f_d = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.post :
            self.post[userId].append([self.id, tweetId])
        else :
            self.post[userId] = [[self.id, tweetId]]
        self.id += 1
        
        #print(self.post)
        #print(self.f_d)

    def getNewsFeed(self, userId: int) -> List[int]:
        
        P = []
        if userId in self.f_d :
            U = [userId] + list(self.f_d[userId])
        else :
            U = [userId]
            
        for u in U :
            if u in self.post:
                P += self.post[u]
            
        P.sort()
        P_ID = []
        
        for i in range(min(10, len(P))):
            P_ID.append(P[-(i+1)][1])
            
        #print(P_ID)
        #print(self.post)
        #print(self.f_d)
        
        return P_ID
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.f_d :
            self.f_d[followerId].add(followeeId)
        else :
            self.f_d[followerId] = set()
            self.f_d[followerId].add(followeeId)
        
        #print(self.post)
        #print(self.f_d)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.f_d and followeeId in self.f_d[followerId] :
            self.f_d[followerId].remove(followeeId)

        #print(self.post)
        #print(self.f_d)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)