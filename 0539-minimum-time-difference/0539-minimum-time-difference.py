class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        timePoints.sort()
        ret = 720

        first = list(map(int, timePoints[0].split(':')))
        tmp = f'{first[0] + 24}:{first[1]}'
        timePoints.append(tmp)

        L = len(timePoints)

        tmps = []
        for i in range(L):
            tmps.append(list(map(int, timePoints[i].split(':'))))

        for i in range(L-1):
            prv, nxt = tmps[i], tmps[i+1]
            H1, M1, H2, M2 = prv[0], prv[1], nxt[0], nxt[1]
            
            ret = min(ret, (H2-H1) * 60 + (M2-M1))
        
        return ret