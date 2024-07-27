class Solution:
    def hammingWeight(self, n: int) -> int:
        
        out = 0
        #print(n)
        #print('---------------------')
        while n > 0 :
            
            #print(n)
            out += n % 2
            n = n//2
        
        #print(n)
        #print('---------------------')
        #print(out)
        
        return out
        
        
        
        
        