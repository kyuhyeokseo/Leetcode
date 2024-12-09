import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        q = []
        N = len(matrix)
        
        for i in range(N):
            heapq.heappush(q, (matrix[i][0], i, 0))
        
        for _ in range(k):
            out = heapq.heappop(q)
            j, idx = out[1], out[2]
            if idx != N-1 :
                heapq.heappush(q, (matrix[j][idx+1], j, idx+1))
        
        return out[0]
            
        
        
        
        
        