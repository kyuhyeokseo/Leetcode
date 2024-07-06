class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        N = 2*n - 1
        self.MAX = n
        
        self.save = [["(", 1, 0]]
        self.out = []
        
        for _ in range(N):
            self.nextStep()
        
        return self.out
        
    def nextStep(self) :
        
        tmp = self.save[:]
        self.save = []
        
        for X in tmp :
            item, o, c = X[0], X[1], X[2]
            
            if X[1] == self.MAX :
                self.save.append([item+")", X[1], X[2]+1])
                
                if X[2]+1 == self.MAX :
                    self.out.append(item+")")
                
            elif X[1] > X[2] :
                self.save.append([item+"(", X[1]+1, X[2]])    
                if X[1]+1 == self.MAX and X[2] == self.MAX:
                    self.out.append(item+"(")
                self.save.append([item+")", X[1], X[2]+1])
                if X[1] == self.MAX and X[2]+1 == self.MAX:
                    self.out.append(item+")")
                    
            elif X[1] == X[2] :
                self.save.append([item+"(", X[1]+1, X[2]])
                if X[1]+1 == self.MAX and X[2] == self.MAX:
                    self.out.append(item+"(")
        