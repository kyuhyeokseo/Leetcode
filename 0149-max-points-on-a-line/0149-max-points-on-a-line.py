class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        L = len(points)
        
        if L == 1 :
            return 1
        
        out = 0
        memo = {}
        
        for i in range(L-1):
            
            x1, y1 = points[i]
            
            
            for j in range(i+1, L):
                x2, y2 = points[j]
        
                if x1 == x2 :
                    a = 'inf'
                else :
                    a = (y2-y1) / (x2-x1)
                
                if (a,i) in memo :
                    cnt = memo[(a,i)]
                    del memo[(a,i)]
                    memo[(a,j)] = cnt + 1
                    out = max(out, cnt+1)
                    
                else :
                    memo[(a,j)] = 2
                    out = max(out, 2)
                
        
        return out
        