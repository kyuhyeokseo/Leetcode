import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        q1 = []
        q2 = []
        
        
        for idx in range(len(profits)) :
            P, C = profits[idx], capital[idx]
            
            q1.append((C, P))
        
        q1.sort()
        
        i = 0
        
        for _ in range(k):
            
            while i < len(profits) and q1[i][0] <= w:
                heapq.heappush(q2, -q1[i][1])
                i += 1
                
            if not q2:
                break
                
            w -= heapq.heappop(q2)

        return w
    