class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        L = len(columnTitle)
        N = 0
        
        for i in range(L):
            N *= 26
            N += (ord(columnTitle[i]) - ord('A') + 1)
            
        return N