class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.A = [[] for _ in range(numCourses)]
        self.B = [[] for _ in range(numCourses)]
        self.loop = False
        
        if len(prerequisites) == 0 :
            return range(numCourses)
        
        for pre in prerequisites :
            self.A[pre[1]].append(pre[0])
            self.B[pre[0]].append(pre[1])
        
        check = [False for _ in range(numCourses)]
        ans = []
        
        for _ in range(numCourses) :
            for i in range(numCourses) :
                if len(self.B[i]) == 0 and check[i] == False :
                    check[i] = True
                    ans.append(i)
                    for j in self.A[i] :
                        self.B[j].remove(i)
        
        if len(ans) == numCourses :
            return ans
        else :
            return []
        
        
        
        
        