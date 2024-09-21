class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        elif rowIndex == 1:
            return [1,1]
        
        out = [1,1]
        
        for level in range(2, rowIndex+1):
            
            tmp = [1]
            L = len(out)
            for i in range(L-1):
                tmp.append(out[i] + out[i+1])
            tmp.append(1)
            out = tmp[:]
        
        return out