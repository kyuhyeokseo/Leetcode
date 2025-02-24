class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        self.matchsticks = matchsticks
        self.matchsticks.sort(reverse=True)
        self.set = set()

        L = 0
        for s in matchsticks :
            L += s
        if L % 4 > 0 :
            return False
        
        L = L // 4
        return self.findSquare([L,L,L,L], 0)
    

    def findSquare(self, target_list, idx):
        #print('Call : ', target_list, idx)
        
        if idx >= len(self.matchsticks):
            for t in target_list :
                if t != 0 :
                    return False
            return True

        s = set()

        for i in range(4):

            if target_list[i] in s:
                continue

            s.add(target_list[i])
            if target_list[i] - self.matchsticks[idx] >= 0 :
                tmp = target_list[:]
                tmp[i] -= self.matchsticks[idx]
                result = self.findSquare(tmp, idx+1)

                if result :
                    return True

        return False


