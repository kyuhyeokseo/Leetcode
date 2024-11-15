class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3 :
            return False
        
        MIN1, MIN2 = None, None
        THRE = None
        
        for n in nums:
            
            if THRE is not None and THRE < n :
                return True
            
            if MIN1 is None :
                MIN1 = n
            
            elif MIN1 is not None and MIN2 is None :
                if n < MIN1 :
                    MIN1 = n
                elif n > MIN1 :
                    MIN2 = n
                    if THRE is None :
                        THRE = n
                    else :
                        THRE = min(n, THRE)
            
            else :
                if n < MIN1 :
                    MIN1 = n
                    MIN2 = None
                elif n > MIN1 and n < MIN2 :
                    MIN2 = n
                    if THRE is None :
                        THRE = n
                    else :
                        THRE = min(n, THRE)
            
            #print(n, MIN1, MIN2, THRE)
        
        return False
            
            
            
                
        
        
        
        
        
        