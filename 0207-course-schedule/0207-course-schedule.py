class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.A = [[] for _ in range(numCourses)]
        self.loop = False
        
        if len(prerequisites) == 0 :
            return True
        
        for pre in prerequisites :
            self.A[pre[1]].append(pre[0])
        
        for idx in range(numCourses) :
            
            self.target = idx
            self.check = [False for _ in range(numCourses)]
            self.dfs(idx)
            
            if self.loop == True :
                return False
        
        return True
        
        
    def dfs(self, idx) :
        
        self.check[idx] = True
        for nei in self.A[idx] :
            if nei == self.target :
                self.loop = True
            
            if self.check[nei] == False :
                self.dfs(nei)
        