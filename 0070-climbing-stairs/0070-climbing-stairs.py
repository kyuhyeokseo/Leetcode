class Solution:
    def climbStairs(self, n: int) -> int:
            
        record = []
        
        for i in range(n):
            if i == 0 :
                record.append(1)
            elif i == 1 :
                record.append(2)
            else :
                record.append(record[i-1] + record[i-2])
        
        return record[n-1]
        
        
        
        
        
        