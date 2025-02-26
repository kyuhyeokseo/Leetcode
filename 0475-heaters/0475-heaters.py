class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        M, N = len(houses), len(heaters)

        houses.sort()
        heaters.sort()
        
        ret = -1

        i,j = -1, 0

        for x in range(M):
            
            house = houses[x]

            while (i <= -1 and house > heaters[j]) or (i >= 0 and j < N and (heaters[i] > house or house > heaters[j])) or (j >= N and house < heaters[i]):
                i += 1
                j += 1

            if i == -1 :
                ret = max(ret, abs(heaters[j]-house))
            elif (i >= 0 and j < N) :
                ret = max(ret, min(abs(heaters[i]-house) ,abs(heaters[j]-house)))
            else :
                ret = max(ret, abs(heaters[i]-house))
        
        return ret