class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        L = len(nums)
        
        tmp = [0 for _ in range(32)]
        
        for num in nums :
            
            num += (2<<31)
            
            i = 0
            
            while num > 0 :
                R = num % 3
                tmp[i] += R
                tmp[i] %= 3
                
                i+= 1
                num = num //3
                
        out = 0
        for i in range(32) :
            out += tmp[31-i]
            if i < 31 :
                out *= 3
        
        out -= (2<<31)
        
        return out