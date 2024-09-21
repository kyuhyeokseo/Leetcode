class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1 :
            return [[1]]
        
        elif numRows == 2 :
            return [[1], [1,1]]
        
        out = [[1], [1,1]]
        
        for level in range(3, numRows+1):
            
            last = out[-1]
            
            tmp = [1]
            for i in range(len(last)-1):
                tmp.append(last[i] + last[i+1])
            tmp.append(1)
            
            out.append(tmp[:])
        
        return out
            
        
        
        
        
        
        