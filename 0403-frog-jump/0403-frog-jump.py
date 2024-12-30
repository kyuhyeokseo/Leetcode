from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        L = len(stones)
        D = {}

        for i in range(1, L):
            D[stones[i]] = []

        D[1] = [1]

        for i in range(1, L):

            if i == L-1 and len(D[stones[i]]) == 0 :
                return False
            
            des = D[stones[i]][:]
            des = list(set(des))

            #print(stones[i], des)

            for k in des :
                if (stones[i] + k-1) in D :
                    D[stones[i] + k-1].append(k-1)
                if (stones[i] + k) in D :
                    D[stones[i] + k].append(k)
                if (stones[i] + k+1) in D :
                    D[stones[i] + k+1].append(k+1)
        
        return True








