import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        M, N = len(heightMap), len(heightMap[0])
        if M*N == 0 :
            return 0
        
        q = []
        visited = [[False for _ in range(N)] for _ in range(M)]

        for m in range(M):
            for n in range(N):
                if m == 0 or n == 0 or m == M-1 or n == N-1 :
                    heapq.heappush(q, (heightMap[m][n], m, n))
                    visited[m][n] = True
        
        ret = 0

        while q :
            H, x, y = heapq.heappop(q)
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0<= x+dx <= M-1 and 0<= y+dy <= N-1 and visited[x+dx][y+dy] == False :
                    ret += max(0, H-heightMap[x+dx][y+dy])
                    heapq.heappush(q, (max(H, heightMap[x+dx][y+dy]), x+dx, y+dy))
                    visited[x+dx][y+dy] = True
        
        return ret


        



