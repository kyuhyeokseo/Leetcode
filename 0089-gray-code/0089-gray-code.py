class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 1 :
            return [0,1]
        
        
        out = [0,1]
        for x in range(1,n):
            
            tmp = out[:]
            
            for i in range(len(tmp)):
                out.append((1<<x) + tmp[-i-1])
        
        return out
            