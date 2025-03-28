class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        N = len(ring)
        D = {}
        srts  = []
        costs = []
        for i, r in enumerate(ring):
            if r in D:
                D[r].append(i)
            else:
                D[r] = [i]
            if r == key[0]:
                srts.append(i)
                costs.append(min(i, N-i)+1)
        
        for idx in range(1, len(key)):
            new_srts = D[key[idx]][:]
            new_costs = []

            for new in new_srts:
                tmp = 10 ** 5
                for i, srt in enumerate(srts):
                    tmp = min(abs(new-srt)+costs[i], N-abs(new-srt)+costs[i], tmp)
                new_costs.append(tmp+1)
            
            srts  = new_srts[:]
            costs = new_costs[:]
        
        return min(costs)
        
        
        
