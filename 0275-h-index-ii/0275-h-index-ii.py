class Solution:
    
    def __init__(self):
        self.citations = []
        self.L = 0
    
    def hIndex(self, citations: List[int]) -> int:
        self.citations = citations
        self.L = len(citations)
        
        H = self.findHindex(0, self.L-1)
        
        return H
        
        
    def findHindex(self, i, j):
        
        if i==j :
            if self.citations[i] >= self.L - i :
                return 1
            else :
                return 0
    
        k = (i+j+1)//2
        
        if self.citations[k] >= self.L - k :
            H = j - k + 1 + self.findHindex(i, k-1)
        else :
            H = self.findHindex(k, j)
            
        #print(self.citations[i:j+1], ' : ', H)
        return H