class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xorN = 0
        
        for num in nums :
            xorN = xorN ^ num
        
        finddiff = 1
        while finddiff & xorN == 0 :
            finddiff = (finddiff << 1)
        
        x,y = 0,0
        for num in nums :
            if finddiff & num == 0 :
                x = x ^ num
            else :
                y = y ^ num
        
        return [x,y]
        
                
        