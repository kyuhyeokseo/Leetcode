class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        

        N = len(isConnected)
        visited = [False] * N
        cnt = 0

        for i in range(N):
            if visited[i] == False:
                cnt += 1
                visited[i] = True
                dfs(i)
        
        return cnt
            
                    
