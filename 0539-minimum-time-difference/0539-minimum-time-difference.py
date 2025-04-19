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
            v = list(map(int, timePoints[i].split(':')))
            H, M = v[0], v[1]
            tmps.append(60 * H + M)

        for i in range(L-1):
            
            ret = min(ret, tmps[i+1] - tmps[i])
        
        return ret