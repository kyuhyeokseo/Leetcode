class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.n = n
        self.visited = []
        
        self.cnt = 0
        
        for i0 in range(n) :
            self.visited.append(i0)
            self.queens()
            self.visited = []
            
        return self.cnt
            
    def queens(self):
        if len(self.visited) == self.n :
            self.cnt += 1
        else :
            L = len(self.visited)
            available = [True for _ in range(self.n)]
            for j in range(L) :
                for idx in [self.visited[j], self.visited[j]-(L-j), self.visited[j]+(L-j)]:
                    if 0<=idx and idx<self.n:
                        available[idx] = False
            
            for i in range(self.n) :
                if available[i] :
                    self.visited.append(i)
                    self.queens()
                    self.visited = self.visited[:-1]
        
    
        
        
        
        
        
        
        
        
        