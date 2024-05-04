class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        x,y = newInterval
            
        ans = []
        p, q = x,y
        for j in range(len(intervals)):
            X, Y = intervals[j]
            if (x-X) * (y-X) <= 0 or (x-Y) * (y-Y) <= 0 or (X<=x and y<=Y) :
                p = min(p, X)
                q = max(q, Y)
            else :
                ans.append([X,Y])
        
        ans.append([p,q])
        ans.sort()

        return ans
        
        
        
        
        
        
        
        
        
        
        