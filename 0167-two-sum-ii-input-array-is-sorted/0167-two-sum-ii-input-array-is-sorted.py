class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = len(numbers)
        
        for i in range(L):
            if i>0 and numbers[i] == numbers[i-1] :
                    continue
                    
            for j in range(i+1, L) :
                
                if j>i+1 and numbers[j] == numbers[j-1] :
                    continue
                
                if numbers[i] + numbers[j] == target :
                    return [i+1, j+1]
        
        
        
        
        
        
        